Summary:	Ion - an X11 window manager
Summary(pl):	Ion - zarz±dca okien dla X11
Name:		ion
Version:	20030416
Release:	5
License:	Artistic
Group:		X11/Window Managers
Source0:	http://modeemi.cs.tut.fi/~tuomov/dl/%{name}-devel-%{version}.tar.gz
# Source0-md5:	07da07e2ac4e20855d5621f1111bd09b
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-edit.patch
Patch2:		%{name}-OPT.patch
Patch3:		%{name}-va.patch
URL:		http://modeemi.fi/~tuomov/ion/
BuildRequires:	XFree86-devel
BuildRequires:	libltdl-devel
BuildRequires:	lua50-devel >= 5.0.2-2
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
	CC="%{__cc}" \
	LUA_INCLUDES="-I/usr/include/lua50" \
	LUA_LIBS="-llua50 -llualib50" \
	X11_LIBS="-L/usr/X11R6/%{_lib} -lX11 -lXext" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%dir %{_sysconfdir}/X11/ion-devel
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/X11/ion-devel/*
%attr(755,root,root) %{_bindir}/*
# %{_libdir}/ion-devel/*.so instead? chmod +x them?
%{_libdir}/ion-devel
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/ion.desktop
%{_mandir}/man1/*
