# programa para dizer o numero de caracteres, vogais e espaços numa frase

frase = str(input("Insira uma frase:\n\t\t"))

print("Nº de Caracteres: %d"%len(frase))#contar os caracteres
print("Nº de Espaços:%d"%frase.count(" ")) # contar os espaços
print("nº de Vogais:%d"%(frase.count("a")+frase.count("e")+frase.count("i")+frase.count("o")+frase.count("u")))# contar as vogais