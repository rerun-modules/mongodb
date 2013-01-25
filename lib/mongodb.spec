Summary: MongoDB server
Name: mongodb
Version: %{mongo_version}
Release: %{release}%{?dist}
Source0: mongodb-linux-x86_64-%{mongo_version}.tgz
Source1: mongos.init
Source2: mongod.init

License: LGPL
Group: Applications/System

# Disables automatic dependencies in order to allow for using an alternate RPM database:
AutoReqProv: no

# Makes the package relocatable:
Prefix: /usr

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
install -d -m 755 %{buildroot}/%{_datadir}/doc/%{name}
cp ./mongodb-linux-x86_64-%{mongo_version}/GNU* %{buildroot}/%{_datadir}/doc/%{name}
cp ./mongodb-linux-x86_64-%{mongo_version}/REA* %{buildroot}/%{_datadir}/doc/%{name}
cp ./mongodb-linux-x86_64-%{mongo_version}/THI* %{buildroot}/%{_datadir}/doc/%{name}
install -d -m 755 %{buildroot}/%{_bindir}
cp ./mongodb-linux-x86_64-%{mongo_version}/bin/* %{buildroot}/%{_bindir}/
install -d %{buildroot}/%{_initrddir}/
install -m 755 %{SOURCE1} %{buildroot}/%{_initrddir}/mongos
install -m 755 %{SOURCE2} %{buildroot}/%{_initrddir}/mongod

%clean

%pre
# make sure the jboss-as user and group exist:
if id mongod > /dev/null 2>&1
then
  :
else
  groupadd -f mongod
  useradd -rd %{_datadir}/doc/%{name} -g mongod mongod
  passwd -l mongod
fi

%files
%defattr(-,root,root)
# Removes user/group verification to support installation as a non-root user:
/usr
%{_initrddir}/mongos
%{_initrddir}/mongod
 
%changelog
* Wed Jan 23 2013 Lee Thompson <thompson@dtosolutions.com> 2.2.2
    - add some RPM syntax sugar, FHS, dist and compression
* Fri Jun 3 2011 Chuck Scott <chuck@dtosolutions.com> 2.2-2
    - test the changelong
