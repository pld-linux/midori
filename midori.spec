Summary:	Web browser based on GTK+ WebCore
Summary(pl.UTF-8):	Przeglądarka WWW oparta na GTK+ WebCore
Name:		midori
Version:	0.0.16
Release:	1
License:	GPL v2+
Group:		X11/Applications/Networking
Source0:	http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.gz
# Source0-md5:	606497b1254d87df5267034d95abd516
URL:		http://software.twotoasts.de/?page=midori
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	gtk-webkit-devel >= 1.0.0-0.r29013.1
BuildRequires:	libsexy-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midori is a lightweight GTK+ 2 web browser based on GTK+ WebCore. It
features tabs, windows and session management, bookmarks stored with
XBEL, searchbox based on OpenSearch, and user scripts support.

%description -l pl.UTF-8
Midori to lekka przeglądarka dla GTK+ 2 oparta na GTK+ WebCore.
Obsługuje panele, okienka, zarządzanie sesjami, zakładki przechowywane
przy użyciu XBEL, okno wyszukiwania oparte na OpenSearch oraz skrypty
użytkownika.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
cat > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Midori
Comment=Lightweight web browser
Comment[pl]=Lekka przeglądarka WWW
Exec=%{name}
Icon=web_browser_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Network;WebBrowser;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
