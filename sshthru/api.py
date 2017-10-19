import boto3
from bson import json_util
import json
import sys
import subprocess
import configparser
import os
import threading
from os.path import expanduser

class SshThru:
    def __init__(self,file):
        os.environ['AWS_PROFILE'] = file
        home = expanduser("~")
        self.configFile=home+"/."+file
        self.loadConfigs()
        self.proxySSHcommand = "ssh -o StrictHostKeyChecking=no -l %s -i  %s %s -o ProxyCommand=\"ssh -o StrictHostKeyChecking=no -i %s -W %%h:%%p %s@%s\""


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
        instanceIp = self.getPublicIpFromName("bastion")
        return instanceIp


    def get_filter(self,name,value):
        return {
            'Name': '%s' % name,
            'Values': ['%s' % value]
        }

    def getmatchingInstancesFromName(self,str):
        client = boto3.client('ec2')
        filter = self.get_filter("tag:Name","*"+str+"*")
        response = client.describe_instances(Filters =[ filter ])
        instanceList = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instanceList.append((self.getNameFromTags(instance['Tags']),instance['PrivateIpAddress'],instance['LaunchTime']))
        return instanceList
       
    def getPublicIpFromName(self,str):
        client = boto3.client('ec2')
        filter = self.get_filter("tag:Name","*"+str+"*")
        response = client.describe_instances(Filters =[ filter ])
        instanceList = []
        return response['Reservations'][0]['Instances'][0]['PublicIpAddress']
 
    
    def getInstanceIP(self,instances):
        client = boto3.client('ec2')
        response = client.describe_instances(InstanceIds=instances)
        instanceList = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instanceList.append(instance['PrivateIpAddress'])
        return instanceList
    
    def exceptionEasterEgg(self):
        process = subprocess.Popen("open http://i.imgur.com/UnAOggP.gif", shell=True, stdout=subprocess.PIPE)

    def search(self,str):
        instances = []
        instances.extend(self.getmatchingInstancesFromName(str))
        return instances

    def getNameFromTags(self,tags):
        for tag in tags:
            if tag['Key'] == 'Name':
                return tag['Value']
        
        


