# vmchecktools
Features vmchecktools is used for:
- make VMware-Tools installation/update for Linux/Unix as easy as rpm-managment
- copy over pvscsi/vmxnet3 modules for new kernel BEFORE booting into it
  and rebuild initialrd, so they are used during boot (for older kernels)
- reinstall vmware-tools while first boot into a certain kernel

Some comments:
Usable also as standalone script also it's designed as init script.
Heavily tested and productive in a hugh RHEL/CentOS4-7 environment.

A specfile is avail, so a rpm can be build with vmchecktools added as init script
and possibility to add required version of official VMware-Tools into for easy deployment. 
