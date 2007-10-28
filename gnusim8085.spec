Name: gnusim8085
Summary: Graphical Intel 8085 simulator, assembler and debugger
Version: 1.3.2
Release: %mkrel 1
License: GPLv2+
Group: Emulators
Source: http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL: http://gnusim8085.sourceforge.net
BuildRequires: gnomeui2-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

%description
GNUSim8085 is a graphical simulator plus assembler with debugger for
the Intel 8085 microprocessor.  It is written using GNOME libs.  It
can also run on several window managers.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%clean
rm -rf %{buildroot}

