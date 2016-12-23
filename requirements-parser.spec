#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requirements-parser
Version  : 0.1.0
Release  : 9
URL      : https://pypi.python.org/packages/source/r/requirements-parser/requirements-parser-0.1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/r/requirements-parser/requirements-parser-0.1.0.tar.gz
Summary  : Parses Pip requirement files
Group    : Development/Tools
License  : BSD-2-Clause
Requires: requirements-parser-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Requirements Parser
===================
.. image:: https://secure.travis-ci.org/davidfischer/requirements-parser.png?branch=master
:target: https://travis-ci.org/davidfischer/requirements-parser
.. image:: https://coveralls.io/repos/davidfischer/requirements-parser/badge.png
:target: https://coveralls.io/r/davidfischer/requirements-parser

%package python
Summary: python components for the requirements-parser package.
Group: Default

%description python
python components for the requirements-parser package.


%prep
%setup -q -n requirements-parser-0.1.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
