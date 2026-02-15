#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PACKAGE_NAME="westinghouse-whtp203e-driver"
VERSION="1.0"

echo "Building RPM package for Westinghouse WHTP203e driver..."

# Check if required tools are installed
if ! command -v rpmbuild &> /dev/null; then
    echo "Error: rpmbuild not found. Please install rpm-build:"
    echo "  sudo dnf install rpm-build rpmdevtools"
    exit 1
fi

# Set up RPM build environment
echo "Setting up RPM build environment..."
rpmdev-setuptree

# Create source directory
SRCDIR="${HOME}/rpmbuild/SOURCES/${PACKAGE_NAME}-${VERSION}"
mkdir -p "${SRCDIR}"

# Copy files to source directory
echo "Copying source files..."
cp "${PROJECT_ROOT}/drivers/filters"/rastertosnail*-westinghouse "${SRCDIR}/"
cp "${PROJECT_ROOT}/drivers/ppd/Westinghouse-WHTP203e.ppd" "${SRCDIR}/"

# Create source tarball
echo "Creating source tarball..."
cd "${HOME}/rpmbuild/SOURCES"
tar czf "${PACKAGE_NAME}-${VERSION}.tar.gz" "${PACKAGE_NAME}-${VERSION}"
rm -rf "${SRCDIR}"

# Copy spec file
cp "${SCRIPT_DIR}/${PACKAGE_NAME}.spec" "${HOME}/rpmbuild/SPECS/"

# Build RPM
echo "Building RPM package..."
cd "${HOME}/rpmbuild/SPECS"
rpmbuild -bb "${PACKAGE_NAME}.spec"

echo ""
echo "Build complete!"
echo "RPM package location:"
find "${HOME}/rpmbuild/RPMS" -name "${PACKAGE_NAME}*.rpm" -type f
echo ""
echo "To install the RPM on Fedora Kinoite, use:"
echo "  rpm-ostree install path/to/${PACKAGE_NAME}-${VERSION}-1.fc*.x86_64.rpm"
echo "  systemctl reboot"
