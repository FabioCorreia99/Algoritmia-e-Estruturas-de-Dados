# reverseWords

def  reverseWords(frase):
    """
        Retorna a frase ao contrario
    """
    listFrase = frase.split(" ")#divide a frase
    for i in range(len(listFrase)-1,-1,-1):#comeca no final e percorre ate ao inicio
        print(listFrase[i], end=" ")#print da palavra na posição i

frase = str(input("Insira uma frase:"))
reverseWords(frase)