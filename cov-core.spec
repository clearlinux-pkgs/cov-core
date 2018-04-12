#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cov-core
Version  : 1.15.0
Release  : 21
URL      : http://pypi.debian.net/cov-core/cov-core-1.15.0.tar.gz
Source0  : http://pypi.debian.net/cov-core/cov-core-1.15.0.tar.gz
Summary  : plugin core for use by pytest-cov, nose-cov and nose2-cov
Group    : Development/Tools
License  : MIT
Requires: cov-core-python3
Requires: cov-core-python
Requires: coverage
BuildRequires : coverage
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
========
        
        This is a lib package for use by pytest-cov, nose-cov and nose2-cov.  Unless you're developing a
        coverage plugin for a test framework, you probably want one of those.

%package python
Summary: python components for the cov-core package.
Group: Default
Requires: cov-core-python3

%description python
python components for the cov-core package.


%package python3
Summary: python3 components for the cov-core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cov-core package.


%prep
%setup -q -n cov-core-1.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523565737
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
