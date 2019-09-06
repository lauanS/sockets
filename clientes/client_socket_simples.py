import socket

# criando o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectando ao servidor local na porta 80
# Onde nosso socket servidor estará escutando
client_socket.connect(("localhost", 80))

msg = b'Hello world'
totalsent = 0
while totalsent < len(msg):
    sent = client_socket.send(msg[totalsent:])
    if sent == 0:
        raise RuntimeError("socket connection broken")
    totalsent = totalsent + sent
