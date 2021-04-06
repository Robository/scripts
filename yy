#!/bin/python
from sys import argv as GET
from os import system as OS
getURL = GET[1]
OS(f'youtube-dl -f 251 "{getURL}"')