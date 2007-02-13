Summary:	A tiling tabbed X11 window manager
Summary(pl.UTF-8):	Zarządca okien dla X11
Name:		ion
Version:	20040729
Release:	1
License:	LGPL
Group:		X11/Window Managers
Source0:	http://modeemi.fi/~tuomov/ion/dl/%{name}-2-%{version}.tar.gz
# Source0-md5:	d7d98baa41635c1989e423adf76eb2ac
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
URL:		http://iki.fi/tuomov/ion/
BuildRequires:	XFree86-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 1.4.3
BuildRequires:	lua50 >= 5.0.2-2
BuildRequires:	lua50-devel >= 5.0.2-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Ion is a keyboard-friendly X11 window manager. It is fast and takes up
little resources.

%description -l pl.UTF-8
Ion jest zarządcą okien, obsługiwanym prawie wyłącznie z klawiatury.
Jest szybki i zajmuje mało zasobów.

%prep
%setup -q -n %{name}-2-%{version}

%build
%configure \
	--disable-static \
	--with-lua-suffix=50 \
	--with-lua-includes=%{_includedir}/lua50
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir}}

%{__make} install \
	MODULEDIR=%{buildroot}%{_libdir}/ion \
	SHAREDIR=%{buildroot}%{_datadir}/ion \
	LCDIR=%{buildroot}%{_libdir}/ion/lc \
	ETCDIR=%{buildroot}%{_sysconfdir}/ion \
	BINDIR=%{buildroot}%{_bindir} \
	EXTRABINDIR=%{buildroot}%{_libdir}/ion \
	MANDIR=%{buildroot}%{_mandir} \
	DOCDIR=%{buildroot}%{_docdir}/%{name}-%{version}

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%dir %{_sysconfdir}/ion
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ion/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ion
%attr(755,root,root) %{_libdir}/ion/*.so
# used (lt_dlopen)
%{_libdir}/ion/*.la
%attr(755,root,root) %{_libdir}/ion/ion-completefile
%{_libdir}/ion/lc
%dir %{_datadir}/ion
%{_datadir}/ion/delib.lc
%{_datadir}/ion/*.lua
%attr(755,root,root) %{_datadir}/ion/ion-*
%{_datadir}/ion/welcome_message.txt
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/ion.desktop
%{_mandir}/man1/*
