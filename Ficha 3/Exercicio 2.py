# Programa para adicionar numeros e dar o maior e a média mas o cliente é que introduz a quantidade de numeros que pretende
import math
maior = -math.inf #inicializar a variavel com o menor numero possivel
media = 0
escolha = int(input("Quantos numeros deseja ler?\n"))# numero de repetições
for i in range(escolha):
    numero = int(input("Insira um numero:"))
    if numero > maior: # if para indicar o numero maior
        maior = numero
    media += numero # somar as opções para fazer a media 
print("Maior:%i"%maior)
print("Media:%.2f"%(float(media/escolha)))