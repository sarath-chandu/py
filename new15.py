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
    
    Host = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=Host,username=user,password=password)
    
    print "Successfull connection", Host
    
    remote_connection = ssh_client.invoke_shell ()
    
    print "Getting log of" + Host
    
    remote_connection.send("term len 0\n")
    remote_connection.send("sh ip int brief\n")
    remote_connection.send("sh ip route\n")
    remote_connection.send("sh int status | i connected\n")
    remote_connection.send("sh log\n")
    remote_connection.send("exit\n")
    
    time.sleep(20)
    readoutput = remote_connection.recv(655350)
    saveoutput = open("Log_file_of_" + Host, "w")
   
    print "Saving log of_" + Host + "\n"
   
    saveoutput.write(readoutput)
    saveoutput.write("\n")
   
    saveoutput.close
    ssh_client.close
    