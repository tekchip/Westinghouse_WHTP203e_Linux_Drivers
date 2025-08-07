# Westinghouse_WHTP203e_Linux_Drivers
Linux driver files and instructions for the Westinghouse WHTP203e thermal printer.

Westinghouse does release thermal printers with Linux support technically. Unfortunately they only provide a deb package which leaves everyone else out in the cold.

Alien fails to conver the deb to rpm due to missing dependencies.

Note the files I've provided are for x64 platform only. The Westinghouse deb file does includes the files for many other platforms.

To install this on Fedora 42 or similar do the following:

Manually point your printer dialogue at the PPD file.

Copy all the rastertosnail...-westinghouse files to /usr/lib/cups/filter/

Happy printing!
