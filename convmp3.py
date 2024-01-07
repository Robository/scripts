#!/bin/python
from os import listdir 
from os import system
from os import getcwd as cwd
from time import sleep
from os import path

import subprocess

getpath = cwd()
tracks = [f for f in listdir(getpath) if f.endswith('.m4a')]

for i in tracks:
	input = getpath+"\\"+i
	output = getpath+"\\"+i[:-3]
	output = output+"mp3"
	subprocess.run(["ffmpeg", "-i", input, output])
