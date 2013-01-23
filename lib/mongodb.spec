Summary: MongoDB server
Name: mongodb
Version: %{mongo_version}%{?dist}
Release: %{release} 
Source0: mongodb-linux-x86_64-%{mongo_version}.tgz
Source1: mongos.init
Source2: mongod.init

License: LGPL
Group: Applications/System

# Disables automatic dependencies in order to allow for using an alternate RPM database:
AutoReqProv: no

# Makes the package relocatable:
Prefix: /usr/share

BuildArch: x86_64
 
# Disables debug packages and stripping of binaries:
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

# Crank up the compression
%define _binary_payload w7.lzdio
 
%description
MongoDB Server
 
%prep
%setup -c

%build
 
%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/usr/share/mongodb
cp -R . %{buildroot}/usr/share/mongodb
install -d %{buildroot}/%{_initrddir}/
install -m 755 %{SOURCE1} %{buildroot}/%{_initrddir}/mongos
install -m 755 %{SOURCE2} %{buildroot}/%{_initrddir}/mongod

%clean

%files
%defattr(-,root,root)
# Removes user/group verification to support installation as a non-root user:
%verify(not user group) /usr/share/%{name}
%{_initrddir}/mongos
%{_initrddir}/mongod
 
%changelog
* Wed Jan 23 2013 Lee Thompson <thompson@dtosolutions.com> 2.2.2
    - add some RPM syntax sugar like dist and compression
* Fri Jun 3 2011 Chuck Scott <chuck@dtosolutions.com> 2.2-2
    - test the changelong
