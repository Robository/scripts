DIR = '/home/rob/.dosbox/'
CONF = 'dosbox-0.74-3.conf'

from tkinter import Tk
from tkinter import Listbox
from tkinter import Frame
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Text
from tkinter import LEFT
from tkinter import TOP
from tkinter import END
from tkinter import SINGLE

from os import listdir
from os import scandir
from os import system
from os import remove as removeFile
from os import walk
from os.path import isfile
from os.path import join

from shutil import copyfile as copy
from shutil import rmtree as removeDir

from time import sleep

exebat = []

def createConf(name):
	newConf = open(DIR+name+'.conf', 'w')
	newConf.write(r'''# Generated dosbox config by dosboxconfiger script
# github.com/robository GPL3.0
[sdl]
fullscreen=false
fulldouble=false
fullresolution=original
windowresolution=original
output=surface
autolock=true
sensitivity=100
waitonerror=true
priority=higher,normal
mapperfile=mapper-0.74-3.map
usescancodes=true
[dosbox]
language=
machine=svga_s3
captures=capture
memsize=16
[render]
frameskip=0
aspect=false
scaler=normal2x
[cpu]
#auto, 386, 386_slow, 486_slow, pentium_slow, 386_prefetch
core=auto
cputype=486_slow
cycles=auto
cycleup=10
cycledown=20
[mixer]
nosound=false
rate=44100
blocksize=1024
prebuffer=25
[midi]
mpu401=intelligent
mididevice=default
midiconfig=
[sblaster]
sbtype=sb16
sbbase=220
irq=7
dma=1
hdma=5
sbmixer=true
oplmode=auto
oplemu=default
oplrate=44100
[gus]
gus=false
gusrate=44100
gusbase=240
gusirq=5
gusdma=3
ultradir=C:\ULTRASND
[speaker]
pcspeaker=true
pcrate=44100
tandy=auto
tandyrate=44100
disney=true
[joystick]
joysticktype=auto
timed=true
autofire=false
swap34=false
buttonwrap=false
[serial]
serial1=dummy
serial2=dummy
serial3=disabled
serial4=disabled
[dos]
xms=true
ems=true
umb=true
keyboardlayout=de
[ipx]
ipx=false
[autoexec]














	''')
	newConf.close()
	
def getFiles():
	global fetchFiles
	fetchFiles = [ff for ff in listdir(DIR)\
		if not ff.endswith('.conf') and\
			not ff.endswith('.jpg')]
def init():
	listbox.focus()
	listbox.delete(0, END)
	getFiles()
	fetchFiles.sort()
	for i in fetchFiles:
		listbox.insert(0, i)
		if len(listbox.curselection()) == 0:
			listbox.select_set(0)
			listbox.event_generate("<<ListboxSelect>>")
		if isfile(DIR+CONF) == True:
			pass
		else:
			genConf = open(DIR+CONF, 'w')
			genConf.write('')
			genConf.close()			
		if isfile(DIR+i+'.conf') == True:
			pass
		else:
			createConf(i)
			writeLines = open(DIR+i+'.conf').read().splitlines()
			writeLines[81] = 'mount c "'+DIR+i+'"'
			writeLines[92] = 'c:'	
			open(DIR+i+'.conf', 'w').write('\n'.join(writeLines))
					
def select(event):
	global gameName
	selectItem = event.widget
	try:
		getName = int(selectItem.curselection()[0])
		gameName = selectItem.get(getName)
	except IndexError:
		return
		
	readLines = open(DIR+gameName+'.conf').read().splitlines()
	entry.delete(0, END)
	entry.insert(0, readLines[81])	
	entry1.delete(0, END)
	entry1.insert(0, readLines[82])
	entry2.delete(0, END)
	entry2.insert(0, readLines[83])	
	entry3.delete(0, END)
	entry3.insert(0, readLines[84])
	entry4.delete(0, END)
	entry4.insert(0, readLines[85])
	entry5.delete(0, END)
	entry5.insert(0, readLines[86])
	entry6.delete(0, END)
	entry6.insert(0, readLines[87])
	entry7.delete(0, END)
	entry7.insert(0, readLines[88])
	entry8.delete(0, END)
	entry8.insert(0, readLines[89])	
	entry9.delete(0, END)
	entry9.insert(0, readLines[90])
	entry10.delete(0, END)
	entry10.insert(0, readLines[91])
	entry11.delete(0, END)
	entry11.insert(0, readLines[92])	
	entry12.delete(0, END)
	entry12.insert(0, readLines[93])
	entry13.delete(0, END)
	entry13.insert(0, readLines[94])
	
	textbox.delete(1.0,END)
	exebat.clear()
	for root, subdirs, files in walk(DIR+gameName+'/'):
		for exe in files:
			if exe.lower().endswith('.exe') or\
				exe.lower().endswith('.bat'):
				exebat.append(exe)	
	exebat.sort()
	for i in exebat:
		textbox.insert(END,i+'\n')
			
	for root, subdirs, files in walk(DIR+gameName+'/'):
		for cd in subdirs:
			if cd == 'cd' or cd == 'CD':
				getCD = [c for c in listdir(DIR+gameName+'/'+cd)\
					if not c.endswith('.cue') and\
					not c.endswith('.ccd') and not c.endswith('.sub')]
				
				str2int = [getCD.index(i) for i in getCD]
				int2str = [str(i) for i in str2int]
				for i in int2str:
					if '0' in i:
						entry1.delete(0, END)
						entry1.insert(0,'imgmount d "'\
						+DIR+gameName+'/'+cd+'/'+getCD[0]+'" '+'-t iso')
					if '1' in i:
						entry2.delete(0, END)
						entry2.insert(0,'imgmount e "'\
						+DIR+gameName+'/'+cd+'/'+getCD[1]+'" '+'-t iso')							
					if '2' in i:
						entry3.delete(0, END)
						entry3.insert(0,'imgmount f "'\
						+DIR+gameName+'/'+cd+'/'+getCD[2]+'" '+'-t iso')
					if '3' in i:
						entry4.delete(0, END)
						entry4.insert(0,'imgmount g "'\
						+DIR+gameName+'/'+cd+'/'+getCD[3]+'" '+'-t iso')														
					if '4' in i:
						entry5.delete(0, END)
						entry5.insert(0,'imgmount h "'\
						+DIR+gameName+'/'+cd+'/'+getCD[4]+'" '+'-t iso')
					if '5' in i:
						entry6.delete(0, END)
						entry6.insert(0,'imgmount i "'\
						+DIR+gameName+'/'+cd+'/'+getCD[5]+'" '+'-t iso')
					if '6' in i:
						entry7.delete(0, END)
						entry7.insert(0,'imgmount j "'\
						+DIR+gameName+'/'+cd+'/'+getCD[6]+'" '+'-t iso')							
					if '7' in i:
						entry8.delete(0, END)
						entry8.insert(0,'imgmount k "'\
						+DIR+gameName+'/'+cd+'/'+getCD[7]+'" '+'-t iso')
					if '8' in i:
						entry9.delete(0, END)
						entry9.insert(0,'imgmount l "'\
						+DIR+gameName+'/'+cd+'/'+getCD[8]+'" '+'-t iso')														
					if '9' in i:
						entry10.delete(0, END)
						entry10.insert(0,'imgmount m "'\
						+DIR+gameName+'/'+cd+'/'+getCD[9]+'" '+'-t iso')					

	for root, subdirs, files in walk(DIR+gameName+'/'):
		for win in subdirs:
			if win == 'WINDOWS' or win == 'windows':
				entry12.delete(0, END)
				entry13.delete(0, END)
				entry12.insert(0,'cd '+win)
				entry13.insert(0,'win')	
						
def writeConf():
	writeLines = open(DIR+gameName+'.conf').read().splitlines()
	writeLines[81] = entry.get()
	writeLines[82] = entry1.get()
	writeLines[83] = entry2.get()
	writeLines[84] = entry3.get()
	writeLines[85] = entry4.get()
	writeLines[86] = entry5.get()
	writeLines[87] = entry6.get()
	writeLines[88] = entry7.get()
	writeLines[89] = entry8.get()
	writeLines[90] = entry9.get()
	writeLines[91] = entry10.get()
	writeLines[92] = entry11.get()
	writeLines[93] = entry12.get()						
	writeLines[94] = entry13.get()
	open(DIR+gameName+'.conf', 'w').write('\n'.join(writeLines))
	
def run():
	writeConf()
	removeFile(DIR+CONF)
	copy(DIR+gameName+'.conf', DIR+CONF)	
	system('dosbox')
	
def run2(event):
	writeConf()
	removeFile(DIR+CONF)
	copy(DIR+gameName+'.conf', DIR+CONF)
	system('dosbox')

def delete():
	removeFile(DIR+gameName+'.conf')
	removeDir(DIR+gameName,ignore_errors=True)
	init()

root = Tk()
root.title('Dosbox Configer')
root.resizable(0,0)
root.geometry('600x800+400+100')

listbox = Listbox(root,height=50,width=30,selectmode=SINGLE)
listbox.pack(side=LEFT)
listbox.bind('<<ListboxSelect>>', select)
listbox.bind('<Double-1>', run2)

buttonFrame = Frame(root)
buttonFrame.pack(side=TOP)
button = Button(buttonFrame,text='Refresh Games',command=init)
button.pack(side=LEFT)
button2 = Button(buttonFrame,text='Write Conf',command=writeConf)
button2.pack(side=LEFT)
button3 = Button(buttonFrame,text='Delete Game', command=delete)
button3.pack(side=LEFT)

button4 = Button(root,text='Start game',width=39,command=run)
button4.pack(side=TOP)

entryFrame = Frame(root)
entryFrame.pack(side=TOP)
labelEmpty = Label(entryFrame,text='')
labelEmpty.pack()
label = Label(entryFrame,text='Game Directory:')
label.pack()
entry = Entry(entryFrame,width=42)
entry.pack()
textbox = Text(entryFrame,width=48,height=5)
textbox.pack()
label1 = Label(entryFrame,text='Discs:')
label1.pack()
entry1 = Entry(entryFrame,width=42)
entry1.pack()
entry2 = Entry(entryFrame,width=42)
entry2.pack()
entry3 = Entry(entryFrame,width=42)
entry3.pack()
entry4 = Entry(entryFrame,width=42)
entry4.pack()
entry5 = Entry(entryFrame,width=42)
entry5.pack()
entry6 = Entry(entryFrame,width=42)
entry6.pack()
entry7 = Entry(entryFrame,width=42)
entry7.pack()
entry8 = Entry(entryFrame,width=42)
entry8.pack()
entry9 = Entry(entryFrame,width=42)
entry9.pack()
entry10 = Entry(entryFrame,width=42)
entry10.pack()
label2 = Label(entryFrame,text='Miscellaneous:')
label2.pack()
entry11 = Entry(entryFrame,width=42)
entry11.pack()
entry12 = Entry(entryFrame,width=42)
entry12.pack()
entry13 = Entry(entryFrame,width=42)
entry13.pack()

init()
root.mainloop()






