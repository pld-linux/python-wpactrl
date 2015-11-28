%define 	module	wpactrl
%define		snap	20090609
%define		rel		2
Summary:	A Python extension for wpa_supplicant/hostapd control interface access
Name:		python-%{module}
Version:	1.0.7
Release:	0.%{snap}.%{rel}
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://mirror.leaseweb.com/archlinux/other/python-wpactrl/python-wpactrl-%{snap}.tar.gz
# Source0-md5:	8d45739aa9bfa1110a4570bb5ceda768
URL:		http://projects.otaku42.de/wiki/PythonWpaCtrl
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
Suggests:	hostapd
Suggests:	wpa_supplicant
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python extension for wpa_supplicant/hostapd control interface
access.

wpa_supplicant/hostapd implements a control interface that can be used
by external programs to control the operations of the
wpa_supplicant/hostapd daemon and to get status information and event
notifications.

The WPACtrl class provided by python-wpactrl allows Python programs to
use helper functions to connect with the UNIX domain socket form of
control interface and communicate with a wpa_supplicant/hostapd
daemon.

%prep
%setup -q -n %{name}-%{snap}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README example.py
%attr(755,root,root) %{py_sitedir}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif
