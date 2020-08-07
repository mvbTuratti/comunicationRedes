from socket import socket, AF_INET, SOCK_DGRAM
import sys
from BinarioCrip import criptografia
import matplotlib.pyplot as plt
from hdb3 import hdb


PORT_NUMBER = 5004
SIZE = 1024
SERVER_IP = input("Digite o servidor que deseja conectar:\n")
while True:
    mensagem = input("Digite sua mensagem:\n")
    msgcod1 = criptografia(mensagem)
    binary = ' '.join(format(ord(x), 'b') for x in msgcod1)
    hd = hdb(binary)
    mySocket = socket(AF_INET, SOCK_DGRAM)
    mySocket.sendto(msgcod1.encode('utf-8'),(SERVER_IP,PORT_NUMBER))
    print("\nMensagem original:\n{}\n\nMensagem com encriptografia num 1:\n{}\n\nMensagem binaria simples:\n{}\n\nMensagem hdb3 codificada:\n{}".format(mensagem,msgcod1,binary,hd))
    plt.step(range(1, len(hd)+1), hd)
    plt.show()
