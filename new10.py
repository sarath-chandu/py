import getpass
import sys
import telnetlib

#   Get username and Password
user =  raw_input("Enter your username: ")
password = getpass.getpass()

#   Open file with list of Swtiches
f = open ("myswitches.txt")

#   Telnet to each swtich and configure it
for line in f:
    print "Getting running-config " + (line)
    Host = line.strip()
    tn = telnetlib.Telnet(Host)
    
    tn.read_until("Username: ")
    tn.write(user + "\n")
    
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
        
    tn.write("term len 0\n")
    tn.write("sh running-config\n")
    tn.write("exit\n")
    
    readoutput = tn.read_all()
    saveoutput = open("switch" + Host, "w")
    saveoutput.write(readoutput)
    saveoutput.write("\n")
    saveoutput.close
    print tn.read_all()
    