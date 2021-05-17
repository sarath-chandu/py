import getpass
import sys
import telnetlib

user = raw_input("Enter your telnet username:")
password = getpass.getpass()

for j in range(11,15):
    print "Telnet to host" + str(j)
    HOST = "10.10.10." + str(j)
    tn = telnetlib.Telnet(HOST)
    
    tn.read_until("Username: ")
    tn.write(user + "\n")
    
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    
    tn.write("conf t\n")
    
    for n in range(11,15):
        tn.write("Vlan " + str(n) + "\n" + 'name Python_' + str(n) + "\n")
    
tn.write("end\n")
tn.write("wr\n")
tn.write("exit\n")

print tn.read_all()