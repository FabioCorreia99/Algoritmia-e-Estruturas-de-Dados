# Exercicio para reverter uma plavra inserida pelo utilizador

palavra = str(input("Insira uma frase:\n\t\t"))#frase do utilizador
for i in range(len(palavra)-1,-1,-1):#for começa no final da frase e acaba no inicio
    print(palavra[i], end="")#imprimir na posição i
