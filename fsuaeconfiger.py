CONF = '/home/rob/FS-UAE/Configurations/'
DIR = '/home/rob/FS-UAE/Floppies/'
KICKS = '/home/rob/FS-UAE/Kickstarts/'

from tkinter import Tk
from tkinter import Listbox
from tkinter import Frame
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import LEFT
from tkinter import TOP
from tkinter import END
from tkinter import W
from tkinter import N
from tkinter import BOTH
from tkinter import X
from tkinter import Y
from tkinter import SINGLE
from tkinter import Radiobutton
from tkinter import StringVar

from os import listdir
from os import system
from os import remove as removeFile
from os.path import isfile
from shutil import rmtree as removeDir

def createConf(name):
	newConf = open(CONF+name+'.fs-uae', 'w')
	newConf.write(r'''#Generated fs-uae config by fsuaeconfiger script
# github.com/robository GPL3.0
[fs-uae]
kickstart_file = /home/rob/FS-UAE/Kickstarts/A1200.rom
accelerator_memory = 1024
amiga_model = A1200
chip_memory = 2048
fast_memory = 4096
slow_memory = 512
hard_drive_0 = harddrive.zip
joystick_port_1 = Padix Co. Ltd. PSX/USB converter
scanlines = 1
governor_warning = 0
floppy_drive_0 =
floppy_drive_1 = /
floppy_drive_2 = /
floppy_drive_3 = /
floppy_image_0 =
floppy_image_1 =
floppy_image_2 =
floppy_image_3 =
floppy_image_4 =
floppy_image_5 =
floppy_image_6 =
floppy_image_7 =
floppy_image_8 =
floppy_image_9 =
floppy_image_10 =
floppy_image_11 =
ntsc_mode = 0
keep_aspect = 0
joystick_0_button_0 = action_joy_1_fire_button  
joystick_0_button_1 = action_joy_1_2nd_button           
joystick_0_button_2 = action_joy_1_up    
joystick_0_button_3 = action_joy_1_autofire_button
	''')
	newConf.close()

fetchKicks = [fk for fk in listdir(KICKS)]
fetchKicks.sort()

def getFiles():
	global fetchFiles
	fetchFiles = [ff for ff in listdir(DIR)]

def init():
	listbox.focus()
	listbox.delete(0, END)
	getFiles()
	fetchFiles.sort()
	for i in fetchFiles:
		listbox.insert(0, i)
		if isfile(CONF+i+'.fs-uae') == True:
			pass
		else:
			createConf(i)
	
	for i in fetchFiles:
		if len(listbox.curselection()) == 0:
			listbox.select_set(0)
			listbox.event_generate('<<ListboxSelect>>')			
	
def writeKick():
	writeLines = open(CONF+gameName+'.fs-uae').read().splitlines()
	writeLines[5] = 'amiga_model = '+radioVar.get()	
	writeLines[3] = 'kickstart_file = '+KICKS+radioVar.get()+'.rom'
	open(CONF+gameName+'.fs-uae', 'w').write('\n'.join(writeLines))

def select(event):
	global gameName
	global amigaModel
	selectItem = event.widget
	try:
		getName = int(selectItem.curselection()[0])
		gameName = selectItem.get(getName)
	except IndexError:
		return
		
	readLines = open(CONF+gameName+'.fs-uae').read().splitlines()
	amigaModel = readLines[5]
	radioVar.set(amigaModel[14:])
	floppy.delete(0, END)
	swap.delete(0, END)
	swap2.delete(0, END)	
	swap3.delete(0, END)	
	swap4.delete(0, END)	
	swap5.delete(0, END)
	swap6.delete(0, END)	
	swap7.delete(0, END)	
	swap8.delete(0, END)	
	swap9.delete(0, END)
	swap10.delete(0, END)
	swap11.delete(0, END)		
	swap12.delete(0, END)
	getGames()	

def getGames():
	fetchGames = [fg for fg in listdir(DIR+gameName)]
	fetchGames.sort()
	str2int = [fetchGames.index(i) for i in fetchGames]
	int2str = [str(i) for i in str2int]
	writeLines = open(CONF+gameName+'.fs-uae').read().splitlines()
	#int2str.sort()
	for i in int2str:
		if '0' in i:
			floppy.delete(0, END)
			floppy.insert(0, fetchGames[0])
			swap.delete(0, END)
			swap.insert(0, fetchGames[0])
			writeLines[13] = 'floppy_drive_0 = '+gameName+'/'+fetchGames[0]	
			writeLines[17] = 'floppy_image_0 = '+gameName+'/'+fetchGames[0]
		if '1' in i:
			swap2.delete(0, END)
			swap2.insert(0, fetchGames[1])
			writeLines[18] = 'floppy_image_1 = '+gameName+'/'+fetchGames[1]
		if '2' in i:
			swap3.delete(0, END)
			swap3.insert(0, fetchGames[2])
			writeLines[19] = 'floppy_image_2 = '+gameName+'/'+fetchGames[2]	
		if '3' in i:
			swap4.delete(0, END)
			swap4.insert(0, fetchGames[3])
			writeLines[20] = 'floppy_image_3 = '+gameName+'/'+fetchGames[3]	
		if '4' in i:
			swap5.delete(0, END)
			swap5.insert(0, fetchGames[4])
			writeLines[21] = 'floppy_image_4 = '+gameName+'/'+fetchGames[4]		
		if '5' in i:
			swap6.delete(0, END)
			swap6.insert(0, fetchGames[5])
			writeLines[22] = 'floppy_image_5 = '+gameName+'/'+fetchGames[5]		
		if '6' in i:
			swap7.delete(0, END)
			swap7.insert(0, fetchGames[6])
			writeLines[23] = 'floppy_image_6 = '+gameName+'/'+fetchGames[6]		
		if '7' in i:
			swap8.delete(0, END)
			swap8.insert(0, fetchGames[7])
			writeLines[24] = 'floppy_image_7 = '+gameName+'/'+fetchGames[7]		
		if '8' in i:
			swap9.delete(0, END)
			swap9.insert(0, fetchGames[8])
			writeLines[25] = 'floppy_image_8 = '+gameName+'/'+fetchGames[8]		
		if '9' in i:
			swap10.delete(0, END)
			swap10.insert(0, fetchGames[9])
			writeLines[26] = 'floppy_image_9 = '+gameName+'/'+fetchGames[9]		
		if '10' in i:
			swap11.delete(0, END)
			swap11.insert(0, fetchGames[10])
			writeLines[27] = 'floppy_image_10 = '+gameName+'/'+fetchGames[10]
		if '11' in i:
			swap12.delete(0, END)
			swap12.insert(0, fetchGames[11])
			writeLines[28] = 'floppy_image_11 = '+gameName+'/'+fetchGames[11]			
	open(CONF+gameName+'.fs-uae', 'w').write('\n'.join(writeLines))

def delete():
	removeFile(CONF+gameName+'.fs-uae')
	removeDir(DIR+gameName,ignore_errors=True)
	init()

def run():
	joinName = '"'+CONF+gameName+'"'+'.fs-uae'
	#system(f'fs-uae {joinName}') 
	system(f'fs-uae {joinName}')	

root = Tk()
root.title('FS-UAE Configer')
root.resizable(0,0)
root.geometry('600x800+400+100')

listbox = Listbox(root,height=50,width=30,selectmode=SINGLE)
listbox.pack(side=LEFT)
listbox.bind('<<ListboxSelect>>', select)

buttonFrame = Frame(root)
buttonFrame.pack(side=TOP)
button = Button(buttonFrame,text='Refresh Games',command=init)
button.pack(side=LEFT)
button2 = Button(buttonFrame,text='Delete Game',command=delete)
button2.pack(side=LEFT)	
labelEmpty2 = Label(root,text='')
labelEmpty2.pack()
labelRadio = Label(root,text='Set Kickstarter rom:')
labelRadio.pack(side=TOP)
radioFrame = Frame(root)
radioFrame.pack(side=TOP)

radioVar = StringVar()
for txt in fetchKicks:
	Radiobutton(radioFrame, text=txt[:-4],variable=radioVar,\
		value=txt[:-4],\
		command=writeKick).pack(side=LEFT)
	
button4 = Button(root,text='Start Game',width=39,command=run)
button4.pack(side=TOP)
	
entryFrame = Frame(root)
entryFrame.pack(side=TOP)
labelEmpty = Label(entryFrame,text='')
labelEmpty.pack()
label = Label(entryFrame,text='Floppy Drive:')
label.pack()
floppy = Entry(entryFrame,width=42)
floppy.pack()
#floppy2 = Entry(entryFrame,width=42)
#floppy2.pack()	
#floppy3 = Entry(entryFrame,width=42)
#floppy3.pack()	
#floppy4 = Entry(entryFrame,width=42)
#floppy4.pack()	
label2 = Label(entryFrame,text='Swap Floppies:')
label2.pack()	
swap = Entry(entryFrame,width=42)
swap.pack()	
swap2 = Entry(entryFrame,width=42)
swap2.pack()	
swap3 = Entry(entryFrame,width=42)
swap3.pack()
swap4 = Entry(entryFrame,width=42)
swap4.pack()
swap5 = Entry(entryFrame,width=42)
swap5.pack()
swap6 = Entry(entryFrame,width=42)
swap6.pack()
swap7 = Entry(entryFrame,width=42)
swap7.pack()
swap8 = Entry(entryFrame,width=42)
swap8.pack()
swap9 = Entry(entryFrame,width=42)
swap9.pack()
swap10 = Entry(entryFrame,width=42)
swap10.pack()
swap11 = Entry(entryFrame,width=42)
swap11.pack()
swap12 = Entry(entryFrame,width=42)
swap12.pack()

init()
root.mainloop()	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
