#standardName function

def standardName(name):
    """
        Retorna so O Primeiro e Ultimo nome e o resto adverbiado
    """
    listName = name.split(" ")#separa os nomes
    for i in range(0,len(listName)):
        if i == 0:#imprime o primero nome
            print(listName[i], end=" ")
        elif i == (len(listName)-1):#imprime o ultimo e termina
            print(listName[i], end=" ")
            exit()
        else:#imprime so a primeira letra e acrescenta um ponto
            print(listName[i][0]+".", end=" ")
name = str(input("Insira a frase:\n\n\t\t"))
print(standardName(name))
