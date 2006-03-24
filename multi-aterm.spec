Summary:	multi-aterm - tabbed terminal emulator in an X Window System
Summary(pl):	multi-aterm - emulator terminala dla X Window System
Summary(pt_BR):	Um emulador de vt102 colorido
Name:		multi-aterm
Version:	0.2.1
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.nongnu.org/materm/%{name}-%{version}.tar.gz
# Source0-md5:	52f9c25a6fad7f638f7064ff6cc74c62
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.nongnu.org/materm/
BuildRequires:	autoconf
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	utempter-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
Requires:	terminfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
multi-aterm is a terminal emulator. It is based on aterm 0.4.2,
features most of functionalties of aterm (pseudo fast-transparency,
nextstep look scroll bar) and mostly and notebook functionality. Thus,
you can have several terminals in the same window. Each terminal can
be configured (name, background, ...) with a configuration file. Like
aterm, it aims to be light and fast and desktop independant, meaning
KDE or GNOME are not required. Several configurations files can be
used. Specific files override resources of standard files, and options
override resources found in files.

%description -l pl
multi-aterm to emulator terminala. Jest oparty na atermie 0.4.2, ma
wiêkszo¶æ funkcji aterma (szybk± pseudoprzezroczysto¶æ, pasek
przewijania w stylu nextstepa) oraz funkcjonalno¶æ pozwalaj±c± na
trzymanie wielu terminali w tym samym oknie. Ka¿dy terminal mo¿e byæ
konfigurowany (nazwa, t³o...) w pliku konfiguracyjnym. Podobnie jak
aterm, ten terminal ma byæ lekki, szybki, niezale¿ny od pulpitu, czyli
nie wymagaj±cy KDE ani GNOME. Mo¿na u¿ywaæ kilku plików
konfiguracyjnych. Bardziej konkretne pliki przykrywaj± zasoby ze
standardowych plików, a opcje przykrywaj± zasoby z plików.

%prep
%setup -q

%build
LDFLAGS="%{rpmldflags} -lutempter -L%{_libdir}"
export LDFLAGS
%configure \
	--enable-ttygid \
	--enable-wtmp \
	--enable-background-image \
	--with-term=rxvt \
	--with-png \
	--with-jpeg \
	--with-xpm=/usr \
	--enable-transparency \
	--enable-fading \
	--enable-menubar \
	--enable-graphics \
	--enable-xgetdefault \
	--enable-next-scroll \
	--enable-mousewheel
#	--enable-utmp \

%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
