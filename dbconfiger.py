from tkinter import Tk
from tkinter import Listbox
from tkinter import END
from time import sleep
from os import listdir
from os import remove
from os import system
from shutil import copyfile as copy

dosboxDir = '/home/rob/.dosbox/'
dosboxConfsDir = '/home/rob/.dosbox/confs/'

files = [f for f in listdir(dosboxConfsDir)]
#files = [f for f in listdir(dosboxConfsDir) if f.endswith('.dos')]
dosboxConf = ''
findDosboxConf = [f for f in listdir(dosboxDir)]
for i in findDosboxConf:
	if 'dosbox-' in i:
		dosboxConf = i

files.sort()

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

for i in files:
    listbox.insert(END, i[:-5])

root.title('DB-Configer')
root.mainloop()
