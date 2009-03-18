Name: gnusim8085
Summary: Graphical Intel 8085 simulator, assembler and debugger
Version: 1.3.5
Release: %mkrel 1
License: GPLv2+
Group: Development/Other
Source: http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Patch0: gnusim8085-1.3.5-fix-str-fmt.patch
URL: http://gnusim8085.sourceforge.net
BuildRequires: gtk2-devel >= 2.12.0
BuildRequires: libgtksourceview-2.0-devel >= 2.2.0
BuildRequires: desktop-file-utils
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-build

%description
GNUSim8085 is a graphical simulator plus assembler with debugger for
the Intel 8085 microprocessor.  It is written using GNOME libs.  It
can also run on several window managers.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications \
	--add-category='GTK;GNOME;Development;Debugger' \
	%buildroot%_datadir/applications/GNUSim8085.desktop

# doc files are holding by rpm itself
rm -fr %buildroot%_datadir/doc/*

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README TODO NEWS AUTHORS ABOUT-NLS
%doc doc/*.txt doc/examples/*
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/pixmaps/gnusim8085
%{_datadir}/applications/*.desktop

%clean
rm -rf %{buildroot}
