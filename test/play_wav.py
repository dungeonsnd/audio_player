#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""PyAudio Example: Play a WAVE file."""

# 有的 .wav 文件播放不了,报错 unknown format: 2


import pyaudio
import wave
import sys

def Run(fname):
    CHUNK = 1024
    wf = wave.open(fname, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

if __name__=='__main__':
    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit()
    fname =sys.argv[1]
    Run(fname)
    
