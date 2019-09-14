import socket
from threading import Thread

import json
import time

def process(connection):
    msg = b''
    read_bytes = connection.recv(4096)
    count = 1
    # Lendo todos os bytes da recebidos
    while read_bytes:
        # print('lendo[{}]...'.format(count))
        msg += read_bytes
        read_bytes = connection.recv(4096)
        count += 1
    print('{} bytes lidos'.format(len(msg)))
    print('msg lida: {}'.format(msg[-50:]))
    # Finalizando a conexão
    msg = msg.decode('utf-8')
    print(msg[-50:])
    operation, file_name, msg = json_to_vars(msg);
    if operation == 'read':
        read_file(file_name, connection)
    if operation == 'write':
        write_file(file_name, msg)
    connection.close()

def json_to_vars(json_bits):
    dict_msg = json.loads(json_bits)
    return dict_msg['type'], dict_msg['file'], dict_msg['msg']



def read_file(file_name, connection):
    with open(file_name, 'rb') as file:
        msg = file.read()
    total_sent = 0
    while total_sent < len(msg):
        sent = connection.send(msg[total_sent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        total_sent = total_sent + sent

def write_file(file_name, msg):
    # Salvando o arquivo
    with open(file_name, 'w') as file:
        file.write(msg)

if __name__ == '__main__':
    # Criando um novo socket
    server_socket = socket.socket(
        socket.AF_INET,  # AF_INET diz que familia de endereçamento o socket irá trabalhar
        # nesse caso é o IPV4
        socket.SOCK_STREAM)  # SOCK_STREAM diz que é um STREAMing socket

    # Ligando o socket em local host na porta 2077
    server_socket.bind(('localhost', 2077))

    # Definindo a quantidade máxima de solicitações que queremos enfileirar até o próximo accept
    # apenas para conexões TCP
    server_socket.listen(5)
    print('Iniciando conexão')

    while True:
        # Aceita conexões da rede, retornando uma tupla com a conexão realizada
        (connection, address) = server_socket.accept()
        print('Conectado com {}'.format(address))
        # Criando a Thread que irá executar a função process()
        new_thread = Thread(target=process, args=[connection])
        new_thread.start()
