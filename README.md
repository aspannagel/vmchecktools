# vmchecktools
Features vmchecktools is used for:
- make VMware-Tools installation/update for Linux/Unix as easy as rpm-managment
- copy over pvscsi/vmxnet3 modules for new kernel BEFORE booting into it
  and rebuild initrd, so they are used during boot (for older kernels)
- reinstall vmware-tools while first boot into a certain kernel

Some comments:
- written as init-script, alos usable as standalone script
- heavily tested and productive in a hugh RHEL/CentOS4-7 environment.
- spec-file is avail, so a rpm can be build with vmchecktools and official VMware-Tools 
