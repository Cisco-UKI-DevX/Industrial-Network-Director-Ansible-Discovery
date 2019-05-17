# NDO-Industrial

Project focusing on introducing NetDevOps concepts for Industrial Control and Automation Networks. 

Within this repo there is collection of Ansible playbooks, python scripts and walkthroughs covering multiple network automation usecases for Industrial Networks utilising a selection of typical tools. Please find their summaries and walkthroughs below.

#### Please note this is currently a work in progress

## Asset Discovery with Industrial Network Director (Under development)

This playbook utilises Cisco Industrial Network Director to automate discovery of devices on a network.

Through the user providing a csv file of the estimated asset information, this playbook is able to automatically create the discovery profiles for the devices it is instructed to discover within the IND tool. 

Note: csv file must be in the format of the below - See example included within project:

```"name;accessProfileId;protocol;startip;endip;netmask"
name;accessProfileId;protocol;startip;endip;netmask
test01;20100;OPC-UA;192.168.0.0;192.168.0.255;255.255.255.0
test02;20100;OPC-UA;10.10.10.0;10.10.10.255;255.255.255.0
```

//comment about the accessProfileId and how its being fixed


## Future stuff

Additional usecases in development:

* Network performance baselining
* Traffic analysis and reporting
* Configuration Management
