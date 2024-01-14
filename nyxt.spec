%global         debug_package %{nil}
%global         __strip       /bin/true

%define         _build_id_links none

Name:           nyxt
Version:        3.11.0
Release:        1%{?dist}
Summary:        Keyboard-oriented, infinitely extensible web browser

License:        BSD
URL:            https://nyxt.atlas.engineer/
Source0:        https://github.com/atlas-engineer/%{name}/releases/download/%{version}/%{name}-%{version}-source-with-submodules.tar.xz

BuildRequires:  gcc-c++ git make
BuildRequires:  sbcl >= 2.3.6
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  libfixposix-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       pkgconfig(openssl)
Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(webkit2gtk-4.0)
Requires:       libfixposix-devel
Requires:       xsel
Requires:       wl-clipboard

%description
Nyxt is a keyboard-oriented, infinitely extensible web browser designed for
power users. Conceptually inspired by Emacs and Vim, it has familiar
key-bindings (Emacs, vi, CUA), and is fully configurable in Lisp.

%prep
%setup -q -c -n %{name}-%{version}
echo $PWD

%build
make PREFIX=/usr all

%install
make PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT install

%files
/usr/bin/nyxt
/usr/share/applications/nyxt.desktop
/usr/share/metainfo/nyxt.metainfo.xml
/usr/share/icons/hicolor/scalable/apps/nyxt.svg
/usr/share/icons/hicolor/*/apps/nyxt.png
/usr/share/nyxt/*

%changelog
* Sun Jan 14 2024
- version updated to 3.11.0
* Wed Dec 13 2023 <kiky.tokamuro@yandex.ru>
- version updated to 3.10.0
* Sat Nov 18 2023 <kiky.tokamuro@yandex.ru>
- version updated to 3.9.2
* Tue Oct 24 2023 <kiky.tokamuro@yandex.ru>
- version updated to 3.9.1
* Tue Oct 10 2023 <kiky.tokamuro@yandex.ru>
- version updated to 3.9.0
* Mon Sep 25 2023 <kiky.tokamuro@yandex.ru>
- version updated to 3.8.0
* Mon Sep 11 2023 <kiky.tokamuro@yandex.ru>
- version updated to 3.7.0
* Sat Sep 9 2023 <kiky.tokamuro@yandex.ru>
- initial release
