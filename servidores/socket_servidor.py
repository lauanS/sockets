import socket

MSGLEN = 13


class ServerSocket:

    def __init__(self):
        # Criando um novo socket
        self.socket = socket.socket(
            socket.AF_INET,  # AF_INET diz que familia de endereçamento o socket irá trabalhar
            # nesse caso é o IPV4
            socket.SOCK_STREAM)  # SOCK_STREAM diz que é um STREAMing socket

        # Ligando o socket em local host na porta 80
        self.socket.bind(('localhost', 80))

        # Definindo a quantidade máxima de solicitações que queremos enfileirar até o próximo accept
        # apenas para conexões TCP
        self.socket.listen(5)

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.socket.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)
