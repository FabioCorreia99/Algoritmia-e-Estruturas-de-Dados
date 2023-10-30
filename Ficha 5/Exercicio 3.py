#capicua function

def capicuafunction(frase):
    """
        Retorna True se a palavra for capicua
    """
    capicua = ""#iniciar a variavel
    for i in range(len(frase)-1,-1,-1):#for para percorrer a variavel de tras para a frente e passa para a variavel capicua
        capicua += frase[i]
    if capicua == frase:#se for igual retorna True
        return True
    else:
        return False
    
frase = input("Insira uma Palavra:\n\t\t")
if capicuafunction(frase.lower) == True:#se for true é porque é capicua
    print("A palavra é uma capicua")
else:
    print("A palavra NÃO é uma capicua")
