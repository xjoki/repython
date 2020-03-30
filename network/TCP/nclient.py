# nclient
import socket

# Erzeugen einer Socket Instanz
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP
ip = "127.0.0.1"        # IP Adresse
s.connect((ip, 49200))

try:
    while True:
        message = "zu uebermittelnder Nachrichtentext"
        # Nachricht versenden
        s.send(message.encode())  
        antwort = s.recv(1024)
        print("{} - {}".format(ip, antwort.decode()))
finally:
    s.close()
