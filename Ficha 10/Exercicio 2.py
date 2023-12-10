#lerTexto()
import os


def lerTexto():
    if os.path.isfile(".\\ficheiros\\dados.bin"):
        f = open(".\\ficheiros\\dados.bin","rb")    
        texto = f.read()
        f.close
        return str(texto)
    else:
        print("Ficheiro não existe")

print(lerTexto())