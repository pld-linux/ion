Summary:	Ion - an X11 window manager
Summary(pl):	Ion - mened¿er okien dla X11
Name:		ion
Version:	20010314
Release:	1
License:	Artistic
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(pl):	X11/Zarz±dcy Okien
Source0:	http://www.students.tut.fi/~tuomov/dl/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.students.tut.fi/~tuomov/ion/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Ion is a keyboard-friendly X11 window manager. It is fast and takes up
little resources.

%description -l pl
Ion jest mened¿erem okien, obs³ugiwanym prawie wy³±cznie z klawiatury.
Jest szybki i zajmuje ma³o zasobów.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf doc/* README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz *.gz
%dir %{_sysconfdir}/X11/ion
%config(noreplace) %verify(not size, mtime, md5) %{_sysconfdir}/X11/ion/*
%attr(755,root,root) %{_prefix}/bin/*
%{_mandir}/man1/*
