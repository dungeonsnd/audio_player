#!/bin/python 
# -*- coding:utf-8 -*-

from distutils.core import setup
import py2exe

options = {"py2exe":{"compressed": 1,
                    "optimize": 2,
                    "bundle_files": 1,
                    "dll_excludes": ["w9xpopen.exe"],
                    "includes":["pymedia.muxer", "pymedia.audio.acodec"]
            }}

# window or console
setup(version = "0.1",
    name = "audioplayer",
    description = "audio player",
    console =["audioplayer.py"],
    options=options,
    zipfile=None)
