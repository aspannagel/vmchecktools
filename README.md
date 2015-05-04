# vmchecktools
Easily upgrade of VMware-Tools taking care of kernel updates on Linux VM's

This script project was intential born while a hugh amount of virtual RedHat/CentOS
servers needed to be kept current as easly as possibly.
Especially servers using pvscsi and vmxnet3 kernel modules required more than one reboot
during patching cycles that included kernel upgrades. For a few hunderds of servers that
has taken it's time due to the required manual intervention. Additional it was intended
to replace a half automated upgrade of the vmware-tools that also has eaten up a lot of
time during patching cycles.
The idea was born to look for something to make this as easily as upgrading any other 
package in an satserv/apcewalk managed environment. As none of the scripts found on the 
web did all the above, the idea of writting an own was born to safe the syasdmins day...

Features vmchecktools is used for:
- make VMware-Tools installation/update for Linux/Unix as easy as package-managment
- copy over pvscsi/vmxnet3 modules for new kernel BEFORE booting into it
  and rebuild initrd, so they are used during boot (required for older kernels)
- reinstall vmware-tools while first boot into a new kernel
- provide infos about used distro, kernel, esx-host and vmwaretools  

Some comments:
- written as init-script, also usable as standalone script
- heavily tested and productive in a hugh RHEL/CentOS[4-7] environment
- spec-file is avail, so a rpm can be build with vmchecktools and official VMware-Tools 

