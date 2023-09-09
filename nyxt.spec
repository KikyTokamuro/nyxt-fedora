%global         debug_package %{nil}
%global         __strip       /bin/true

Name:           nyxt
Version:        3.6.1
Release:        1%{?dist}
Summary:        Keyboard-oriented, infinitely extensible web browser

# The additional --eval flag is needed to avoid an error with UTF-8
# characters in /etc/mime.types
%global lisp_flags "--no-userinit --non-interactive --eval '(setf sb-impl::*default-external-format* :UTF8)'"

License:        BSD
URL:            https://nyxt.atlas.engineer/
#Source0:        https://github.com/atlas-engineer/%{name}/archive/refs/tags/%{version}.tar.gz
Source0:        https://github.com/atlas-engineer/%{name}/releases/download/%{version}/%{name}-%{version}-source-with-submodules.tar.xz

BuildRequires:  gcc-c++ git make sbcl
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  libfixposix-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  wget

Requires:       pkgconfig(gobject-introspection-1.0)
Requires:       pkgconfig(webkit2gtk-4.0)
Requires:       libfixposix-devel

%description
Nyxt is a keyboard-oriented, infinitely extensible web browser designed for
power users. Conceptually inspired by Emacs and Vim, it has familiar
key-bindings (Emacs, vi, CUA), and is fully configurable in Lisp.

#%prep
#%autosetup
#wget https://beta.quicklisp.org/quicklisp.lisp
#sbcl --load quicklisp.lisp --eval '(quicklisp-quickstart:install)'
#sbcl --load quicklisp.lisp --eval '(ql:add-to-init-file)'

%build
make PREFIX=/usr LISP_FLAGS=%{lisp_flags} all

%install
make PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT LISP_FLAGS=%{lisp_flags} install

%files
/usr/bin/nyxt
/usr/share/applications/nyxt.desktop
/usr/share/icons/hicolor/*/apps/nyxt.png

%changelog
* Sat Sep 9 2023 <kiky.tokamuro@yandex.ru>
- initial release
