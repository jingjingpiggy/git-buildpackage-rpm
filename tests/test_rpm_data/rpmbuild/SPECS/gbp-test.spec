Name:       gbp-test
Summary:    Test package for git-buildpackage
Version:    1.0
Release:    1
Group:      Development/Libraries
License:    GPLv2
Source:     %{name}-%{version}.tar.bz2
Source1:    foo.txt
Source20:   bar.tar.gz
# GbpIgnorePatch: 0
Patch0:     my.patch
Patch10:    my2.patch
Patch20:    my3.patch


%description
Package for testing the RPM functionality of git-buildpackage.


%prep
%setup -n %{name} -a 20

%patch0
%patch10 -p1


%build
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -R * %{buildroot}/%{_datadir}/%{name}
install %{SOURCE0} %{buildroot}/%{_datadir}/%{name}



%files
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}
