Name:           bison
Version:        3.7.4
Release:        2%{?dist}
Summary:        A general-purpose parser generator

License:        GPLv3+
URL:            https://www.gnu.org/software/bison/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
%define         SHA256SUM0 a3b5813f48a11e540ef26f46e4d288c0c25c7907d9879ae50e430ec49f63c010

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/bison/"}

Provides:       gbison = %{version}-%{release}

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure --bindir=%{_prefix}/opt/bin --disable-static
%make_build

%install
%make_install

# macOS provides its own bison so link as gbison
install -dm755 %{buildroot}%{_bindir}
for f in $(ls %{buildroot}%{_prefix}/opt/bin); do
    ln -sv ../opt/bin/$f %{buildroot}%{_bindir}/g$f
done

%find_lang %{name}
%find_lang %{name}-gnulib
%find_lang %{name}-runtime

rm -f %{buildroot}%{_infodir}/dir

%files -f %{name}.lang -f %{name}-gnulib.lang -f %{name}-runtime.lang
%license COPYING
%{_bindir}/*
%{_prefix}/opt/bin/*
%exclude %{_prefix}/lib/liby.a
%{_datadir}/bison
%{_datadir}/aclocal/bison-i18n.m4
%doc %{_datadir}/doc/bison
%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.7.4-2
  Rebuilt with dependency generation.
