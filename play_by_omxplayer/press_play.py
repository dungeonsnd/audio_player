#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import  os

print 'Please run this script as user of root!\nUsage:\n    python press_play.py\nUse Ctrl+C to change another audio to play, Q or q to quit!\n\nList of audio file is :'
l = os.listdir('../audio')
k =0
for i in l:
	k +=1
	print "[%d] %s"%(k,i)

while True:
	index =raw_input('\nPlease input file index , Q or q to exit ^-^ ...\n')
	if index=='Q' or index=='q':
		break
		
	index =int(index)-1
	if index<0 or index>len(l):
		print 'Index error! Usage default of 1'
		index =0
	os.system('/usr/bin/omxplayer -p -o both ../audio/'+l[index])


