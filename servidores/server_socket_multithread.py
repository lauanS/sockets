import socket
from threading import Thread

import base64
import re
import time

def get_msg(msg):
    # Decodificando a msg em UTF-8
    re_msg = msg.decode('utf-8')

    # Obtendo o tipo da operação e o nome do arquivo
    type = re.search(r'"type":"(.+?)", "file', re_msg)
    file = re.search(r'"file":"(.+?)", "msg', re_msg)

    return type.group(1), file.group(1)


def proces(connection):
    read_file('test_read.txt', connection)
def process(connection):
    msg = b''
    read_bytes = connection.recv(4096)

    # Lendo todos os bytes da recebidos
    while read_bytes:
        msg += read_bytes
        read_bytes = connection.recv(4096)
    print('{} bytes lidos'.format(len(msg)))
    print('msg lida: {} [...] {}'.format(msg[:60], msg[-10:]))

    # Lendo o JSON
    operation, file_name = get_msg(msg)

    # Obtendo as informações da mensagem recebida
    start_msq = 30 + len(operation) + len(file_name)
    arq = msg[start_msq:-2]

    # Definindo qual operação será executada
    if operation == 'read':
        read_file(file_name, connection)
    if operation == 'write':
        write_file(file_name, arq)

    # Finalizando a conexão
    connection.close()


def read_file(file_name, connection):
    # Lendo o arquivo solicitado
    with open(file_name, 'rb') as file:
        msg = file.read()
    total_sent = 0

    # Enviando o arquivo
    while total_sent < len(msg):
        sent = connection.send(msg[total_sent:])
        if sent == 0:
            raise RuntimeError("Erro de conexão com o socket")
        total_sent = total_sent + sent

def write_file(file_name, msg):
    # Salvando o arquivo
    with open('temp_file.txt', 'wb') as file:
        file.write(msg)

    with open('temp_file.txt', 'rb') as file:
        with open(file_name, 'wb') as file_output:
            base64.decode(file, file_output)


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
