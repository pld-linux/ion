Name:		ion
Version:	20010314
Release:	1
Summary:	Ion - an X11 window manager
Summary(pl):	Ion - mened¿er okien dla X11
Source:		%{name}-%{version}.tar.gz
URL:		http://www.students.tut.fi/~tuomov/ion/
Patch0:		%{name}-DESTDIR.patch
License:	Artistic
Group:		X11/Window Managers
BuildRequires:	XFree86-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ion is a keyboard-friendly X11 window manager. It is fast and takes up little resources.

%description -l pl
Ion jest mened¿erem okien, obs³ugiwanym prawie wy³±cznie z klawiatury. Jest szybki i zajmuje ma³o zasobów.

%prep
%setup -q
%patch0 -p1

%build

%{__make}

%install

rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf doc/* README ChangeLog

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/X11/ion
%config(noreplace) %verify(not size, mtime, md5) %{_sysconfdir}/X11/ion/*
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/man/man1/*
%doc doc/*.gz *.gz
