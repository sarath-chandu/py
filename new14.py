import paramiko
import time
import getpass

#   Get username and Password
user =  raw_input("Enter your username: ")
password = getpass.getpass()

#   Open file with list of Swtiches
f = open ("myswitches.txt")

#   SSH to each swtich and configure it
for line in f:
    
    ip_address = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=user,password=password)
    
    print "Successfull connection", ip_address
    
    remote_connection = ssh_client.invoke_shell ()
    
    print "Getting running-config of" + ip_address
    
    remote_connection.send("term len 0\n")
    remote_connection.send("sh running-config\n")
    remote_connection.send("exit\n")
    
    time.sleep(20)
    readoutput = remote_connection.recv(655350)
    saveoutput = open("Backup_Switch_" + ip_address, "w")
   
    print "Saving Configuration in Backup_Switch_" + ip_address + "\n"
   
    saveoutput.write(readoutput)
    saveoutput.write("\n")
   
    saveoutput.close
    ssh_client.close
    