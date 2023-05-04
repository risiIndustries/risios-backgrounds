Name:		risios-backgrounds
Version:	38
Release:	13%{?dist}
Summary:	Wallpapers for risioS

License:	GPL v3
URL:		risi.io
Source0:	https://github.com/risiIndustries/risios-backgrounds/archive/refs/heads/main.tar.gz

BuildArch:	noarch

%description
Package hosting wallpapers for risiOS

%package 36
Summary: 	risiOS 36 Wallpapers
Conflicts:  risios-36-backgrounds
Provides:	  risios-36-backgrounds

%description 36
risiOS 36 Wallpapers

%package 37
Summary: 	risiOS 37 Wallpapers

%description 37
risiOS 37 Wallpapers

%package 38
Summary: 	risiOS 38 Wallpapers

%description 38
risiOS 38 Wallpapers

%prep
%autosetup -n risios-backgrounds-main
%build

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds

cp -a risios-*/ %{buildroot}%{_datadir}/backgrounds
cp -a gnome-background-properties %{buildroot}%{_datadir}/gnome-background-properties

%files 36
%{_datadir}/backgrounds/risios-36-backgrounds
%{_datadir}/gnome-background-properties/risios-36-backgrounds.xml

%files 37
%{_datadir}/backgrounds/risios-37
%{_datadir}/gnome-background-properties/risios-37.xml

%files 38
%{_datadir}/backgrounds/risios-38
%{_datadir}/gnome-background-properties/risios-38.xml

%changelog
* Sun Jan 9 2022 PizzaLovingNerd
- risiOS 36 Wallpapers
