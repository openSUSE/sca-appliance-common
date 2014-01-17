# Copyright (C) 2013,2014 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# norootforbuild
# neededforbuild
%define sca_common sca

Name:         sca-appliance-common
Summary:      Supportconfig Analysis Appliance Common Files
URL:          https://bitbucket.org/g23guy/sca-appliance-common
Group:        Documentation/SuSE
Distribution: SUSE Linux Enterprise
Vendor:       SUSE Support
License:      GPL-2.0
Autoreqprov:  on
Version:      1.3
Release:      1
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
Requires:     curl
Requires:     php5, php5-bz2, php5-mbstring, php5-mcrypt, php5-mysql, php5-zip, php5-zlib
Requires:     /bin/logger
Requires:     /usr/bin/ssh
Requires:     /usr/bin/mysql
Requires:     /usr/bin/sed
Requires:     /usr/bin/awk
Requires:     /bin/ping

%description
Provides the common files needed by both the SCA Broker and Agent.

Authors:
--------
    Jason Record <jrecord@suse.com>

%prep
%setup -q

%build

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/srv/www/htdocs/%{sca_common}
install -m 644 websca/* $RPM_BUILD_ROOT/srv/www/htdocs/%{sca_common}
install -m 400 websca/db-config.php $RPM_BUILD_ROOT/srv/www/htdocs/%{sca_common}

%files
%defattr(-,wwwrun,www)
%dir /srv/www/htdocs/%{sca_common}
/srv/www/htdocs/%{sca_common}/*

%changelog
* Thu Jan 16 2014 jrecord@suse.com
- clean up unused variable
- cleaned up spec file
- added pattern link to login screen
- fixed pattern report identifier link
- changed Internal to SRView
- Archive File links of file:// are not supported for hyper links

* Thu Jan 02 2014 jrecord@suse.com
- initialized

