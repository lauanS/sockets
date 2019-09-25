## Programação de sockets TCP em Python e Java.

##### Atividade proposta:
Desenvolva um servidor usando a tecnologia Socket que seja capaz de:

 - Receber um arquivo de dados e armazená-lo em disco

 - Retornar o arquivo gravado anteriormente para um cliente requisitante

Faça um simples menu para as duas opções acima (enviar e receber arquivo)

O servidor deverá ser concorrente e usar TCP

Servidor deverá ser capaz de receber vários arquivos ao mesmo tempo, ou seja, deverá ser Multithread. 
Para isso, use a classe Thread ou similar da linguagem de programação que for utilizar para implementar o servidor

Desenvolva também um cliente que invoque o servidor para enviar e receber o arquivo.

Para testar o Multithreading do servidor, execute várias instâncias do cliente 
ao mesmo tempo ou use threads também do lado do cliente.

> O cliente deverá ser desenvolvidona linguagem A e o servidor na linguagem B, sendo A ≠ B.
> A escolha da linguagem de programação a ser usada fica a critério da dupla

##### Comunicação

O cliente manda uma mensagem em JSON com o seguinte formato:

```JSON
  {"type":"write", "file":"new_file.jpeg", "msg":"Sample"}
```
