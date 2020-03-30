# nserver

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # IPv4 UDP
try:
    # wird beim bind keine IP-Adresse angegeben, dann kann über alle dem Server
    # zugeordneten Adressen empfangen werden
    s.bind(("", 49200)) # Port 49200
    # wichtig: Adressobjekt = Tupel mit den 2 Elementen (str_IP_Adresse, int_Portnummer)
    while True:         # abhören
        daten, addr = s.recvfrom(1024)  # max. Paketgröße 1KB
        print("{} - {}".format(addr[0], daten.decode()))
finally:
    s.close()
