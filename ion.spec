Summary:	Ion - an X11 window manager
Summary(pl):	Ion - zarz±dca okien dla X11
Name:		ion
Version:	20030327
Release:	1
License:	Artistic
Group:		X11/Window Managers
Source0:	http://modeemi.cs.tut.fi/~tuomov/dl/%{name}-devel-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-no_devel.patch
Patch2:		%{name}-edit.patch
Patch3:		%{name}-OPT.patch
URL:		http://www.students.tut.fi/~tuomov/ion/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Ion is a keyboard-friendly X11 window manager. It is fast and takes up
little resources.

%description -l pl
Ion jest zarz±dc± okien, obs³ugiwanym prawie wy³±cznie z klawiatury.
Jest szybki i zajmuje ma³o zasobów.

%prep
%setup -q -n %{name}-devel-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} \
	HAS_SYSTEM_ASPRINTF=1 \
	OPTFLAGS="%{rpmcflags}" \
	CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_wmpropsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.txt README ChangeLog
%dir %{_sysconfdir}/X11/ion
%config(noreplace) %verify(not size, mtime, md5) %{_sysconfdir}/X11/ion/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ion-devel/*
%{_wmpropsdir}/ion.desktop
%{_mandir}/man1/*
