Name:           westinghouse-whtp203e-driver
Version:        1.0
Release:        1%{?dist}
Summary:        CUPS driver for Westinghouse WHTP203e thermal label printer

License:        Proprietary
URL:            https://westinghouse.com/pages/thermal-printer-whtp203e
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
Requires:       cups

%description
Linux CUPS driver for the Westinghouse WHTP203e thermal label printer.
This package provides the necessary CUPS filters and PPD file to enable
printing to the Westinghouse WHTP203e printer on Fedora and other
RPM-based Linux distributions.

%prep
%setup -q

%build
# No build needed - binary distribution

%install
rm -rf %{buildroot}

# Create directories
install -d %{buildroot}%{_cups_serverbin}/filter
install -d %{buildroot}%{_datadir}/cups/model/westinghouse

# Install CUPS filters
install -m 0755 rastertosnailep2-westinghouse %{buildroot}%{_cups_serverbin}/filter/
install -m 0755 rastertosnailep-westinghouse %{buildroot}%{_cups_serverbin}/filter/
install -m 0755 rastertosnailppli-westinghouse %{buildroot}%{_cups_serverbin}/filter/
install -m 0755 rastertosnailtspl-westinghouse %{buildroot}%{_cups_serverbin}/filter/
install -m 0755 rastertosnailxpl-westinghouse %{buildroot}%{_cups_serverbin}/filter/

# Install PPD file
install -m 0644 Westinghouse-WHTP203e.ppd %{buildroot}%{_datadir}/cups/model/westinghouse/

%files
%{_cups_serverbin}/filter/rastertosnailep2-westinghouse
%{_cups_serverbin}/filter/rastertosnailep-westinghouse
%{_cups_serverbin}/filter/rastertosnailppli-westinghouse
%{_cups_serverbin}/filter/rastertosnailtspl-westinghouse
%{_cups_serverbin}/filter/rastertosnailxpl-westinghouse
%{_datadir}/cups/model/westinghouse/Westinghouse-WHTP203e.ppd

%post
# Restart CUPS to pick up new driver
if [ $1 -eq 1 ] ; then
    systemctl try-restart cups.service >/dev/null 2>&1 || :
fi

%changelog
* Sat Feb 15 2025 Tekchip <tekchip@localhost> - 1.0-1
- Initial RPM package for Westinghouse WHTP203e printer driver
