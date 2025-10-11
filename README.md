# Westinghouse_WHTP203e_Linux_Drivers
Linux driver files and instructions for the Westinghouse WHTP203e thermal printer.

Westinghouse does release thermal printers with Linux support technically. Unfortunately they only provide a deb package which leaves everyone else out in the cold.

Alien fails to conver the deb to rpm due to missing dependencies.

Note the files I've provided are for x64 platform only. The Westinghouse deb file does includes the files for many other platforms.

To install this on Fedora 42 or similar do the following:

Copy all the rastertosnail...-westinghouse files to /usr/lib/cups/filter/ Most likely this folder will require sudo or root access.
```
sudo cp *-westinghouse /usr/lib/cups/filter/
```
You may run in to permissions issues. You should do the following to avoid these.
```
sudo chown root:root /usr/lib/cups/filter/*-westinghouse
```
```
sudo chmod 755 /usr/lib/cups/filter/*-westinghouse
```
Add the printer which should be detected and when prompted manually point the printer dialogue to the PPD file.

Happy printing!
