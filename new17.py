import paramiko
import time
import getpass

#   Get username and Password
user =  raw_input("Enter your username: ")
password = getpass.getpass()

#   Open file with list of Swtiches
f = open ("myswitches.txt")

for line in f:
    
  try:
    Host = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=Host,username=user,password=password)
    
    remote_connection = ssh_client.invoke_shell ()
    
    remote_connection.send("exit\n")
  except:
    remote_connection =  ("Authentication failed") 
    remote_connection =  ("in connect passphrase")
    remote_connection =  ("in _authraise saved_exception")
    remote_connection =  ("paramiko.ssh_exception.AuthenticationException: Authentication failed")
        
    result = remote_connection
    
    if result == "socket.error":
        print Host, " Not Accessible"
    else:
        print Host, "Accessible"
        
raw_input("Connectivity check done, press Enter to Exit: ")
