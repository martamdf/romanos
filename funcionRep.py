
lista = ('M','C','M', 'M', 'V','V')
tipo1= ('M','C','X','I')
tipo5= ('V', 'L', 'D')

def validaRep (lista): 
    if len(lista)> 1:
        for i in range(len(lista)-1):
            if lista[i] in tipo5:
                if lista[i] == lista[i+1]:
                    return False
        if len(lista) > 3:
            for i in range(len(lista)-3):
                if lista[i] in tipo1:
                    if lista[i] == lista[i+1] and lista[i] == lista[i+2] and lista[i] == lista[i+3]:
                        return False   
        return True
    else:
        return True

print(validaRep(lista))
