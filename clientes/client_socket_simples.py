import socket

# criando o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectando ao servidor local na porta 2077
# Onde nosso socket servidor estará escutando
client_socket.connect(("localhost", 2077))

msg = b'{ "type":"write", "file":"new_file.txt", "msg":"'
msg += b'Quando eu me encontrava na'
msg += b'"}'
file_name = b'teste.txt'

totalsent = 0
while totalsent < len(msg):
    sent = client_socket.send(msg[totalsent:])
    if sent == 0:
        raise RuntimeError("socket connection broken")
    totalsent = totalsent + sent
