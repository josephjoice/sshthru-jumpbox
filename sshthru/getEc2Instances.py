import boto3
from bson import json_util
import json
import sys
import subprocess
import configparser
from os.path import expanduser

class SshThru:
    def __init__(self):
        home = expanduser("~")
        self.configFile=home+"/.sshthru"
        self.loadConfigs()
        self.proxySSHcommand = "ssh -o StrictHostKeyChecking=no -l ec2-user -i  %s %s -o ProxyCommand=\"ssh -i %s   -v -W %%h:%%p ec2-user@%s\""


    def loadConfigs(self):
        config = configparser.ConfigParser()
        config.read(self.configFile)
        try:
            account = config['authoring']
            keyfile = account.get("key")
            bastionIp = account.get('bastionIp')
            print("Reading configs from "+self.configFile)
        except:
            config['authoring'] = {}
            account  = config['authoring']
            keyfile = self.getKeyFileLocation()
            bastionIp = self.getBastionIp()
        config['authoring']['key'] = keyfile
        config['authoring']['bastionIp'] = bastionIp
        with open(self.configFile,'w+') as configFile:
            config.write(configFile)
        self.keyfile = keyfile
        self.bastionIp = bastionIp
        

    
    def getKeyFileLocation(self):
        print("Enter the location of key file : "),
        key = raw_input()
        return key

    def getBastionIp(self):
        print("Getting bastion")
        instances = self.getMatchingASGInstances("bastion")
        instances = self.getInstanceIP(instances)
        return instances[0]["PublicIpAddress"]

        

    def getMatchingASGInstances(self,str):
        client = boto3.client('autoscaling')
        response = client.describe_auto_scaling_groups()
        autoscalingGroups = response['AutoScalingGroups']
        instanceList = list()
        for asg in autoscalingGroups:
            if str in asg['AutoScalingGroupName']:
                for instance in asg['Instances']:
                    instanceList.append(instance['InstanceId'])
        return instanceList
    
    def getInstanceIP(self,instances):
        client = boto3.client('ec2')
        response = client.describe_instances(InstanceIds=instances)
        instanceList = []
        for reservation in response['Reservations']:
            instanceList.extend(reservation['Instances'])
        return instanceList
    
    def exceptionEasterEgg(self):
        process = subprocess.Popen("open http://i.imgur.com/UnAOggP.gif", shell=True, stdout=subprocess.PIPE)
    
    
  
