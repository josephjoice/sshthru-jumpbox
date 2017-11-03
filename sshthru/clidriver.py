from sshthru.api import SshThru
import sys
import subprocess
import getpass
import click


@click.command()
@click.option('--username','-u',help="Username to use to login.",required=True)
@click.option('--awsprofile','-a',help="AWS Profile name from the credentials file.",required=True)
@click.option('--string','-s',help="Unique string to look for in the instance names.",required=True)
def main(username,awsprofile,string):
    file = awsprofile
    sshThru = SshThru(file)
    instances = sshThru.search(string) 
    index=1;
    for instance in instances:
        try:
            print(str(index)+" "+instance[0]+" "+instance[1]+" "+str(instance[2]))
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
    instanceIp = instances[userSelection][1]
    username = username
    connectString  = sshThru.proxySSHcommand % (username,sshThru.keyfile,instanceIp,sshThru.keyfile,username,sshThru.bastionIp)
    process = subprocess.call(connectString, shell=True)

if __name__ == "__main__":
    main()

