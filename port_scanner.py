import socket
import sys
import ipaddress
from datetime import datetime

##### Define target
from pip._vendor.distlib.compat import raw_input

host = raw_input("Enter Host IP: ")

##### Validate IP address
ip = ipaddress.ip_address(host)
target = socket.gethostname()

##### start scan

print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))

try:

    #### Scan ports between 1 to 65,535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator
        result = s.connect_ex((host, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\n Server not responding !!!!")
    sys.exit()
