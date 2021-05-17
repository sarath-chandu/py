import getpass
import sys
import telnetlib

HOST = "10.10.10.21"
user = raw_input("Enter your telnet username:")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")

for n in range(2, 5):
    tn.write("no vlan " + str(n) + "\n")
    
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()