
def hdb(valor):

    contador = 0
    zeros = 0
    code = []
    posouneg = True
    numero = 0
    for bit in valor:
        if bit == '1':
            if posouneg:
                posouneg = False
                code.append(1)
                contador +=1
            else:
                posouneg = True
                code.append(-1)
                contador+=1
            zeros = 0
        elif bit == '0':
            if zeros == 3:
                if contador %2 == 0:
                    if posouneg:
                        code[-3] = 1
                        code.append(1)
                        contador += 2
                        posouneg = False
                    else:
                        code[-3] = -1
                        code.append(-1)
                        contador +=2
                        posouneg = True
                else:
                    if posouneg:
                        code.append(-1)
                        contador +=1
                    else:
                        code.append(1)
                        contador +=1
                zeros = 0
            else:
                code.append(0)
                zeros +=1
    
    return code
