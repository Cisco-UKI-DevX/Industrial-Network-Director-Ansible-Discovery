# NDO-Industrial

Project focusing on introducing NetDevOps concepts for Industrial Control and Automation Networks.

Within this repo there is collection of Ansible playbooks, python scripts and walkthroughs covering multiple network automation usecases for Industrial Networks utilising a selection of tools. Please find their summaries and walkthroughs below.

## Asset Discovery with Industrial Network Director

By providing a csv file, of the estimated asset information this playbook is able to automatically create the discovery profiles for the devices it is instructed to discover. 

Note: csv file must be in the format of the below:

```"name;accessProfileId;protocol;startip;endip;netmask"``` 

See example included within project

Additional usecases in development:

* Network performance baselining
* Traffic 
* Configuration Management
