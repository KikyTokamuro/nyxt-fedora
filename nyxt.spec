%global         debug_package %{nil}
%global         __strip       /bin/true

Name:           nyxt
Version:        3.6.1
Release:        1%{?dist}
Summary:        Keyboard-oriented, infinitely extensible web browser

License:        BSD
URL:            https://nyxt.atlas.engineer/
Source0:        https://github.com/atlas-engineer/%{name}/releases/download/%{version}/%{name}-%{version}-source-with-submodules.tar.xz

BuildRequires:  gcc-c++ git make sbcl
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  libfixposix-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       pkgconfig(openssl)
Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(webkit2gtk-4.0)
Requires:       libfixposix-devel

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
/usr/share/icons/hicolor/*/apps/nyxt.png

%changelog
* Sat Sep 9 2023 <kiky.tokamuro@yandex.ru>
- initial release
