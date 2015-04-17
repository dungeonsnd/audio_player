#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import sys

def Run(fname,ext):
    f =None 
    data =None 
    frames =[]

    print time.strftime(u'%Y%m%d %H:%M:%S')

    #尝试读取前n个字节,直到成功
    import pymedia.muxer as muxer
    i =512
    step =1
    while len(frames)<1:
        if f:
            f.close()
        step *=2
        i +=step
        print 'i=%d,step=%d'%(i,step)
        #1.二进制方法读取前n个字节，保证能读到第一帧音频数据
        f = open( fname, 'rb' ) 
        data= f.read(i)

        #2.创建合成器对象，解析出最初的几帧音频数据
        dm = muxer.Demuxer(ext)
        #print 'dm=',dm
        frames = dm.parse( data )
        #print 'frames=',frames
        

    print time.strftime(u'%Y%m%d %H:%M:%S')

    #3.根据解析出来的 Mp3 编码信息，创建解码器对象
    import pymedia.audio.acodec as acodec
    dec = acodec.Decoder( dm.streams[ 0 ] )

    #像下面这样也行
    #params = {'id': acodec.getCodecID('mp3'), 'bitrate': 128000, 'sample_rate': 44100, 'ext': 'mp3', 'channels': 2}
    #dec= acodec.Decoder(params)

    #4.解码第一帧音频数据
    frame = frames[0]
    #音频数据在 frame 数组的第二个元素中
    r= dec.decode( frame[ 1 ] )
    print "sample_rate:%s , channels:%s " % (r.sample_rate,r.channels)
    #注意：这一步可以直接解码 r=dec.decode( data)，而不用读出第一帧音频数据
    #但是开始会有一下噪音，如果是网络流纯音频数据，不包含标签信息，则不会出现杂音

    #5.创建音频输出对象
    import pymedia.audio.sound as sound
    snd = sound.Output( r.sample_rate, r.channels, sound.AFMT_S16_LE )
    print 'sound.Output=',sound.Output

    #6.播放
    if r: snd.play(r.data)

    #7.继续读取、解码、播放
    while True:
        data = f.read(32)
        if len(data)>0:
            r = dec.decode( data )
            if r: snd.play( r.data )
        else:
            break

    print time.strftime(u'%Y%m%d %H:%M:%S')
    #8.延时，直到播放完毕
    while snd.isPlaying(): time.sleep( .5 )
    print time.strftime(u'%Y%m%d %H:%M:%S')

