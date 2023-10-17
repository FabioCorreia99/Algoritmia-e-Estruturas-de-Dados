# Programa para adicionar 10 numeros e dar o maior e a média
import math
maior = -math.inf #inicializar a variavel com o menor numero possivel
media = 0
for i in range(10):
    numero = int(input("Insira um numero:"))
    if numero > maior:
        maior = numero
    media += numero
print("Maior:%i"%maior)
print("Media:%.2f"%(float(media/10)))

