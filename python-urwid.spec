#
# Conditional build:
%bcond_without	doc	# docs build
%bcond_with	tests	# test target (fails on builders due to lack of pts)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	urwid
Summary:	Urwid - a console user interface library for Python 2
Summary(hu.UTF-8):	Urwid egy konzolos felhasználói felület könyvtár Pythonhoz 2
Summary(pl.UTF-8):	Urwid - biblioteka konsolowego interfejsu użytkownika dla Pythona 2
Name:		python-%{module}
Version:	2.1.2
Release:	3
License:	LGPL v2.1+
Group:		Development/Languages/Python
#Source0Download: http://urwid.org/
Source0:	https://pypi.python.org/packages/source/u/urwid/%{module}-%{version}.tar.gz
# Source0-md5:	f7f4e6bed9ba38965dbd619520f39287
Patch0:		0002-Use-non-deprecated-template.patch
URL:		http://urwid.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.5
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg-3 >= 2.0.0
%endif
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Urwid is a console user interface library for Python.

%description -l hu.UTF-8
Urwid egy konzolos felhasználói felület könyvtár Pythonhoz.

%description -l pl.UTF-8
Urwid to biblioteka konsolowego interfejsu użytkownika dla Pythona.

%package -n python3-%{module}
Summary:	Urwid - a console user interface library for Python 3
Summary(hu.UTF-8):	Urwid egy konzolos felhasználói felület könyvtár Pythonhoz 3
Summary(pl.UTF-8):	Urwid - biblioteka konsolowego interfejsu użytkownika dla Pythona 3
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
Urwid is a console user interface library for Python.

%description -n python3-%{module} -l hu.UTF-8
Urwid egy konzolos felhasználói felület könyvtár Pythonhoz.

%description -n python3-%{module} -l pl.UTF-8
Urwid to biblioteka konsolowego interfejsu użytkownika dla Pythona.

%package apidocs
Summary:	API documentation for urwid module
Summary(pl.UTF-8):	Dokumentacja API modułu urwid
Group:		Documentation

%description apidocs
API documentation for urwid module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu urwid.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
sphinx-build-3 -b html . _html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

# tests
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/urwid/tests
%endif

%if %{with python3}
%py3_install

# tests
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/urwid/tests
%if %{with tests}
# unversioned copy installed if tests are run
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/urwid.egg-info
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst docs/changelog.rst
%dir %{py_sitedir}/urwid
%attr(755,root,root) %{py_sitedir}/urwid/str_util.so
%{py_sitedir}/urwid/*.py[co]
%{py_sitedir}/urwid-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst docs/changelog.rst
%dir %{py3_sitedir}/urwid
%attr(755,root,root) %{py3_sitedir}/urwid/str_util.cpython-*.so
%{py3_sitedir}/urwid/*.py
%{py3_sitedir}/urwid/__pycache__
%{py3_sitedir}/urwid-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_html/{_images,_static,examples,manual,reference,tutorial,*.html,*.js}
%endif
