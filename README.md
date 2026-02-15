# Westinghouse_WHTP203e_Linux_Drivers
Linux driver files and instructions for the Westinghouse WHTP203e thermal printer.

Westinghouse does release thermal printers with Linux support technically. Unfortunately they only provide a deb package which leaves everyone else out in the cold. https://westinghouse.com/pages/thermal-printer-whtp203e

Alien fails to conver the deb to rpm due to missing dependencies.

Note the files I've provided are for x64 platform only. The Westinghouse deb file does includes the files for many other platforms.

## Installation for Fedora Kinoite (RPM-OSTree)

For immutable Fedora distributions like Kinoite, Silverblue, or CoreOS:

### Option A: Download Pre-built RPM (Recommended)

1. **Download the latest RPM from [Releases](https://github.com/tekchip/Westinghouse_WHTP203e_Linux_Drivers/releases)**

2. **Install via rpm-ostree:**
```bash
rpm-ostree install ~/Downloads/westinghouse-whtp203e-driver-*.rpm
systemctl reboot
```

3. **Add the printer:**
After reboot, the printer should be automatically detected. If not, add it manually through GNOME Settings or system-config-printer and select the "Westinghouse WHTP203e" driver.

### Option B: Build the RPM Package Locally

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

## Creating a New Release

To create a new release with an automatically built RPM:

**Method 1: Create a Git Tag (Automatic)**
```bash
git tag v1.0
git push origin v1.0
```

**Method 2: Manual Trigger via GitHub**
1. Go to the "Actions" tab on GitHub
2. Select "Build RPM and Create Release"
3. Click "Run workflow"
4. Enter the version number and choose whether to create a release

The GitHub Actions workflow will automatically build the RPM and attach it to the release.

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
