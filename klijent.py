import socket

klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
klijent.connect(('localhost', 12345))

moj_broj = input("Pogodi broj koji je server zamislio (1-10): ")
klijent.send(moj_broj.encode())

odgovor = klijent.recv(1024).decode()
print("ODGOVOR SERVERA:", odgovor)

klijent.close() 
