from tkinter import *
from time import sleep
from os import listdir
from os import remove
from os import system
from shutil import copyfile as copy

dosboxDir = '/home/user/.dosbox/'
dosboxConf = 'dosbox-0.74-3.conf'
dosboxConfsDir = '/home/user/.dosbox/confs/'

files = [f for f in listdir(dosboxConfsDir)]
#files = [f for f in listdir(dosboxConfsDir) if f.endswith('.dos')]

files.sort()
files.insert(0, files.pop(files.index('1. Ms-dos.conf')))
files.insert(1, files.pop(files.index('2. Windows 3.11.conf')))

def exec(event):
    click = int(''.join(map(str, listbox.curselection())))
    remove(dosboxDir+dosboxConf)
    sleep(0.2)
    copy(dosboxConfsDir+files[click],dosboxDir+dosboxConf)
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
