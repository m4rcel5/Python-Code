"""
    author: m4rcel5
    19.02.2022
    portscanner
"""


import socket
import sys
from datetime import datetime as dt

target = "scanme.nmap.org" # enter the target domain or ip adress here ('scanme.nmap.org' is only an example, because its allowed to use this domain for educational purposes)
target = socket.gethostbyname(target)

tstart = dt.now()

try:    
    for port in range(1, 65536):        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((target, port))
        if res == 0:
            print(f"Opened connection in {port}")
        sock.close()
except Exception:
    print("An error occurred!")
    sys.exit()

tend = dt.now()
tres = tstart - tend
print(tres)