#generatePassword function
import random

def generatePassword(nome):
    """
        Gera uma password atravez de um nome
    """
    password = ""
    for i in range(1,len(nome)):#percorre o nome 
        ale = random.randint(1,9)#criar um valor aleatorio
        if i % 2 != 0:# nas posições pares
            if i == len(nome)-1:#confirmar se é o final
                password = password + nome[i]
                password = password + str(ale)
            else:
                password = password + nome[i]
        else:
            password = password +str(ale)
    password = password + str(len(nome))
    return password

nome = str(input("Nome:"))
if nome.find(" ") != -1:
    print("Nome Invalido")
else:
    print("Password:%s"%generatePassword(nome))

