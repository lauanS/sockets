import socket
import base64

msg = b'{"type":"read", "file":"test_read.txt", "msg":"Sample"}'

# criando o socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectando ao servidor local na porta 2077
# Onde nosso socket servidor estará escutando
client_socket.connect(("localhost", 2077))

file_name = b'teste.txt'

totalsent = 0
while totalsent < len(msg):
    sent = client_socket.send(msg[totalsent:])
    if sent == 0:
        raise RuntimeError("socket connection broken")
    totalsent = totalsent + sent

# Avisa para o servidor que terminei de enviar os dados
# porém ele deve manter a conexão aberta
client_socket.shutdown(1)
msg = b''
read_bytes = client_socket.recv(4096)

while read_bytes:
    msg += read_bytes
    read_bytes = client_socket.recv(4096)

print("bytes lidos:")
print(read_bytes)

client_socket.close()
