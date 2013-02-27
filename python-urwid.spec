%define 	module	urwid
Summary:	Urwid is a console user interface library for Python
Summary(hu.UTF-8):	Urwid egy konzolos felhasználói felület könyvtár Pythonhoz
Name:		python-%{module}
Version:	1.1.1
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://excess.org/urwid/urwid-%{version}.tar.gz
# Source0-md5:	eca2e0413cf7216b01c84b99e0f2576d
URL:		http://excess.org/urwid/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Urwid is a console user interface library for Python.

%description -l hu.UTF-8
Urwid egy konzolos felhasználói felület könyvtár Pythonhoz.

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG 
%{py_sitedir}/%{module}
%{py_sitedir}/*.egg-info
