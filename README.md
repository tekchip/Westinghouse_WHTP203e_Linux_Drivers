# Westinghouse_WHTP203e_Linux_Drivers
Linux driver files and instructions for the Westinghouse WHTP203e thermal printer.

Westinghouse does release thermal printers with Linux support technically. Unfortunately they only provide a deb package which leaves everyone else out in the cold. https://westinghouse.com/pages/thermal-printer-whtp203e

Alien fails to conver the deb to rpm due to missing dependencies.

Note the files I've provided are for x64 platform only. The Westinghouse deb file does includes the files for many other platforms.

## Installation for Fedora Kinoite (RPM-OSTree)

For immutable Fedora distributions like Kinoite, Silverblue, or CoreOS:

1. **Build the RPM package:**
```bash
# Install build dependencies (if not already installed)
sudo rpm-ostree install rpm-build rpmdevtools

# Reboot to apply the layered packages
systemctl reboot

# After reboot, build the RPM
cd Westinghouse_WHTP203e_Linux_Drivers
./build-rpm.sh
```

2. **Install the RPM via rpm-ostree:**
```bash
# Find the built RPM (typically in ~/rpmbuild/RPMS/x86_64/)
rpm-ostree install ~/rpmbuild/RPMS/x86_64/westinghouse-whtp203e-driver-1.0-1.fc*.x86_64.rpm

# Reboot to apply changes
systemctl reboot
```

3. **Add the printer:**
After reboot, the printer should be automatically detected. If not, add it manually through GNOME Settings or system-config-printer and select the "Westinghouse WHTP203e" driver.

## Installation for Traditional Fedora (or similar)

To install this on Fedora 42 or similar traditional installations do the following:

Download the files in this repo.
```
git clone https://github.com/tekchip/Westinghouse_WHTP203e_Linux_Drivers.git
```
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
