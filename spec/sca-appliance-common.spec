# spec file for package sca-appliance-common
#
# Copyright (C) 2014 SUSE LLC
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# norootforbuild
# neededforbuild
%define sca_common sca

Name:         sca-appliance-common
Summary:      Supportconfig Analysis Appliance Common Files
URL:          https://bitbucket.org/g23guy/sca-appliance-common
Group:        System/Monitoring
License:      GPL-2.0
Autoreqprov:  on
Version:      1.3
Release:      13
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
Requires:     curl
Requires:     php5, php5-bz2, php5-mbstring, php5-mcrypt, php5-mysql, php5-zip, php5-zlib
Requires:     apache2-mod_php5
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
install -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{sca_common}
install -m 444 docs/COPYING.GPLv2 $RPM_BUILD_ROOT/usr/share/doc/packages/%{sca_common}
install -m 644 websca/* $RPM_BUILD_ROOT/srv/www/htdocs/%{sca_common}
install -m 600 websca/db-config.php $RPM_BUILD_ROOT/srv/www/htdocs/%{sca_common}
install -m 600 websca/web-config.php $RPM_BUILD_ROOT/srv/www/htdocs/%{sca_common}

%files
%defattr(-,wwwrun,www)
%dir /srv/www/htdocs/%{sca_common}
%dir /usr/share/doc/packages/%{sca_common}
/srv/www/htdocs/%{sca_common}/*
%doc /usr/share/doc/packages/%{sca_common}/*

%changelog

