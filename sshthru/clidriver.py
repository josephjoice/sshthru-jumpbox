from sshthru.getEc2Instances import SshThru
import sys
import subprocess



def main():
    file = sys.argv[2]
    sshThru = SshThru(file)
    instances = sshThru.getMatchingASGInstances(sys.argv[1]) 
    instances = sshThru.getInstanceIP(instances)
    index=1;
    for instance in instances:
        try:
            print(str(index)+" "+instance['PrivateIpAddress']+" "+instance['State']['Name']+" "+str(instance['LaunchTime']))
            index =  index+1
        except:
            print "",
    if(len(instances) == 1):
        userSelection = 0
    else:
        try:
            print ("Enter your option :"),
            userSelection = int(raw_input())
            userSelection = userSelection - 1; 
            if (userSelection > len(instances) or userSelection < 0):
                raise 
        except Exception as e:
            sshThru.exceptionEasterEgg()
            print("I failed you. (Invalid option)")
    instanceIp = instances[userSelection]['PrivateIpAddress']
    connectString  = sshThru.proxySSHcommand % (sshThru.keyfile,instanceIp,sshThru.keyfile,sshThru.bastionIp)
    process = subprocess.call(connectString, shell=True)

