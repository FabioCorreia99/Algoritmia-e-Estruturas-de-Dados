#countWord function

def countWord(texto,palavra):
    """
        Função para contar qunatos vezes a palavra aparece no texto
    """
    while texto.find(",")!= -1 and texto.find(".")!= -1:#subestituir . e , para espaços para dividir sem problemas
        texto = texto.replace("."," ")
        texto = texto.replace(","," ")
    listTexto = texto.split(" ")#dividir a frase
    count = 0 
    pos = ""
    aux= -1
    for i in range(len(listTexto)):#percurrer a string para encontrar a palavra igual 
        if listTexto[i] == palavra:
            pos = pos + " " + str(texto.find(palavra,aux+1)+1)#guarda a possição
            aux = texto.find(palavra,aux+1)#variavel para no auxiliar para guardar a posição correta
            count += 1#vezes que a palavra aparece
    return count, pos

texto = str(input("Insira a frase:\n\n\t\t"))
palavra = str(input("Palavra:"))
count, pos = countWord(texto,palavra)
print("A palavra %s parece %s nas posições %s"%(palavra,count,pos))
