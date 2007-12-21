Name: gnusim8085
Summary: Graphical Intel 8085 simulator, assembler and debugger
Version: 1.3.2
Release: %mkrel 1
License: GPLv2+
Group: Development/Other
Source: http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL: http://gnusim8085.sourceforge.net
BuildRequires: gnomeui2-devel gtksourceview1-devel
BuildRequires: desktop-file-utils
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

desktop-file-install --vendor='' --delete-original \
	--dir %buildroot%_datadir/applications \
	--add-category='GTK;GNOME;Development;Debugger' \
	--remove-key='MultipleArgs' \
	--remove-key='Encoding' \
	%buildroot%_datadir/gnome/apps/Development/GNUSim8085.desktop

# doc files are holding by rpm itself
rm -fr %buildroot%_datadir/doc/*

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc README TODO NEWS AUTHORS ABOUT-NLS
%doc doc/*.txt doc/examples/*
%{_bindir}/*
%{_datadir}/pixmaps/gnusim8085
%{_datadir}/gtksourceview-1.0/language-specs/*.lang
%{_datadir}/applications/*.desktop

%clean
rm -rf %{buildroot}
