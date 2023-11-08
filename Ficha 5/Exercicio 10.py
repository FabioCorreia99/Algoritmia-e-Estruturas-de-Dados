#printCharLine function

def printCharLine(frase,numero):
    inicio = 0
    fim = int(numero)
    while fim <= len(frase):#enquanto o ultimo caracter for menor que o tamanho da frase
        print(frase[inicio:fim])#print nas possições    
        inicio=fim#actualiza a variavel
        fim+= int(numero)#soma o numero ao fim
    print(frase[inicio:])
    


frase = str(input("Insira a frase:\n\n\t\t"))
numero = input("Numero de caracteres a imprimir:")
printCharLine(frase,numero)