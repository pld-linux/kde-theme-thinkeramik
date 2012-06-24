
%define		_name	thinkeramik

Summary:	KDE style - thinkeramik
Summary(pl.UTF-8):	Styl do KDE - thinkeramik
Name:		kde-theme-%{_name}
Version:	3.2.1
Release:	3
License:	GPL
Group:		Themes
Source0:	http://prefsx1.hp.infoseek.co.jp/tk040429/%{_name}-%{version}.tar.gz
# Source0-md5:	a151cd6ccba9376fb884d716ff4c4512
URL:		http://www.kde-look.org/content/show.php?content=10919
Patch0:		%{_name}-paths.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel >= 3.1.2
BuildRequires:	unsermake
Requires:	kde-style-%{_name}
Requires:	kde-colorscheme-%{_name}
Requires:	kde-decoration-%{_name}
Obsoletes:	kde-style-thin_keramik
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
thinkeramik is a KDE style based on Keramik.

%description -l pl.UTF-8
thinkeramik to styl KDE oparty na Keramiku.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl.UTF-8):	Styl do KDE - %{_name}
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

%description -n kde-style-%{_name} -l pl.UTF-8
thinkeramik to zmodyfikowany keramik z następującymi zmianami:
- Płaskie paski menu i narzędzi
- Inny kolor suwaka - nieaktywnego tła
- Cienkie przyciski i suwak
- Efekt dla zaznaczonej i aktywnej pozycji w pasku menu
- Ikonki na zakładkach
- Efekt aktywnej zakładki
- Paskowane menu

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - thinkeramik
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - thinkeramik
Group:		Themes
Requires:	kdelibs

%description -n kde-colorscheme-%{_name}
Color schemes for KDE style - thinkeramik. One of them
has a subdued green look and the second is an interesting
yet a little eccentric green/orange/blue mix.


%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Schematy kolorów do stylu KDE - thinkeramik. Jeden z nich
ma stonowany, zielony wygląd; a drugi jest interesującym,
acz trochę ekstrawaganckim połączeniem kolorów: 
zielonego, pomarańczowego i niebieskiego.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - thinkeramik
Summary(pl.UTF-8):	Dekoracja kwin - thinkeramik
Group:		Themes
Requires:	kdebase-desktop

%description -n kde-decoration-%{_name}
A window decoration which goes with the thinkeramik KDE style.
It is similar to the keramik decoration, it differs by:
- having flattened buttons
- extended customizability (like the buttons' shape)

%description -n kde-decoration-%{_name} -l pl.UTF-8
Dekoracja okien, która pasuje do stylu KDE - thinkeramika.
Jest podobna do dekoracji keramika z wyjątkiem:
- spłaszczonych przycisków
- zwiększonej dostosowywalności (np. kształtu przycisków)

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
export UNSERMAKE=/usr/share/unsermake/unsermake
cp -f /usr/share/automake/config.sub admin
%{__make} -f Makefile.cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%files

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
