%define name rox-mime-editor
%define oname MIME-Editor
%define fname mime-editor
%define version 0.5
%define release 6
%define appdir %_prefix/lib/apps

Summary: MIME database editor
Name: %{name}
Version: 0.6
Release: 2
Source0: https://sourceforge.net/projects/rox/files/MIME-Editor/0.6/mime-editor-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/Other
URL: http://rox.sf.net/mime_editor.php3
Requires: rox-lib
Buildarch: noarch

%description
The Shared MIME Database stores information about file types. It holds
information such as "Files with names ending in .html have the MIME
type text/html" and "A text/html file should be described as an `HTML
Page'".

Normally, you shouldn't need to edit this database, but if you do you
can use MIME-Editor for the task.

%prep
%setup -q -n %fname-%version

%build

%install
mkdir -p %{buildroot}/%appdir
cp -r %oname %{buildroot}/%appdir
rm -f %{buildroot}%appdir/%oname/Messages/dist
rm -f %{buildroot}%appdir/%oname/Messages/*po
for gmo in %{buildroot}%appdir/%oname/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%{buildroot}!!)" >> %name.lang
done

%clean

%files -f %name.lang
%doc %appdir/%oname/Help
%dir %appdir/%oname/
%appdir/%oname/*.*
%appdir/%oname/AppRun
%appdir/%oname/.DirIcon
%dir %appdir/%oname/Messages



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5-5mdv2010.0
+ Revision: 433393
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5-4mdv2009.0
+ Revision: 242558
- rebuild
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Jul 31 2006 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2007.0
- Rebuild

* Fri Dec 16 2005 Götz Waschk <waschk@mandriva.org> 0.5-1mdk
- New release 0.5
- use mkrel

* Thu Jul 21 2005 Götz Waschk <waschk@mandriva.org> 0.4-1mdk
- update file list
- don't use %%_libdir
- add source URL
- new version

* Sun Mar 13 2005 Götz Waschk <waschk@linux-mandrake.com> 0.1.3-2mdk
- drop prefix

* Wed Feb 25 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.3-1mdk
- add new files
- new version

* Mon Nov 24 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.2-1mdk
- new version


