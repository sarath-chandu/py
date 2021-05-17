import getpass
import sys
import telnetlib

HOST = "172.16.16.20"
user = raw_input("Enter your telnet username:")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name Python_Vlan2\n")
tn.write("end\n")
tn.write("conf t\n")
tn.write("vlan 3\n")
tn.write("name Python_Vlan3\n")
tn.write("end\n")
tn.write("conf t\n")
tn.write("vlan 4\n")
tn.write("name Python_Vlan4\n")
tn.write("end\n")
tn.write("conf t\n")
tn.write("vlan 5\n")
tn.write("name Python_Vlan5\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()