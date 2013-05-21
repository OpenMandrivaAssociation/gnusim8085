Name: gnusim8085
Summary: Graphical Intel 8085 simulator, assembler and debugger
Version: 1.3.7
Release: 2
License: GPLv2+
Group: Development/Other
Source:  http://launchpad.net/gnusim8085/trunk/%version/+download/%name-%version.tar.gz
URL: http://launchpad.net/gnusim8085
BuildRequires: pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires: pkgconfig(gtksourceview-2.0) >= 2.2.0
BuildRequires: desktop-file-utils

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

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications \
	--add-category='GTK;GNOME;Development;Debugger' \
	%buildroot%_datadir/applications/GNUSim8085.desktop

%find_lang %name

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

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO NEWS AUTHORS ABOUT-NLS
%doc doc/*.txt doc/examples/*
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%{_iconsdir}/*/*/*/*

%clean
rm -rf %{buildroot}


%changelog
* Wed May 18 2011 Funda Wang <fwang@mandriva.org> 1.3.7-1mdv2011.0
+ Revision: 676054
- new version 1.3.7

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 1.3.6-1mdv2011.0
+ Revision: 565284
- New version 1.3.6

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.3.5-2mdv2010.1
+ Revision: 437797
- rebuild

* Wed Mar 18 2009 Funda Wang <fwang@mandriva.org> 1.3.5-1mdv2009.1
+ Revision: 357118
- New version 1.3.5

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-3mdv2009.0
+ Revision: 246506
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Oct 28 2007 Funda Wang <fwang@mandriva.org> 1.3.2-1mdv2008.1
+ Revision: 102847
- install correct dekstop file
- fix file list
- First package
- Created package structure for gnusim8085.

