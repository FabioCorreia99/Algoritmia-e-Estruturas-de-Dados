import random


def imprimePais(pais,tentativas):
    """
        Funçao de imprimir dicas do jogo
    """
    match tentativas:
        case 0:#tentativa 1
            print(pais[0],end=" ")#imprime 1 caracter
            for i in range(1,len(pais)):
                print("-", end=" ")#preenche o resto da palavra com -
        case 1:#tentativa 2
            print(pais[0:2],end=" ")#imprime 2 caracter
            for i in range(2,len(pais)):
                print("-", end=" ")#preenche o resto da palavra com -
        case 2:#tentativa 3
            print(pais[0:3],end=" ")#imprime 3 caracter
            for i in range(3,len(pais)):
                print("-", end=" ")#preenche o resto da palavra com -
    print("\n")



ficheiro = open("./ficheiros/paises.txt","r", encoding="utf-8")#abre o ficheiro
texto = ficheiro.readlines()#le as linhas em uma lista
ficheiro.close()#fecha o ficheiro
pais = texto[random.randint(0,len(texto)-1)]#escolher uma linha(pais) aleatoria
pais = pais[:len(pais)-1]#tirar o \n
print("\t\t Adivinhe o nome do país")#Titulo
print("\n\n")
for i in range(3):# 3 Tentativas
    escolha = str(input("Qual o país:"))# input do utilizador
    if escolha.lower() == pais.lower():#pergunta se o input é igual ao pais
        print("ACERTOU!!!!!!!!")
        exit()#acaba o programa
    else:
        imprimePais(pais,i)#invoca a função
print("NÃO ACERTOU!!!!!!!")#se chegou aqui é porque falhou as 3 tentativas