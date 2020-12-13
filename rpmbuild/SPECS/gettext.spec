Name:           gettext
Version:        0.21
Release:        1%{?dist}
Summary:        An internationalization library

License:        GPLv3+
URL:            https://gnu.org/software/gettext
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 c77d0da3102aec9c07f43671e60611ebff89a996ef159497ce8e59d075786b12

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/gettext/"}

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure --disable-static --libdir=%{_prefix}/lib
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%find_lang gettext-runtime
%find_lang gettext-tools

%files -f gettext-runtime.lang -f gettext-tools.lang
# this should be split but i'm having an awful case of the not-giving-a-s**ts
%license COPYING
%{_bindir}/autopoint
%{_bindir}/envsubst
%{_bindir}/gettext
%{_bindir}/gettext.sh
%{_bindir}/gettextize
%{_bindir}/msgattrib
%{_bindir}/msgcat
%{_bindir}/msgcmp
%{_bindir}/msgcomm
%{_bindir}/msgconv
%{_bindir}/msgen
%{_bindir}/msgexec
%{_bindir}/msgfilter
%{_bindir}/msgfmt
%{_bindir}/msggrep
%{_bindir}/msginit
%{_bindir}/msgmerge
%{_bindir}/msgunfmt
%{_bindir}/msguniq
%{_bindir}/ngettext
%{_bindir}/recode-sr-latin
%{_bindir}/xgettext
%{_prefix}/lib/*.dylib
%{_prefix}/lib/gettext
%{_includedir}/*
%{_datadir}/gettext
%{_datadir}/gettext-%{version}
%{_datadir}/aclocal/*.m4
%{_datadir}/locale/locale.alias
%doc %{_infodir}/*.info*
%doc %{_mandir}/man{1,3}/*
%doc %{_docdir}/gettext
%doc %{_docdir}/libtextstyle
%doc %{_docdir}/libasprintf
%changelog
