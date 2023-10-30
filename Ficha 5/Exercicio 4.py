#removeSpaces function

def removeSpaces(frase):
    """
        Remove os espaços a mais
    """
    while frase.find("  ")!= -1:# executa enquanto tiver dois espaços seguidos
        frase = frase.replace("  "," ")#replace nos espaços
    print(frase)



frase = str(input("Insira a frase:\n\n\t\t"))
removeSpaces(frase)