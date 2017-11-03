# sshthru
A dumb script which simply generates a ssh-proxy command string, which is commonly used to login to private instances through a bastion host.


**Installation**

`git clone` and `python setup.py install`

or

`pip install git+https://github.intuit.com/jjoice/sshthru.git`

**Requirements**

This program expects your aws credentials in the ~/.aws/credentials file in the following format

```
[auth-preprod]
aws_access_key_id = AKIAJ5XXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXX
region=us-west-2
[ttcom-preprod]
aws_access_key_id = XXXXXXXXXXXXXXXXXXXX
aws_secret_access_key = XXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Usage**

You can use the script to login to an instance  by giving some unique portion of the instance name.
First time when the script is run, a config file is created `~/.<profile-name>` which will have the key and bastion ip. If the file is not found the key file location will be requested again.
The bastion Ip is found out looking for an instance which has `bastion` in its name. You can manually update it in the config file as well.


```
sshthru -u <username> -s <unique-string-in-asg-name> -a <aws-profile-to-use>
$ sshthru -u jjoice -a auth-preprod -s cdev
Enter the location of key file :   ~/Downloads/cms-authoring-key.pem
Getting bastion
1 wp-authoring-cdev-web-app-deploy-20171026-031237 10.131.153.89 2017-10-30 10:30:24+00:00
********************************************************************************
This is a private computer system containing information that is proprietary
....
```

```
$ sshthru -u jjoice -a auth-preprod -s perf
Reading configs from /Users/jjoice/.sshthru
1 wp-authoring-perf-web-app-deploy-20171026-031237 10.131.153.82 2017-10-30 10:30:24+00:00
********************************************************************************
This is a private computer system containing information that is proprietary
```
