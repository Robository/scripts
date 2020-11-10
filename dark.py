from os import system as SYS
from time import sleep as SLP

def sleep():
	SLP(0.33)	

WMTHEME    = ' Default '
THEMENAME  = ' barahi '
ICONNAME   = ' MB-Lime-Suru-GLOW '
CURSORNAME = ' Adwaita'
BACKGROUND = '/usr/share/backgrounds/xfce/xfce-stripes.png'
MENUNAME = ' HACK '
MENUICON = '/home/rob/.local/share/icons/arch.png'

SYS(f'xfconf-query -c xsettings -p /Net/ThemeName -s {THEMENAME}')
sleep()
SYS(f'xfconf-query -c xsettings -p /Net/IconThemeName -s {ICONNAME}')
sleep()
SYS(f'xfconf-query -c xsettings -p /Gtk/CursorThemeName -s {CURSORNAME}')
sleep()
SYS(f'xfconf-query -c xfwm4 -p /general/theme -s {WMTHEME}')
sleep()
SYS(f'xfconf-query -c xfce4-desktop -p \
	  /backdrop/screen0/monitorDisplayPort-1/workspace0/last-image \
	  -s {BACKGROUND}')
sleep()
SYS(f'xfconf-query -c xfce4-panel -p \
	  /plugins/plugin-1/button-title -s {MENUNAME}')
sleep()
SYS(f'xfconf-query -c xfce4-panel -p \
	  /plugins/plugin-1/button-icon -s {MENUICON}')


