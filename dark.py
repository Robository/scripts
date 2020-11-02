from os import system as SYS
from time import sleep as SLP

def sleep():
	SLP(0.33)	

WMTHEME    = ' Default '
THEMENAME  = ' Adwaita-dark '
ICONNAME   = ' OieIcons '
CURSORNAME = ' Chicago95 Standard Cursors '
BACKGROUND = '/home/rob/Images/Wallpaper/dw.jpg'
MENUNAME = ' Arch '
MENUICON = '/home/rob/.local/share/icons/OieIcons/24x24/places/user-desktop.svg'

SYS(f'xfconf-query -c xsettings -p /Net/ThemeName -s {THEMENAME}')
sleep()
SYS(f'xfconf-query -c xsettings -p /Net/IconThemeName -s {ICONNAME}')
sleep()
SYS(f'xfconf-query -c xsettings -p /Gtk/CursorThemeName -s {CURSORNAME}')
sleep()
SYS(f'xfconf-query -c xfwm4 -p /general/theme -s {WMTHEME}')
sleep()
SYS(f'xfconf-query -c xfce4-desktop -p \
	  /backdrop/screen0/monitorVirtual-1/workspace0/last-image \
	  -s {BACKGROUND}')
sleep()
SYS(f'xfconf-query -c xfce4-panel -p \
	  /plugins/plugin-1/button-title -s {MENUNAME}')
sleep()
SYS(f'xfconf-query -c xfce4-panel -p \
	  /plugins/plugin-1/button-icon -s {MENUICON}')


