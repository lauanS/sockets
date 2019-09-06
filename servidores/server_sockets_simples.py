import socket

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
    # aceita conexões da rede, retornando uma tupla com a conexão realizada
    (client_socket, address) = server_socket.accept()
    print('Conectado')
