# TODO:
# - docdir fix (both docdir/midori and docdir/midori-version exist too)
%define mainver	0.3
%define minorver 3
Summary:	Web browser based on GTK+ WebCore
Summary(hu.UTF-8):	GTK+ WebCore alapú web-böngésző
Summary(pl.UTF-8):	Przeglądarka WWW oparta na GTK+ WebCore
Name:		midori
Version:	%{mainver}.%{minorver}
Release:	1
License:	LGPL v2
Group:		X11/Applications/Networking
Source0:	http://archive.xfce.org/src/apps/midori/%{mainver}/%{name}-%{version}.tar.bz2
# Source0-md5:	e1262cc7cc0c1773c331ab794480f037
URL:		http://www.twotoasts.de/index.php?/pages/midori_summary.html
BuildRequires:	docutils
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	gtk-doc
BuildRequires:	gtk-webkit-devel >= 1.1.1
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel >= 2.30.0
BuildRequires:	libunique-devel >= 0.9
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pkgconfig
BuildRequires:	python-modules
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sqlite3-devel >= 3.0
BuildRequires:	vala
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

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--docdir=%{_docdir} \
	--enable-apidocs

./waf build

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

# install API documentation
install -d $RPM_BUILD_ROOT%{_gtkdocdir}/{katze,midori}
cp _build_/docs/api/katze/html/* $RPM_BUILD_ROOT%{_gtkdocdir}/katze
cp _build_/docs/api/midori/html/* $RPM_BUILD_ROOT%{_gtkdocdir}/midori

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
%doc AUTHORS ChangeLog HACKING README TODO TRANSLATE
%attr(755,root,root) %{_bindir}/midori
%dir %{_libdir}/midori
%attr(755,root,root) %{_libdir}/midori/*.so
%{_sysconfdir}/xdg/midori
%{_desktopdir}/midori.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/midori
%{_docdir}/midori

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/katze
%{_gtkdocdir}/midori
