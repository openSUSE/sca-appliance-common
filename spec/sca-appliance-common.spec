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
Release:      16
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
Requires:     curl
Requires:     php, php-bz2, php-mbstring, php-mcrypt, php-mysql, php-zip, php-zlib
Requires:     mod_php_any
Requires:     /bin/logger
Requires:     /usr/bin/ssh
Requires:     /usr/sbin/mysqld
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

