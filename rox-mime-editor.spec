%define name rox-mime-editor
%define oname MIME-Editor
%define fname mime-editor
%define version 0.5
%define release %mkrel 2
%define appdir %_prefix/lib/apps

Summary: MIME database editor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/rox/%fname-%version.tar.bz2
License: GPL
Group: Graphical desktop/Other
URL: http://rox.sf.net/mime_editor.php3
BuildRoot: %{_tmppath}/%{name}-buildroot
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
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%appdir
cp -r %oname %buildroot/%appdir
rm -f %buildroot%appdir/%oname/Messages/dist
rm -f %buildroot%appdir/%oname/Messages/*po
for gmo in %buildroot%appdir/%oname/Messages/*.gmo;do
echo "%lang($(basename $gmo|sed s/.gmo//)) $(echo $gmo|sed s!%buildroot!!)" >> %name.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc %appdir/%oname/Help
%dir %appdir/%oname/
%appdir/%oname/*.*
%appdir/%oname/AppRun
%appdir/%oname/.DirIcon
%dir %appdir/%oname/Messages

