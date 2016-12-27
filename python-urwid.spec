%define 	module	urwid
Summary:	Urwid - a console user interface library for Python
Summary(hu.UTF-8):	Urwid egy konzolos felhasználói felület könyvtár Pythonhoz
Summary(pl.UTF-8):	Urwid - biblioteka konsolowego interfejsu użytkownika dla Pythona
Name:		python-%{module}
Version:	1.1.1
Release:	2
License:	LGPL v2.1+
Group:		Development/Languages/Python
Source0:	http://excess.org/urwid/urwid-%{version}.tar.gz
# Source0-md5:	eca2e0413cf7216b01c84b99e0f2576d
URL:		http://excess.org/urwid/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Urwid is a console user interface library for Python.

%description -l hu.UTF-8
Urwid egy konzolos felhasználói felület könyvtár Pythonhoz.

%description -l pl.UTF-8
Urwid to biblioteka konsolowego interfejsu użytkownika dla Pythona.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG 
%dir %{py_sitedir}/urwid
%attr(755,root,root) %{py_sitedir}/urwid/str_util.so
%{py_sitedir}/urwid/*.py[co]
%{py_sitedir}/urwid-%{version}-py*.egg-info
