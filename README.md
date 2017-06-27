# sshthru
A dumb script which simply generates a ssh-proxy command string, which is commonly used to login to private instances through a bastion host.

*Disclaimer*

This script assumes that the aws account which is configured in `~/.aws/credentials` are created using the [ctgdevops](https://github.intuit.com/ctgdevops/deployment-patterns) patterns.

**Usage**

You can use the script to login to an instance in any availability group by giving some uniquely identifiable portion of that ASG name.
First time when the script is run, a config file is created `~/.sshthru` which will have the key and bastion ip. If the file is not found the key file location will be requested again.
The bastion Ip is found out looking for a ASG which has `bastion` in its name. You can manually update it in the config file as well.
```
$ python -m sshthru dev
Enter the location of key file :   ~/Downloads/cms-authoring-key1\ \(1\).pem
Getting bastion
1 10.131.152.158 running 2017-06-27 14:43:39+00:00
OpenSSH_7.4p1, LibreSSL 2.5.0
debug1: Reading configuration data /Users/jjoice/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
....
```
```
$ python -m sshthru dev
Reading configs from /Users/jjoice/.sshthru
1 10.131.153.20 running 2017-06-21 21:01:39+00:00
OpenSSH_7.4p1, LibreSSL 2.5.0
```
