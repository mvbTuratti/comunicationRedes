#!/usr/bin/env python3

from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
from BinarioCrip import criptografia
from hdb3 import hdb
import matplotlib.pyplot as plt

PORT_NUMBER = 5004
SIZE = 1024

hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
    (data,addr) = mySocket.recvfrom(SIZE)

    msgdec1 = criptografia(str(data))
    binario = ' '.join(format(ord(x), 'b') for x in str(data))
    hd = hdb(binario)
    print("\nMensagem recebida:\n{0}\n\nMensagem binaria:\n{1}\n\nMensagem decodificada:\n{2}\n\nMensagem original:\n{3}".format(hd,binario,data,msgdec1))
    plt.step(range(1, len(hd)+1), hd)
    plt.show()


sys.exit()
