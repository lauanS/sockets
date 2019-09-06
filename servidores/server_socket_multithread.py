import socket
from threading import Thread
import time

def process(connection):
    msg = b''
    read_bytes = connection.recv(4096)
    count = 1
    # Lendo todos os bytes da recebidos
    while read_bytes:
        print('lendo[{}]...'.format(count))
        msg += read_bytes
        read_bytes = connection.recv(4096)
        count += 1
    print('{} bytes lidos'.format(len(msg)))
    print('msg lida: {}'.format(msg))
    # Finalizando a conexão
    connection.close()

if __name__ == '__main__':
    # Criando um novo socket
    server_socket = socket.socket(
        socket.AF_INET,  # AF_INET diz que familia de endereçamento o socket irá trabalhar
        # nesse caso é o IPV4
        socket.SOCK_STREAM)  # SOCK_STREAM diz que é um STREAMing socket

    # Ligando o socket em local host na porta 80
    server_socket.bind(('localhost', 80))

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
