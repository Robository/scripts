VER = 'dosbox-0.74-3.conf'
DIR = '/home/rob/.dosbox/'

from tkinter import Tk
from tkinter import Button
from tkinter import Listbox
from tkinter import Text
from tkinter import Label
from tkinter import LabelFrame
from tkinter import Frame
from tkinter import Checkbutton
from tkinter import Radiobutton
from tkinter import OptionMenu
from tkinter import StringVar
from tkinter import IntVar
from tkinter import messagebox
from tkinter import END
from tkinter import Entry

from os import system
from os import listdir
from os import walk
from os import remove as remFile
from os.path import isfile

from shutil import copyfile
from shutil import rmtree as remDir

def isConf():
	start = 0
	global setCD
	for isConf in listdir(DIR):
		if VER == isConf:
			if isfile(DIR+VER[:-4]+'BAK') == True:
				listboxRight.focus()				
			else:
				copyfile(DIR+VER,DIR+VER[:-4]+'BAK')
				listboxRight.focus()
			start = 1
		elif isfile(DIR+VER) == False:
			messagebox.showerror('Dosbox config file missing!','Dosbox creates a\
			config file when started first time!')
			root.destroy()
			break
	if start == 1:
		refresh()
	
def getCDs(x):
	cdsText = ''
	for root, subdirs, files in walk(x+'/'):
		for cd in subdirs:
			if cd == 'cd' or cd == 'CD':
				for cds in listdir(x+'/'+cd):
					if cds.endswith('.img') or cds.endswith('.IMG')\
					or cds.endswith('.bin') or cds.endswith('.BIN')\
					or cds.endswith('.iso') or cds.endswith('.ISO'):
						cdsText += 'imgmount d "'+x+'/'+cds+'" -t iso\n'	
	
	cdsText += '\nc:'
	writeLines = open(x+'.conf').read().splitlines()
	writeLines[24] = '#0  '
	writeLines[98] = 'nosound=0       '
	writeLines[238] = 'keyboardlayout=de'	
	writeLines[248] = 'mount c "'+x+'/'
	writeLines[249] = cdsText
	open(x+'.conf','w').write('\n'.join(writeLines))	

def getGames():
	global games
	games = [g for g in listdir(DIR) if not g.endswith('.conf') and\
			not g.endswith('.BAK')]
	games.sort()
	
def refresh():
	getGames()
	
	for gameConfs in games:
		if isfile(DIR+gameConfs+'.conf') == True:
			pass
		else:
			copyfile(DIR+VER[:-4]+'BAK',DIR+gameConfs+'.conf')
			getCDs(DIR+gameConfs)
			
		read(gameConfs)			
	listGames()
	
def listExeBats():
	exeBatsText = ''
	exeBatsCheck = ''
	for root, subdirs, files in walk(DIR+gameName+'/'):
		for exeBats in files:
			if exeBats.endswith('.exe') or exeBats.endswith('.EXE')\
			or exeBats.endswith('.bat') or exeBats.endswith('.BAT'):
				exeBatsCheck = exeBatsText 	
				if 'WINDOWS' in exeBatsCheck\
				or 'Apps' in exeBatsCheck\
				or 'SB16' in exeBatsCheck:
					pass
				else:
					exeBatsText += root+exeBats+'\n'	
	
	dirText.delete(1.0,END)
	dirText.insert(1.0,exeBatsText)
	
def getLines(x):
	global lines; lines = 0;
	global startLine; startLine = 248;
	global getMaxLines 

	countLines = open(DIR+x+'.conf').read().splitlines()
	for i in countLines:
		lines += 1
	getMaxLines = lines - startLine	
	
def read(x):
	getLines(x)
	global favorite
	global memSize
	global cpuType
	global cycles
	global sound
	global keyboard
	global textLine; textLine = ''
		
	readLines = open(DIR+x+'.conf').read().splitlines()
	favorite = readLines[24]; favorite=favorite[1:][:1]; favoriteVar.set(favorite)
	memSize = readLines[50]
	cpuType = readLines[85]; cpuType=cpuType[8:]; cpuTypeVar.set(cpuType)
	cycles = readLines[86]; cycles=cycles[7:]; cyclesVar.set(str(cycles))
	sound = readLines[98]; soundVar.set(int(sound[8:]))
	keyboard = readLines[238]; keyboard=keyboard[15:]; keyboardVar.set(keyboard)
	
	for i in range(getMaxLines):
		textLine += readLines[startLine+i]+'\n'

def write():
	getLines(gameName)
	textLine = autoexecText.get(1.0,END)
	writeLines = open(DIR+gameName+'.conf').read().splitlines()
	writeLines[24] = '#'+str(favoriteVar.get())
	writeLines[50] = memSize
	writeLines[85] = 'cpuType='+str(cpuTypeVar.get())
	writeLines[86] = 'cycles='+str(cyclesVar.get())
	writeLines[98] = 'nosound='+str(soundVar.get())
	writeLines[238] = 'keyboardlayout='+str(keyboardVar.get())
	
	for i in range(getMaxLines):
		writeLines[startLine+i]= ''
	writeLines[startLine] = textLine
	open(DIR+gameName+'.conf','w').write('\n'.join(writeLines))
	
def listGames():
	listboxRight.delete(0,END)
	listboxLeft.delete(0,END)
	for listGames in games:
		readLines = open(DIR+listGames+'.conf').read().splitlines()
		favorite = readLines[24]; favorite=favorite[1:][:1]	
		
		if not listGames.endswith('.conf') and\
				not listGames.endswith('.BAK'):
			if favorite == '1':
				listboxLeft.insert(0,listGames)
			if favorite == '0':
				listboxRight.insert(0,listGames)

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
		autoexecText.delete(1.0,END)
		autoexecText.insert(1.0,textLine)
		listExeBats()	

def reload():
	remFile(DIR+gameName+'.conf')
	refresh()
	
def delete():
	remFile(DIR+gameName+'.conf')
	remDir(DIR+gameName,ignore_errors=True)
	refresh()

def quit():
	root.destroy()

def run():
	write()
	system('dosbox -conf "'+DIR+gameName+'.conf"')	

def doFav():
	write()
	refresh()

root = Tk()
root.title('Dosconf')
root.resizable(0,0)

soundVar = IntVar()
favoriteVar = IntVar()
cpuTypeVar = StringVar()
cyclesVar = StringVar()
keyboardVar = StringVar()

buttonLabelFrame = LabelFrame(root,text='Menu')
buttonLabelFrame.grid(row=0,column=0,padx=2,pady=2)

favCheck = Checkbutton(buttonLabelFrame,text=' Favorite ',variable=favoriteVar,\
															command=doFav)
favCheck.grid(row=0,column=3,padx=2,pady=2)
refreshButton = Button(buttonLabelFrame,text='Refresh',command=refresh)
refreshButton.grid(row=0,column=5,padx=2,pady=2)

deleteButton = Button(buttonLabelFrame,text='Delete Game',command=delete)
deleteButton.grid(row=0,column=0,padx=2,pady=2)

soundCheck = Checkbutton(buttonLabelFrame,text=' No Sound ',variable=soundVar,\
															command=write)
soundCheck.grid(row=0,column=6,padx=2,pady=2)

quitButton = Button(buttonLabelFrame,text='Quit',command=quit)
quitButton.grid(row=0,column=1,padx=2,pady=2)

listboxFrame = Label(root)
listboxFrame.grid(row=1,column=0,padx=2,pady=2)
listboxLabelFrameLeft = LabelFrame(listboxFrame,text='Favorites')
listboxLabelFrameLeft.grid(row=0,column=0,padx=2,pady=2)
listboxLabelFrameRight = LabelFrame(listboxFrame,text='Games')
listboxLabelFrameRight.grid(row=0,column=1,padx=2,pady=2)

listboxLeft = Listbox(listboxLabelFrameLeft,width=32,height=20)
listboxLeft.grid(row=0,column=0,padx=4,pady=4)
listboxRight = Listbox(listboxLabelFrameRight,width=32,height=20)
listboxRight.grid(row=0,column=0,padx=4,pady=4)

doubleClickFlag = False
listboxRight.bind('<Double-Button-1>',doubleClick)
listboxRight.bind('<Button-1>',click)
listboxLeft.bind('<Double-Button-1>',doubleClick)
listboxLeft.bind('<Button-1>',click)

autoexecLabelFrame = LabelFrame(root,text='Autoexec')
autoexecLabelFrame.grid(row=4,column=0,padx=2,pady=2)

autoexecText = Text(autoexecLabelFrame,width=76,height=12)
autoexecText.grid(row=0,column=0,padx=4,pady=4)

optionLabelFrame = LabelFrame(root,text='Config settings')
optionLabelFrame.grid(row=3,column=0,padx=2,pady=2)

keyboardMenu = OptionMenu(optionLabelFrame,keyboardVar,\
	'auto','de','us','ru')
keyboardMenu.grid(row=0,column=5,padx=2,pady=2)
													
writeButton = Button(optionLabelFrame,text='Write',command=write)
writeButton.grid(row=0,column=2,padx=2,pady=2)
reloadButton = Button(optionLabelFrame,text='Reload',command=reload)
reloadButton.grid(row=0,column=3,padx=2,pady=2)
															
cpuMenu = OptionMenu(optionLabelFrame,cpuTypeVar,\
	'auto','386','386_slow','486_slow','pentium_slow','pentium_386')
cpuMenu.grid(row=0,column=4,padx=2,pady=2)

cyclesLabel = Label(optionLabelFrame,text='Cycles: ')
cyclesLabel.grid(row=0,column=0,padx=2,pady=2)
cyclesEntry = Entry(optionLabelFrame,width=10,textvariable=cyclesVar)
cyclesEntry.grid(row=0,column=1,padx=4,pady=2)

dirLabelFrame = LabelFrame(root,text='Directory')
dirLabelFrame.grid(row=5,column=0,padx=2,pady=2)

dirText = Text(dirLabelFrame,width=76,height=6)
dirText.grid(row=0,column=0,padx=4,pady=4)

isConf()
root.mainloop()

