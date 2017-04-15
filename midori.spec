%bcond_without	gtk3
Summary:	Web browser based on GTK+ WebCore
Summary(hu.UTF-8):	GTK+ WebCore alapú web-böngésző
Summary(pl.UTF-8):	Przeglądarka WWW oparta na GTK+ WebCore
Name:		midori
Version:	0.5.11
Release:	0.1
License:	LGPL v2+
Group:		X11/Applications/Networking
Source0:	http://midori-browser.org/downloads/%{name}_%{version}_all_.tar.bz2
# Source0-md5:	fcc03ef759fce4fe9f2446d9da4a065e
Patch0:		homepage.patch
Patch1:		gtk-doc-path.patch
Patch2:		soversion.patch
Patch3:		vala-0.35.patch
Patch4:		vala-0.36.patch
URL:		http://midori-browser.org/
BuildRequires:	cmake >= 2.6.0
BuildRequires:	gcr-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.22.0
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.16.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel}
BuildRequires:	gtk-doc
%{!?with_gtk3:BuildRequires:	gtk-webkit-devel >= 1.5.1}
%{?with_gtk3:BuildRequires:	gtk-webkit3-devel}
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel >= 2.30.0
BuildRequires:	libsoup-gnome-devel >= 2.30.0
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
BuildRequires:	vala-zeitgeist
BuildRequires:	xorg-lib-libX11-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	/sbin/ldconfig
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
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1

%build
install -d build
cd build
%cmake \
	%{?with_gtk3:-DUSE_GTK3=1} \
	-DUSE_APIDOCS=1 \
	.. \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{nap,no}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING README TODO TRANSLATE
%attr(755,root,root) %{_bindir}/midori
%dir %{_libdir}/%{name}
%attr(755,root,root) %ghost %{_libdir}/libmidori-core.so.?
%attr(755,root,root) %{_libdir}/libmidori-core.so.*.*
%attr(755,root,root) %{_libdir}/%{name}/*.so
/etc/xdg/midori
%{_desktopdir}/midori.desktop
%{_desktopdir}/midori-private.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/%{name}
%{_datadir}/appdata/midori.appdata.xml

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/katze
%{_gtkdocdir}/midori
