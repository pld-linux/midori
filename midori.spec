Summary:	Web browser based on GTK+ WebCore
Name:		midori
Version:	0.0.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://software.twotoasts.de/media/midori/%{name}-%{version}.tar.gz
# Source0-md5:	95cb26bc180693ea9d1c606d4bc9aee6
URL:		http://software.twotoasts.de/?page=midori
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webcore-nrcit-libs-devel
BuildRequires:	libsexy-devel
Requires:	gtk-webcore-nrcore
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Midori is a lightweight GTK+ 2 web browser based on GTK+ WebCore. It
features tabs, windows and session management, bookmarks stored with
XBEL, searchbox based on OpenSearch, and user scripts support.

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
Exec=%{name}
Icon=web_browser_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;GTK;Network;WebBrowser;
EOF

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
