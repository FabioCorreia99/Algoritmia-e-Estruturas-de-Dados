# programa para dar o segundo maior numero 
import math
maior = -math.inf
segMaior = -math.inf
op = int(input("Quantidade de numeros a inserir:"))
while op <2:
    print("Opção invalida, tem que ser maior que 2")
    op = int(input("Quantidade de numeros a inserir:"))
for i in range(op):
    numero = float(input("Nº:"))
    if numero > segMaior:
        if numero > maior:
            segMaior = maior
            maior = numero
        else:
            segMaior = numero
print("%.2f é o segundo maior"%segMaior)
        
