# nclient
import socket

# Erzeugen einer Socket Instanz
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "127.0.0.1"        # IP Adresse des Servers
message = "zu uebermittelnder Nachrichtentext"

# Nachricht versenden
s.sendto(message.encode(), (ip, 49200))  # Port 49200
s.close()
