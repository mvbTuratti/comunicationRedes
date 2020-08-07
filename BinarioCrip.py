#!/usr/bin/python
# -*- coding: utf-8 -*-
def criptografia(crip):
    tam = len(crip)
    aux_string = []
    for i in range(tam):
        aux = crip[i]
        if crip[i] == "a":
            aux = "7"
        elif crip[i] == "e":
            aux = "3"
        elif crip[i] == "i":
            aux = "2"
        elif crip[i] == "o":
            aux = "8"
        elif crip[i] == "u":
            aux = "9"
        elif crip[i] == "c":
            aux = "1"
        elif crip[i] == "s":
            aux = "0"
        elif crip[i] == "r":
            aux = "4"
        elif crip[i] == "A":
            aux = "*"
        elif crip[i] == "7":
            aux = "a"
        elif crip[i] == "3":
            aux = "e"
        elif crip[i] == "2":
            aux = "i"
        elif crip[i] == "8":
            aux = "o"
        elif crip[i] == "9":
            aux = "u"
        elif crip[i] == "1":
            aux = "c"
        elif crip[i] == "0":
            aux = "s"
        elif crip[i] == "4":
            aux = "r"            
        elif crip[i] == "*":
            aux = "A"
        aux_string.append(aux)

    return "".join(aux_string)

