# shoggoth #

A tool utilized to deploy a VMWare Ecosystem onto a specific host through
vCenter. This utility is built off [pyvmomi](https://github.com/vmware/pyvmomi)
while utilizing these [samples](https://github.com/vmware/pyvmomi-community-samples/tree/master/samples).

Converts [deployAm.ps1](https://github.com/Matrix20085/cptSmallTools/blob/main/deployAM.ps1) to python.

# To-Do #

- [ ] Add simple check to make sure the expected number of VMs are present
- [ ] Test boot/invoke-vmscript with the wait-tools option. Need to specify the script type I think
- [ ] Add CPT account to ESXi with full perms
- [ ] Auto-select host and data store one only one option is present.
- [ ] Add reconnect function.
