import sys
import socket
from datetime import datetime

#Create an input for user to input target IP address
target = input(str("Target IP: "))

#Create a banner for the scanner
print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

#Detect all open ports on server
try:
    #Scan every port on the target ip
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open ports
        result = s.connect_ex((target,port))
        if result == 0:
            print("[*] Port {} is open".format(port))
            s.close()

except KeyboardInterrupt:
        print("\n Exiting :")
        sys.exit()

except socket.error:
        print ("\ Host not responding :")
        sys.exit()


