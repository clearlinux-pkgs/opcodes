#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : opcodes
Version  : 0.3.14
Release  : 7
URL      : https://files.pythonhosted.org/packages/df/2d/4d98a725b5e73ba3d8588fd415cc64120182ebec78e0695ecae7408a2d74/opcodes-0.3.14.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/2d/4d98a725b5e73ba3d8588fd415cc64120182ebec78e0695ecae7408a2d74/opcodes-0.3.14.tar.gz
Summary  : Database of Processor Instructions/Opcodes
Group    : Development/Tools
License  : BSD-2-Clause
Requires: opcodes-license = %{version}-%{release}
Requires: opcodes-python = %{version}-%{release}
Requires: opcodes-python3 = %{version}-%{release}
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/github/license/Maratyszcza/Opcodes.svg
:alt: License
:target: https://github.com/Maratyszcza/Opcodes/blob/master/license.rst

%package license
Summary: license components for the opcodes package.
Group: Default

%description license
license components for the opcodes package.


%package python
Summary: python components for the opcodes package.
Group: Default
Requires: opcodes-python3 = %{version}-%{release}

%description python
python components for the opcodes package.


%package python3
Summary: python3 components for the opcodes package.
Group: Default
Requires: python3-core

%description python3
python3 components for the opcodes package.


%prep
%setup -q -n opcodes-0.3.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538435922
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/opcodes
cp license.rst %{buildroot}/usr/share/package-licenses/opcodes/license.rst
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/opcodes/license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
