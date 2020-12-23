%define libname zchunk

Name:           lib%{libname}
Version:        1.1.8
Release:        1%{?dist}
Summary:        zchunk is a compressed file format that splits the file into independent chunks

License:        BSD-2-Clause
URL:            https://github.com/zchunk/zchunk
%undefine       _disable_source_fetch
Source0:        https://github.com/zchunk/%{libname}/archive/%{version}.tar.gz#/%{libname}-%{version}.tar.gz
%define         SHA256SUM0 a47c99ecb6edac984056b921619b64ff25609cecdc9645ca6c7279adf20114de

Patch0:         libzchunk-0001-endian-h.patch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/zchunk/zchunk.git",
# X10-Update-Spec:   "pattern": "^((?:\\d+\\.?)+)$" }

BuildRequires:  pkg-config
BuildRequires:  meson
BuildRequires:  ninja-build

BuildRequires:  libopenssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libzstd-devel
BuildRequires:  libargp-devel

Requires:       libopenssl
Requires:       libcurl
Requires:       libzstd
Requires:       libargp

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libffi-devel
Requires:       libzstd-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n zchunk
Summary:        Command-line utilities for libzchunk
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n zchunk

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version} -p0

%build

mkdir build
LDFLAGS=-largp meson -Dbuildtype=release --prefix=%{_prefix} build/
ninja %{?_smp_mflags} -C build

%install
DESTDIR=%{buildroot} ninja -C build install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%{_prefix}/lib/libzck.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libzck.dylib
%{_prefix}/lib/pkgconfig/*.pc

%files -n zchunk
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.1.8-1
  Updated to version 1.1.8.
