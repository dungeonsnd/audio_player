#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import sys
import os
import player


def Run(fname):
    ext =os.path.splitext(fname)[1]
    if '.mp3'==ext or '.wav'==ext: 
        player.Run(fname,ext[1:])
    else:
        print 'Format <%s> of <%s> unsupported temproraly!'%(ext,fname)

if __name__=='__main__':
    try:
        fname =None
        if len(sys.argv) < 2:
            print("Usage:\n   %s filename.mp3 [.wav]" % sys.argv[0])            
            fname =raw_input('Please input filename to play: \n')
        else:
            fname =sys.argv[1]
        if not os.path.isfile(fname):
            print '[Warning]: File <%s> not exist!'%(fname)
            sys.exit()
        Run(fname)
    except Exception as e:
        print e
