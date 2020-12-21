Name:           
Version:        
Release:        1%{?dist}
Summary:        

License:        
URL:            
%undefine       _disable_source_fetch
Source0:        
%define         SHA256SUM0 0

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

# --------

%build
mkdir build
cd build
cmake -Wno-dev \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%make_build

# --------

%package     -n 
Summary:        Command-line tools and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n 

# --------