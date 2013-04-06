# TODO
# - there's work in progress --enable-webkit2 option enabling WebKit2/ GTK+3
%bcond_with	gtk3
Summary:	Web browser based on GTK+ WebCore
Summary(hu.UTF-8):	GTK+ WebCore alapú web-böngésző
Summary(pl.UTF-8):	Przeglądarka WWW oparta na GTK+ WebCore
Name:		midori
Version:	0.5.0
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Networking
Source0:	http://archive.xfce.org/src/apps/midori/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	ad11685633e23f8173e2cd947d945cce
Patch0:		homepage.patch
URL:		http://twotoasts.de/index.php/midori/
BuildRequires:	gcr-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.22.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.16.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	gtk-doc
%{!?with_gtk3:BuildRequires:	gtk-webkit-devel >= 1.5.1}
%{?with_gtk3:BuildRequires:	gtk-webkit3-devel}
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel >= 2.30.0
%{!?with_gtk3:BuildRequires:	libunique-devel >= 0.9}
%{?with_gtk3:BuildRequires:	libunique3-devel}
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	libzeitgeist-devel >= 0.3.14
BuildRequires:	pkgconfig
#BuildRequires:	pkgconfig(Xss)
#BuildRequires:	pkgconfig(gcr-3-gtk2) >= 2.32
#BuildRequires:	pkgconfig(hildon-1)
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3.6.19
BuildRequires:	vala >= 0.14
BuildRequires:	xorg-lib-libX11-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Provides:	wwwbrowser
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midori is a lightweight GTK+ 2 web browser based on GTK+ WebCore. It
features tabs, windows and session management, bookmarks stored with
XBEL, searchbox based on OpenSearch, and user scripts support.

%description -l hu.UTF-8
Midori egy pehelysúlyú GTK+ 2 webböngésző GTK+ WebCore alapokon.
Lehetőségei között fülek (tabok), ablak és munkafolyamat kezelés,
könyvjelzők tárolása XBEL-lel, OpenSearch-ön alapuló keresődoboz és
felhasználói szkript támogatás van.

%description -l pl.UTF-8
Midori to lekka przeglądarka dla GTK+ 2 oparta na GTK+ WebCore.
Obsługuje panele, okienka, zarządzanie sesjami, zakładki przechowywane
przy użyciu XBEL, okno wyszukiwania oparte na OpenSearch oraz skrypty
użytkownika.

%package apidocs
Summary:	API documentation of midori
Summary(pl.UTF-8):	Dokumentacja API midori
Group:		Documentation
Requires:	gtk-doc-common
Provides:	midori-api-doc
Obsoletes:	midori-api-doc

%description apidocs
API documentation of midori.

%description apidocs -l pl.UTF-8
Dokumentacja API midori.

%prep
%setup -q
%patch0 -p1

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--docdir=%{_docdir} \
	--disable-granite \
	%{?with_gtk3:--enable-gtk3} \
	%{!?with_gtk3:--disable-gtk3} \
	--disable-tests \
	--enable-addons \
	--enable-apidocs \
	--enable-libnotify \
	--enable-unique \
	%{nil}

./waf build

%install
rm -rf $RPM_BUILD_ROOT
./waf install \
	--destdir=$RPM_BUILD_ROOT

# install API documentation
install -d $RPM_BUILD_ROOT%{_gtkdocdir}/{katze,midori}
cp _build/docs/api/katze/html/* $RPM_BUILD_ROOT%{_gtkdocdir}/katze
cp _build/docs/api/midori/html/* $RPM_BUILD_ROOT%{_gtkdocdir}/midori

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# no -devel package, unlink
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/%{name}-0.5
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/vala/vapi

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING README TODO TRANSLATE INSTALL
%attr(755,root,root) %{_bindir}/midori
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.so
/etc/xdg/midori
%{_desktopdir}/midori.desktop
%{_desktopdir}/midori-private.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/%{name}

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/katze
%{_gtkdocdir}/midori
