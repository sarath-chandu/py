import paramiko
import time
import getpass

ip_address = "10.10.10.22"
user = raw_input("Enter your telnet username:")
password = getpass.getpass()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=user,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell ()

remote_connection.send("conf t\n")
remote_connection.send("no int loop 1\n")
remote_connection.send("end\n")
remote_connection.send("conf t\n")
remote_connection.send("no int loop 2\n")
remote_connection.send("end\n")
remote_connection.send("conf t\n")
remote_connection.send("no router ospf 1\n")
remote_connection.send("no network 0.0.0.0 255.255.255.255 area 0\n")
remote_connection.send("end\n")

remote_connection.send("conf t\n")

for n in range(2,5):
    print "removing Vlan " + str(n)
    remote_connection.send("no vlan " + str(n) + "\n")

remote_connection.send("end\n")
remote_connection.send("exit\n")

time.sleep(10)
output = remote_connection.recv(65535)
print output

ssh_client.close



