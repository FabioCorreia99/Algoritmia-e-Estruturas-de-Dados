#escreveTexto(texto)
import os

def escreveTexto(texto):
    texto=bytes(texto, encoding="utf-8")#tranformar em binario
    if not os.path.isfile(".\\ficheiros\\dados.bin"):#perguntar se o file existe
        os.mkdir("ficheiros")#criar o caminho
        f = open(".\\ficheiros\\dados.bin","xb")#criar o file
        f.write(texto)#escrever no file
        ficheiro =os.getcwd()
        print(ficheiro)
        f.close

#try
texto = str(input("Texto:"))
escreveTexto(texto)
