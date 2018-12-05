#%define toolsv4 8.3.12-493255
#%define toolsv5 8.6.0-515842
#%define toolsv5 8.6.5-652272
#%define toolsv5 9.0.0-782409
#%define toolsv5 9.0.5-1065307
#%define toolsv5 9.0.5-1137270
#%define toolsv5 9.4.0-1399439
#%define toolsv5 9.4.5-1598834
#%define toolsv5 9.4.5-1734305
#%define toolsv5 9.4.6-1770165
#%define toolsv5 9.4.10-2092844
#%define toolsv5 9.4.11-2400950
#%define toolsv5 9.4.12-2627939
#%define toolsv6 9.10.1-2791197
#%define toolsv6 9.10.5-2981885
#%define toolsv6 10.0.0-3000743
#%define toolsv6 10.0.6-3560309
#%define toolsv6 10.0.9-3917699
#%define toolsv6 10.1.0-4449150
#%define toolsv6 10.1.7-5541682
#%define toolsv6 10.1.15-6677369
#%define toolsv6 10.2.0-7253323
#%define toolsv6 10.2.5-8068406
%define toolsv6 10.3.2-9925305
%define oldinitscript vmware-check-tools
%define oldname vmware-tools-check
%define lockdir /var/lock/subsys
%define tmpdir /var/tmp

Summary: Install vmware-tools for current kernel at boot
Name: vmchecktools
Version: 1
Release: 49
License: GPL
Group: System Environment/Base
Source0: %{name}
#Source1: VMwareTools-%toolsv4.tar.gz
#Source2: VMwareTools-%{toolsv5}.tar.gz
Source3: VMwareTools-%{toolsv6}.tar.gz
BuildRoot: /tmp/%{name}-buildroot
BuildArch: noarch
Packager:  Monster Technologies (unix@monster.com)
Vendor: Monster
Provides: vmware-tools-check = 0:1-15
Obsoletes: vmware-tools-check < 0:1-15
%define _source_payload w9.gzdio
%define _binary_payload w9.gzdio
%define _source_filedigest_algorithm  1
%define _binary_filedigest_algorithm  1

%description
After a kernel upgrade the vmware-tools need to be re-install
vmware-tools-check will install the vmware-tools at boot once.
This should be run before network starts.
While next boot will end-up in a new kernel, initrd will be
re-build with latest pvscsi, vmxnet and vmxnet3 modules. This
enshures that latest modules are available at boot.
Includes latest vmware-tools for ESXi5 and later.

%prep
%setup -T -c -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_initrddir}/%{name}
#install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_initrddir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{tmpdir}/%{name}
#cp %{SOURCE1} $RPM_BUILD_ROOT/%{tmpdir}/%{name}
#cp %{SOURCE2} $RPM_BUILD_ROOT/%{tmpdir}/%{name}
cp %{SOURCE3} $RPM_BUILD_ROOT/%{tmpdir}/%{name}
cd $RPM_BUILD_ROOT/%{tmpdir}/%{name}
#echo %toolsv4|sed "s/-/ build-/" > vmware-tools-v4.ver
#echo %toolsv5|sed "s/-/ build-/" > vmware-tools-v5.ver

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ $1 -eq 1 ] ; then # package is installed, not upgraded 
  /sbin/chkconfig --add %{name}
  /sbin/chkconfig %{name} on
elif [ $1 -gt 1 ] ; then # package is upgraded  
  /sbin/chkconfig --add %{name}
  /sbin/chkconfig %{name} reset
  /sbin/chkconfig %{name} resetpriorities
fi
touch %{lockdir}/%{name}
# cleanup from older version with init script before rename
if [ -e %{_initrddir}/%{oldinitscript} ]; then
  /sbin/chkconfig --del %{oldinitscript}
  if [ -e %{lockdir}/%{oldinitscript} ]; then
    rm -f %{lockdir}/%{oldinitscript}
  fi
  ln -s %{_initrddir}/%{oldinitscript} %{_initrddir}/%{oldname}
  # now old package should be removable
else
  if [ -h %{_initrddir}/%{oldname} ]; then
    rm %{_initrddir}/%{oldname}
  fi
  if [ -d %{tmpdir}/%{oldname} ]; then
    rmdir %{tmpdir}/%{oldname}
  fi 
fi

%preun
if [ $1 -eq 0 ]; then # package is being erased, not upgraded
  /sbin/chkconfig --del %{name}
  if [ -e %{lockdir}/%{name} ]; then
    rm -f %{lockdir}/%{name}
  fi
fi

%files
%defattr(-,root,root)
%{_initrddir}/%{name}
#%{tmpdir}/%{name}/*
#%{tmpdir}/%{name}/%{Source1}
#%{tmpdir}/%{name}/vmware-tools-v4.ver
#%{tmpdir}/%{name}/VMwareTools-%{toolsv5}.tar.gz
%{tmpdir}/%{name}/VMwareTools-%{toolsv6}.tar.gz
#%{tmpdir}/%{name}/vmware-tools-v5.ver

#TODO:
# - only binaries within vmware-tools-distrib/lib/modules/binary/bld-2.6.18-8.el5-x86_64smp-RHEL5/objects/vmxnet3.o required

%changelog
* Thu Jul 12 2018 Alexander Spannagel
- added newest vmchecktools script (1.35)
* Fri Apr 20 2018 Alexander Spannagel
- upgrade to latest VMwareTools-10.2.5-8068406
- added newest vmchecktools script (1.34)
  added ENABLE_CAF=no to vmware-config
* Fri Jan 12 2018 Alexander Spannagel
- upgrade to latest VMwareTools-10.2.0-7253323
* Mon Oct 09 2017 Alexander Spannagel
- upgrade to latest VMwareTools-10.1.15-6677369
* Wed Jun 28 2017 Alexander Spannagel
- upgrade to latest VMwareTools-10.1.7-5541682
- added newest vmchecktools script (1.31)
  added detection of ESXi6.5
  giving status of vmtoolsd
* Tue Mar 28 2017 Alexander Spannagel
- upgrade to latest VMwareTools-10.1.0-4449150
* Wed Sep 28 2016 Alexander Spannagel
- added newest vmchecktools script (1.27) - added handling of open-vm-tools
* Wed Aug 22 2016 Alexander Spannagel
- upgrade to latest 10.0.9-3917699
- added newest vmchecktools script (1.26) - added detection of ESXi6U1
* Wed Apr 06 2016 Alexander Spannagel
- upgrade to latest 10.0.6-3560309
* Fri Mar 11 2016 Alexander Spannagel
- upgrade to latest 10.0.0-3000743
* Tue Sep 11 2015 Alexander Spannagel
- upgrade to latest VMwareTools-9.10.5-2981885
* Tue Aug 11 2015 Alexander Spannagel
- added newest vmchecktools script (1.25) - added detection of ESXi6
- upgrade to latest VMwareTools-9.10.1-2791197
* Tue May 19 2015 Alexander Spannagel
- added newest vmchecktools script (1.24)
* Tue May 19 2015 Alexander Spannagel
- added newest vmchecktools script (1.23)
- upgrade to latest VMwareTools-9.4.12-2627939
* Thu Feb 26 2015 Alexander Spannagel
- added newest vmchecktools script (1.21)
  fixing broken upgrade due to mkinitrd exit status
* Fri Feb 13 2015 Alexander Spannagel
- upgrade to latest VMwareTools-9.4.11 build-2400950
* Thu Oct 30 2014 Alexander Spannagel
- upgrade to latest VMwareTools-9.4.10-2092844
- added newest vmchecktools script (1.19) - detect ESXi5.5U2
* Tue Aug 26 2014 Alexander Spannagel
- upgrade to latest VMwareTools-9.4.6-1770165
* Tue Jul 01 2014 Alexander Spannagel
- upgrade to latest VMwareTools-9.4.5-1734305
- added newest vmchecktools script (1.18) - keep /boot cleaner
* Tue Apr 01 2014 Alexander Spannagel
- upgrade to latest VMwareTools-9.4.5-1598834
* Tue Jan 21 2014 Alexander Spannagel
- upgrade to latest VMwareTools-9.4.0-1399439
* Tue Jan 21 2014 Alexander Spannagel
- added newest vmchecktools script (1.17) - added detection of ESXi5.5
* Tue Jan 07 2014 Alexander Spannagel
- added newest vmchecktools script (1.16) - removing dmidecode requiremnt on RHEL/CentOS6
* Wed Oct 02 2013 Alexander Spannagel
- upgrade to latest VMwareTools-9.0.5-1137270
* Wed Jul 17 2013 Alexander Spannagel
- added newest vmchecktools script (1.14) - fully support of RHEL/CentOS6
* Wed Jul 10 2013 Alexander Spannagel
- upgrade to latest VMwareTools-9.0.5-1065307
- added newest vmchecktools script (1.12)
* Tue Apr 16 2013 Alexander Spannagel
- upgrade to latest VMwareTools-9.0.0-782409
* Tue Jan 29 2013 Alexander Spannagel
- upgrade to latest VmwareTools-8.6.10-913593
- remove fixed version - always take latest
* Fri Oct 19 2012 Alexander Spannagel
- added latest init scipt
* Thu Aug 30 2012 Alexander Spannagel
- added latest init scipt fixing hang of mkinitrd
- fix init script name of older rpm, so it can be erased without --nopreun
* Mon Aug 27 2012 Alexander Spannagel
- for v5 alternative use latest Tools within /var/tmp/vmchecks 
- always clobber pvscsi, vmxnet, vmxnet3
- fixing problem seen with mkinitrd
* Fri Aug 03 2012 Alexander Spannagel
- rename package from vmware-tools-check to vmchecktools
- reorg as start/stop/install are the same
- re-run vmware-config-tools for kernel modules 
* Wed Aug 01 2012 Alexander Spannagel
- adding lock handeling
* Tue Jul 31 2012 Alexander Spannagel
- fix rebuild initrd after upgrade
- upgrade vmware-tools before reboot
- running chkconfig with reset+resetpriorities 
- remove vmware-tools for ver4 and earlier
* Wed Jul 25 2012 Alexander Spannagel
- adding check to rebuild initrd after upgrade 
- writing lock so stop will work
- fix logic for new kernel - take the one server boots
* Tue Jun 12 2012 Alexander Spannagel
- updrade toolsv5 to 8.6.5-652272
* Fri Mar 23 2012 Alexander Spannagel
- fix Bios Release 10/13/2009 is also ESX5
- get rid of symlinks within tmpdir
* Fri Mar 23 2012 Alexander Spannagel
- fix logic for latest version
- Bios release >2009 looks like ESX5
- renamed init so it may install before usual tools start
* Wed Mar 21 2012 Alexander Spannagel
- fix typo within init script
* Wed Mar 21 2012 Alexander Spannagel
- fix upgrade so current version and available version are compared
- skip install if installed version is newer
- cleanup vmware-tools-distrib after install
* Tue Mar 20 2012 Alexander Spannagel
- upgraded toolsv5 to 8.6.0-515842
* Mon Mar 19 2012 Alexander Spannagel
- check for esx5 and use best matching VMware-Tools
- use same chkconfig line as vmware-tools within init-script
* Mon Feb 20 2012 Alexander Spannagel
- initial spec
