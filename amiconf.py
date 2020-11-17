DIRFLOPS = '/home/rob/FS-UAE/Floppies/'
DIRCONFS = '/home/rob/FS-UAE/Configurations/'
DIRKICKS = '/home/rob/FS-UAE/Kickstarts/'

def create_conf(string):
	TEMPLATE = '''#Favorite = 0
[fs-uae]
kickstart_file = 
amiga_model  =
ntsc_mode = 0
scanlines = 1
keep_aspect = 0
governor_warning = 0

joystick_port_1 = Padix Co. Ltd. PSX/USB converter
joystick_0_button_0 = action_joy_1_fire_button  
joystick_0_button_1 = action_joy_1_2nd_button           
joystick_0_button_2 = action_joy_1_up    
joystick_0_button_3 = action_joy_1_autofire_button\n\n'''

	getFloppies = [gf[:-4] for gf in listdir(DIRFLOPS+string)]
	getFloppies.sort()
	
	getFirstFourFloppies = getFloppies
	getFirstFourFloppies.sort()
		
	for n,i in enumerate(getFirstFourFloppies):
		TEMPLATE += 'floppy_drive_'+str(n)+' = '+string+'/'+i+'.adf\n'
	for n,i in enumerate(getFloppies):
		TEMPLATE += 'floppy_image_'+str(n)+' = '+string+'/'+i+'.adf\n'	
	
	newConf = open(DIRCONFS+string+'.fs-uae','w')
	newConf.write(r''+TEMPLATE)
	newConf.close()
	
def get_kickstarts():
	global kickstarts
	kickstarts = [ks for ks in listdir(DIRKICKS)]

def get_games():
	global games
	games = [g for g in listdir(DIRFLOPS)]
	
def refresh():
	get_games()
	for gameConfs in games:
		if isfile(DIRCONFS+gameConfs+'.fs-uae') == True:
			pass
		else:
			create_conf(gameConfs)
	listbox_fill()
		
def write(game):
	writeLines = open(DIRCONFS+game+'.fs-uae').read().splitlines()
	writeLines[0] = '#Favorite = '+str(favVar.get())
	writeLines[2] = 'kickstart_file = '+str(amigaRomVar.get())
	writeLines[3] = 'amiga_model = '+amigaModelVar.get()
	writeLines[4] = 'ntsc_mode = '+str(ntscVar.get())
	writeLines[5] = 'scanlines = '+str(scanlinesVar.get())
	open(DIRCONFS+game+'.fs-uae','w').write('\n'.join(writeLines))

def read(game):
	readLines = open(DIRCONFS+game+'.fs-uae').read().splitlines()
	fav = readLines[0]; fav=int(fav[12:]); favVar.set(fav)
	amigaK = readLines[2]; amigaK=amigaK[17:]; amigaRomVar.set(amigaK)
	amigaR = readLines[3]; amigaR=amigaR[14:]; amigaModelVar.set(amigaR)
	ntsc = readLines[4]; ntsc=int(ntsc[12:]); ntscVar.set(ntsc)
	scan = readLines [5]; scan=int(scan[12:]); scanlinesVar.set(scan)
	
def listbox_fill():
	listboxRight.delete(0,END)
	listboxLeft.delete(0,END)	
	
	for sortGames in games:
		readLines = open(DIRCONFS+sortGames+'.fs-uae').read().splitlines()
		fav = readLines[0]; fav=int(fav[12:]); favVar.set(fav)

		if fav == 0:
			listboxRight.insert(0,sortGames)
		elif fav == 1:
			listboxLeft.insert(0,sortGames)	

def click(event):
	listboxRight.after(300, action, event)
	listboxLeft.after(300, action, event)
	
def doubleClick(event):
	global doubleClickFlag
	doubleClickFlag = True
		
def action(event):
	global doubleClickFlag
	global gameName
	
	selectItem = event.widget
	try:
		getName = int(selectItem.curselection()[0])
		gameName = selectItem.get(getName)
	except IndexError:
		return
	
	if doubleClickFlag:	
		run()
		doubleClickFlag = False
	else:
		read(gameName)		
		
def quit():
	root.destroy()

def do_write():
	write(gameName)
	listbox_fill()

def run():
	write(gameName)
	system('fs-uae "'+DIRCONFS+gameName+'.fs-uae"')

def delete():
	remFile(DIRCONFS+gameName+'.fs-uae')
	remDir(DIRFLOPS+gameName,ignore_errors=True)
	refresh()

from tkinter import Tk
from tkinter import Listbox
from tkinter import Button
from tkinter import OptionMenu
from tkinter import Checkbutton
from tkinter import StringVar
from tkinter import IntVar
from tkinter import END
from tkinter import LabelFrame
from tkinter import Label
from tkinter import Frame

from os import system
from os import listdir
from os import remove as remFile
from os.path import isfile

from shutil import rmtree as remDir

root = Tk()
root.title('Amiconf')
root.resizable(0,0)

get_kickstarts()

amigaModelVar = StringVar()
amigaRomVar = StringVar()
ntscVar = IntVar()
scanlinesVar = IntVar()
favVar = IntVar()

menuMainFrame = LabelFrame(root,text='Menu')
menuMainFrame.grid(row=0,column=0,padx=2,pady=2)
menuFrameTop = Frame(menuMainFrame)
menuFrameTop.grid(row=0,column=0,padx=0,pady=2)
menuFrameBottom = Frame(menuMainFrame)
menuFrameBottom.grid(row=1,column=0,padx=2,pady=2)

deleteButton = Button(menuFrameTop,text='Delete',command=delete)
deleteButton.grid(row=0,column=0,padx=2,pady=2)

ntscCheck = Checkbutton(menuFrameTop,text='NTSC',\
						variable=ntscVar,command=do_write)
ntscCheck.grid(row=0,column=1,padx=2,pady=2)

scanlinesCheck = Checkbutton(menuFrameTop,text='Scanlines',\
						variable=scanlinesVar,command=do_write)
scanlinesCheck.grid(row=0,column=2,padx=2,pady=2)

favCheck = Checkbutton(menuFrameTop,text='Favorites',\
						variable=favVar,command=do_write)
favCheck.grid(row=0,column=3,padx=2,pady=2)

refreshButton = Button(menuFrameTop,text='Refresh',command=refresh)
refreshButton.grid(row=0,column=4,padx=2,pady=2)

quitButton = Button(menuFrameTop,text='Quit',command=quit)
quitButton.grid(row=0,column=5,padx=2,pady=2)

amigaRomLabel = Label(menuFrameBottom,text='Rom:')
amigaRomLabel.grid(row=0,column=0,padx=2,pady=2)

amigaRomMenu = OptionMenu(menuFrameBottom,amigaRomVar,*kickstarts)
amigaRomMenu.config(width=30,anchor='w')
amigaRomMenu.grid(row=0,column=1,padx=2,pady=2)

amigaModelLabel = Label(menuFrameBottom,text='Amiga model:')
amigaModelLabel.grid(row=0,column=2,padx=2,pady=2)

amigaModelMenu = OptionMenu(menuFrameBottom,amigaModelVar,'A500',\
	'A500+','A600','A1000','A1200','A1200/020','A3000','A4000/040',\
	'CD32','CDTV')
amigaModelMenu.config(width=5,anchor='w')
amigaModelMenu.grid(row=0,column=3,padx=2,pady=2)

listboxMainFrame = Frame(root)
listboxMainFrame.grid(row=1,column=0,padx=2,pady=2)
listboxLeftFrame = LabelFrame(listboxMainFrame,text='Favorites')
listboxLeftFrame.grid(row=0,column=0,padx=2,pady=2)
listboxRightFrame = LabelFrame(listboxMainFrame,text='Games')
listboxRightFrame.grid(row=0,column=1,padx=2,pady=2)

listboxLeft = Listbox(listboxMainFrame,width=32)
listboxLeft.grid(row=0,column=0,padx=0,pady=2)
listboxRight = Listbox(listboxMainFrame,width=32)
listboxRight.grid(row=0,column=1,padx=0,pady=2)

doubleClickFlag = False
listboxRight.bind('<Double-Button-1>',doubleClick)
listboxRight.bind('<Button-1>',click)
listboxLeft.bind('<Double-Button-1>',doubleClick)
listboxLeft.bind('<Button-1>',click)

refresh()
root.mainloop()
