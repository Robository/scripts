from os import system as SYS
from time import sleep as SLP

SYS('xfconf-query -c xsettings -p /Net/ThemeName -s Adwaita-dark')
SLP(0.33)
SYS('xfconf-query -c xsettings -p /Net/IconThemeName -s HighContrast')
SLP(0.33)
SYS('xfconf-query -c xsettings -p /Gtk/CursorThemeName -s "Adwaita"')
SLP(0.33)
SYS('xfconf-query -c xfwm4 -p /general/theme -s Aqua')
SLP(0.33)
SYS('xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s ~/2.jpg')
