#printCharLine function

def printCharLine(frase,numero):
    inicio = 0
    fim = int(numero)
    while fim < len(frase):
        print(frase[inicio:fim])
        inicio=fim
        fim+= int(numero)
    print(frase[fim:])
    


frase = str(input("Insira a frase:\n\n\t\t"))
numero = input("Numero de caracteres a imprimir:")
printCharLine(frase,numero)