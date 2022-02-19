"""
    @author: Marcel Lizak
    19.02.2022
    scanning for open ports
"""


import socket
import sys
from datetime import datetime as dt

target = "scanme.nmap.org"
target = socket.gethostbyname(target)

tstart = dt.now()

try:    
    for port in range(1, 65536):        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((target, port))
        if res == 0:
            print(f"Offene Verbindung in Port {port}")
        sock.close()        
except Exception:
    print("Ein Fehler ist aufgetreten")
    sys.exit()

tend = dt.now()
tres = tstart - tend
print(tres)