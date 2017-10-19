from sshthru.api import SshThru
import sys
import subprocess
import getpass

def main():
    file = sys.argv[3]
    sshThru = SshThru(file)
    instances = sshThru.search(sys.argv[2]) 
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
    username = sys.argv[1]
    connectString  = sshThru.proxySSHcommand % (username,sshThru.keyfile,instanceIp,sshThru.keyfile,username,sshThru.bastionIp)
    process = subprocess.call(connectString, shell=True)

if __name__ == "__main__":
    main()
