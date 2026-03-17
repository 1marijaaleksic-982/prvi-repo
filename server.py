import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)

print("Server je pokrenut i ceka klijenta...")
tajni_broj = random.randint(1, 10)

konekcija, adresa = server.accept()
print("Klijent se povezao!")

podaci = konekcija.recv(1024).decode()
if int(podaci) == tajni_broj:
    odgovor = f"Bravo! Pogodila si, broj je bio {tajni_broj}."
else:
    odgovor = f"Promasaj! Zamislio sam broj {tajni_broj}."

konekcija.send(odgovor.encode())
konekcija.close()
server.close() 
