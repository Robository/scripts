from tkinter import Tk
from tkinter import Listbox
from tkinter import END
from tkinter import Button
from time import sleep
from os import listdir
from os import remove
from os import system
from shutil import copyfile as copy

dosboxDir = '/home/rob/.dosbox/'
dosboxConfsDir = '/home/rob/.dosbox/confs/'

def getFiles():
	global files
	files = [f for f in listdir(dosboxConfsDir)]
	files.sort()

def init():
	global dosboxConf
	getFiles()
	findDosboxConf = [f for f in listdir(dosboxDir)]
	for i in findDosboxConf:
		if 'dosbox-' in i:
			dosboxConf = i
	for i in files:
		listbox.insert(END, i[:-5])

def refresh():
	oldFiles = files
	getFiles()
	newFiles = [x for x in files if x not in oldFiles]	
	str2Int = [files.index(x) for x in newFiles]	
		
	for i in files:
		listbox.delete(0,END)
	for i in files:
		listbox.insert(END,i[:-5])	
	for i in str2Int:
		listbox.itemconfig(i, bg='#87c9ff')

def exec(event):
	click = int(''.join(map(str, listbox.curselection())))	
	remove(dosboxDir+dosboxConf)
	sleep(0.2)
	copy(dosboxConfsDir+files[click], dosboxDir+dosboxConf)
	sleep(0.2)
	system('dosbox')

root = Tk()

listbox = Listbox(root, height=40, width=35)
listbox.bind('<Double-1>', exec)
listbox.pack()

button = Button(root,text="Refresh",command=refresh)
button.pack()

init()
	
root.title('DB-Configer')
root.mainloop()
