#!/bin/python
from os import listdir 
from os import remove
from os import getcwd as cwd
from os import path

import subprocess

getpath = cwd()
tracks = [f for f in listdir(getpath) if f.endswith('.m4a')]

for i in tracks:
	input = getpath+"\\"+i
	remove(input)
	#output = getpath+"\\"+i[:-3]
	#output = output+"mp3"
	#subprocess.run(["ffmpeg", "-i", input, output])
