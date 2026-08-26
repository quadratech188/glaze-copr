%global forgeurl https://github.com/stephenberry/glaze

Name: glaze
Version: 8.1.0
Release: %autorelease
Summary: Extremely fast, in memory, serialization, reflection, and RPC library for C++. JSON, BEVE, BSON, CBOR, CSV, JSONB, MessagePack, TOML, YAML, EETF

%{forgemeta}
License: MIT
URL: %{forgeurl}
Source0: %{forgesource}

BuildRequires: cmake
BuildRequires: g++

BuildArch: noarch

%description
One of the fastest JSON libraries in the world. Glaze reads and writes from
object memory, simplifying interfaces and offering incredible performance.

%prep
%forgeautosetup

%conf
%cmake -Dglaze_DEVELOPER_MODE=OFF -DBUILD_TESTING=OFF

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_includedir}/glaze/
%{_datadir}/glaze/

%changelog
%autochangelog
