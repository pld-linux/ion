Summary:	Ion - an X11 window manager
Summary(pl):	Ion - mened¿er okien dla X11
Name:		ion
Version:	20020207
Release:	1
License:	Artistic
Group:		X11/Window Managers
Source0:	http://www.students.tut.fi/~tuomov/dl/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
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
install -d $RPM_BUILD_ROOT%{_datadir}/wm-properties

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/wm-properties/

gzip -9nf doc/* README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz *.gz
%dir %{_sysconfdir}/X11/ion
%config(noreplace) %verify(not size, mtime, md5) %{_sysconfdir}/X11/ion/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/wm-properties/ion.desktop
%{_mandir}/man1/*
