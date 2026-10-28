%global forgeurl https://github.com/stephenberry/glaze

Name: glaze
Version: 9.1.0
Release: %autorelease
Summary: Extremely fast, in memory, serialization, reflection, and RPC library for C++. JSON, BEVE, BSON, CBOR, CSV, JSONB, MessagePack, TOML, YAML, EETF

%{forgemeta}
License: MIT
URL: %{forgeurl}
Source0: %{forgesource}
Patch0: 2977.patch

BuildRequires: cmake
BuildRequires: g++

BuildArch: noarch

%description
One of the fastest JSON libraries in the world. Glaze reads and writes from
object memory, simplifying interfaces and offering incredible performance.

%prep
%forgeautosetup -p1

%conf
# The cmake(glaze) provide is only found when cmake files are in that dir
%cmake \
	-Dglaze_DEVELOPER_MODE=OFF \
	-DBUILD_TESTING=OFF \
	-Dglaze_INSTALL_CMAKEDIR="%{_libdir}/cmake/glaze"

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
%{_libdir}/cmake/glaze/

%changelog
%autochangelog
