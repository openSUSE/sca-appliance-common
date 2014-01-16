# Copyright (C) 2013 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# norootforbuild
# neededforbuild
%define sca_common sca

##################################################################
## Update FPAT_URL in reportfull.php before release
##################################################################

Name:         sca-appliance-common
Summary:      Supportconfig Analysis Appliance Common Files
URL:          https://bitbucket.org/g23guy/sca-appliance-common
Group:        Documentation/SuSE
Distribution: SUSE Linux Enterprise
Vendor:       SUSE Support
License:      GPL-2.0
Autoreqprov:  on
Version:      1.2
Release:      2
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
Provides the common files needed by both the Broker and the Agent.

Authors:
--------
    Jason Record <jrecord@suse.com>

%prep
%setup -q

%build

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/srv/www/htdocs/sca
install -m 644 websca/* $RPM_BUILD_ROOT/srv/www/htdocs/sca
install -m 400 websca/db-config.php $RPM_BUILD_ROOT/srv/www/htdocs/sca

%files
%defattr(-,wwwrun,www)
%dir /srv/www/htdocs/sca
/srv/www/htdocs/sca/*

%changelog
* Wed Jan 15 2014 jrecord@suse.com
- added pattern link to login screen
- fixed pattern report identifier link
- changed Internal to SRView
- Archive File links of file:// are not supported for hyper links

* Thu Jan 02 2014 jrecord@suse.com
- initialized

