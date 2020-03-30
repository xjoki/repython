# nserver

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # IPv4 TCP
try:
    s.bind(("", 49200))
    s.listen(1)

    while True:
        komm, addr = s.accept()
        while True:
            data = komm.recv(1024)
            if not data:
                komm.close()
                break
            print("{} - {}".format(addr[0], data.decode()))
            nachricht = input("Antwort: ")
            komm.send(nachricht.encode())
finally:
    s.close()