
%define		_name	thinkeramik

Summary:	KDE style - thinkeramik
Summary(pl):	Styl do KDE - thinkeramik
Name:		kde-theme-%{_name}
Version:	3.1.4
Release:	1
License:	GPL
Group:		Themes
Source0:	http://prefsx1.hp.infoseek.co.jp/tk040415/%{_name}-%{version}.tar.gz
# Source0-md5:	ef6317fbd729fa2d5612c7f764677237
Patch0:		%{name}-global_cs.patch
URL:		http://www.kde-look.org/content/show.php?content=10919
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel >= 3.1.2
BuildRequires:	unsermake
Requires:	kdelibs >= 3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kde-style-thin_keramik

%description 
thinkeramik is a KDE style based on Keramik.

%description -l pl
thinkeramik to styl KDE oparty na Keramiku.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
thinkeramik is modified from keramik as follows:
- Flat Menubar and Toolbar.
- Scrollbar-slider color.(= Window-InactiveBackground)
- Thin push-buttons and scrollbar.
- Selected menu-Item effect.
- Active menubar-Item effect.
- Pixmaps of tabs.
- Active tab effect.
- Striped menu.

%description -n kde-style-%{_name} -l pl
thinkeramik to zmodyfikowany keramik z nastêpuj±cymi zmianami:
- P³askie paski menu i narzêdzi
- Inny kolor suwaka - nieaktywnego t³a
- Cienkie przyciski i suwak
- Efekt dla zaznaczonej i aktywnej pozycji w pasku menu
- Ikonki na zak³adkach
- Efekt aktywnej zak³adki
- Paskowane menu

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - thinkeramik
Summary(pl):	Schemat kolorów do stylu KDE - thinkeramik
Group:		Themes
Requires:	kdelibs

%description -n kde-colorscheme-%{_name}
Color scheme for KDE style - thinkeramik.

%description -n kde-colorscheme-%{_name} -l pl
Schemat kolorów do stylu KDE - thinkeramik.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - thinkeramik
Summary(pl):	Dekoracja kwin - thinkeramik
Group:		Themes
Requires:	kdebase-desktop

%description -n kde-decoration-%{_name}
Window decoration style for KDE - thinkeramik.

%description -n kde-decoration-%{_name} -l pl
Styl dekoracji okien dla KDE - thinkeramik.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
export UNSERMAKE=/usr/share/unsermake/unsermake
cp -f /usr/share/automake/config.sub admin
%{__make} -f Makefile.cvs
%configure
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_libdir}/kde3/kstyle_thinkeramik_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_thinkeramik_config.so
%{_datadir}/apps/kstyle/themes/*.themerc
##%{_desktopdir}/thinkeramik.desktop

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/thinkeramik*.kcsrc

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/kde3/kwin*.so
%{_libdir}/kde3/kwin*.la
%{_datadir}/apps/kwin/*.desktop
