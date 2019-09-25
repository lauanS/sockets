import socket
import base64


def encode_64():
    input = open('/home/lauans/law/gitRep/sockets/img_sockets.jpeg', 'rb')
    output = open('/home/lauans/law/gitRep/sockets/txt_img.txt', 'wb')

    base64.encode(input, output)

    input.close()
    output.close()

    with open('/home/lauans/law/gitRep/sockets/txt_img.txt', 'rb') as file:
        base64_str = file.read()

    return base64_str


msg = b'{ "type":"write", "file":"new_file.jpeg", "msg":"'
msg += encode_64()
msg += b'"}'

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
