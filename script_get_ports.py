#!/bin/python3

import socket
import sys

rHost = input("Type the ip target: ")
rHostIP = socket.gethostbyname(rHost)
rPorts = [22,53,80,111,138,443,32768]

print("_" * 50)
print("\nScanning... " + str(rHostIP))
print("_" * 50)

try:
    for ports in rPorts:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)
        
        result = s.connect_ex((rHostIP,ports))
        
        if result == 0:
            print("port {} open".format(ports))
        else:
            print("port {} closed".format(ports))

        s.close()
except KeyboardInterrupt:
    print("Closed by user...Keyboard Interruption")
    sys.exit()