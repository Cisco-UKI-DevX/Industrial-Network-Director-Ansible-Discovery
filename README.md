# Industrial Network Director - Automated asset discovery using Ansible

## Asset Discovery with Industrial Network Director (Under development)

This project utilises Cisco Industrial Network Director to automate discovery of devices on a network through the use of ansible playbooks to dynamically create discovery profiles on IND using user provided information.

https://www.cisco.com/c/en/us/products/cloud-systems-management/industrial-network-director/index.html

With the user providing a csv file of the estimated asset information (IP addressing and discovery profile requried) this playbook is able to automatically create the discovery profiles for the devices it is instructed to discover within the IND tool.

Note: csv file must be in the format of the below - See example included within project:

```"name;accessProfileId;protocol;startip;endip;netmask"
name;accessProfileId;protocol;startip;endip;netmask
test01;20100;OPC-UA;192.168.0.0;192.168.0.255;255.255.255.0
test02;20100;OPC-UA;10.10.10.0;10.10.10.255;255.255.255.0
```

*Currently working to remove the need for an accessProfileId field to automatically create access profiles based on protocol*
