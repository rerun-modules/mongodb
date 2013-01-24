Summary: MongoDB server configuration
Name: mongodb-config
Version: %{mongodb_config_version}%{?dist}
Release: %{release} 
Source0: mongodb.conf

License: LGPL
Group: Applications/System

# Disables automatic dependencies in order to allow for using an alternate RPM database:
AutoReqProv: no

# Makes the package relocatable:
Prefix: /

BuildArch: noarch

Requires: mongodb
 
# Disables debug packages and stripping of binaries:
%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post %{nil}

# Crank up the compression
%define _binary_payload w7.lzdio
 
%description
MongoDB Server Configuration
 
%prep

%build
 
%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/etc
install -m 755 %{SOURCE0} %{buildroot}/etc/mongodb.conf

%clean

%pre

%files
%defattr(-,root,root)
# Removes user/group verification to support installation as a non-root user:
/etc/mongodb.conf
 
%changelog
* Wed Jan 24 2013 Chuck Scott <chuck@dtosolutions.com> 1.0.0
    - initial configuration
