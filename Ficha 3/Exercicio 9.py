# Programa para descubrir numeros perfeitos
div = 0
num = int(input("Numero:"))
for i in range(num-1,0,-1):# loop para percurer do numero até zero para descubrir os divisiveis e soma los
    if num % i == 0: # pergunta se é divisivel
        div += i # se sim soma á variavel para depois comparar
if num == div:# pergunta se é um num perfeito
    print("%i é um numero Perfeito"%num)
else:
    print("%i não é um numero Perfeito"%num)
