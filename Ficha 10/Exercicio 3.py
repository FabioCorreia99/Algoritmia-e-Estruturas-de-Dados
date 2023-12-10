#Programa para codificar e descodificar com a cifra de Cesar
import os
# se nao existir o caminho, criar
if not os.path.exists(".\\ficheiros"):
    os.mkdir("ficheiros")
#
# --encriptar texto--
def encript(texto, chave):
    """
        Recebe um texto e modifica a sua posição na tabela ASCII somando o valor da variavel chave
    """
    textEncript=""#variavel auxiliar
    for char in texto:#percorrer o texto caracter a caracter
        textEncript += chr(ord(char) + chave)#somar chave a posição ascii 
    return textEncript
#
# --decriptar texto--
def decript(textEncript, chave):
    """
        Recebe um texto e modifica a sua posição na tabela ASCII retirando o valor da variavel chave
    """
    text=""#variavel auxiliar
    for char in textEncript:#percorrer o texto caracter a caracter
        text+= chr(ord(char) - chave)#retirar chave á posição ascii 
    return text
#
#   --Guardar texto em Ficheiro--
def guardarFicheiro(textEncript):
    """
        Cria ficheiro e guarda conteudo
    """
    file = open("./ficheiros/texto.txt","w")#criar o ficheiro
    file.write(textEncript)#escrever no ficheiro
    file.close()#fechar o ficheiro
    print(textEncript)#imprimir
#
# --Ler ficheiro--
def lerFicheiro():
    """
        Lê o Ficheiro
    """
    file = open("./ficheiros/texto.txt","r")#abrir o ficheiro
    texto=file.read()#escrever no ficheiro
    file.close()#fechar o ficheiro
    return texto#retorna o texto
#



# --MENU
op=-1
while op!=0:
    os.system("cls")
    print("1 - Escrever em ficheiro")
    print("2 - Ler ficheiro")
    print("0 - Sair")
    try:
        op = int(input("\n\n\tOpção:"))
        if op <0 or op>2:   #verificar se a op é valida
            raise ValueError#erro de valor
        if op == 1:# opção 1
            os.system("cls")
            texto = str(input("\n\n\tTexto:"))#perguntar texto
            textEncript = encript(texto,3)#invocar função
            guardarFicheiro(textEncript)#invocar função
        if op == 2:# opção  2
            if not os.path.isfile("./ficheiros/texto.txt"):#perguntar se existe ficheiro
                  raise FileNotFoundError#erro de existencia
            textEncript = lerFicheiro()#invocar função
            print("Texto descodificado:%s"%decript(textEncript,3))#invocar função
            input("Prima <ENTER> para continuar...")
    except ValueError:
        print("Opção Invalida")
        input("Prima <ENTER> para continuar...")
    except FileNotFoundError:
        print("Não existe nenhum ficheiro para ler, utilize a opção -1-")
        input("Prima <ENTER> para continuar...")
    except:
        print("ERROR")
        input("Prima <ENTER> para continuar...")


# --MENU