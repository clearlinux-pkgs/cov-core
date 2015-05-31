#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cov-core
Version  : 1.15.0
Release  : 3
URL      : https://pypi.python.org/packages/source/c/cov-core/cov-core-1.15.0.tar.gz
Source0  : https://pypi.python.org/packages/source/c/cov-core/cov-core-1.15.0.tar.gz
Summary  : plugin core for use by pytest-cov, nose-cov and nose2-cov
Group    : Development/Tools
License  : MIT
Requires: cov-core-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
cov-core
========
This is a lib package for use by pytest-cov, nose-cov and nose2-cov.  Unless you're developing a
coverage plugin for a test framework, you probably want one of those.

%package python
Summary: python components for the cov-core package.
Group: Default

%description python
python components for the cov-core package.


%prep
%setup -q -n cov-core-1.15.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
