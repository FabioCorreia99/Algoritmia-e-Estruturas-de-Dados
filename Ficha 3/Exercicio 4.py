# Programa de tentar advinhar um numero
import random #Importar a biblioteca para nos dar um numero aleatorio
tentativa = 1
num = random.randint(1,50)#gerar o numero aleatorio
palpite = int(input("Indique o seu palpite:"))#primeiro palpite para entar no loop
while palpite != num:
    if tentativa == 10:#quando atingir as 10 tentativas perdeu o jogo
        print("Esgotou as suas tentativas\n")
        exit()
    if palpite < num:#dizer que o numero que inseriu é menor
        print("O numero a advinhar é MAIOR")
    
    if palpite > num:#dizer que o numero que inseriu é maior
        print("O numero a advinhar é Menor")
    palpite = int(input("Indique o seu palpite:"))#perguntar no final do loop para passar primeiro pelos ifs todos
    tentativa += 1
print("Parabéns!!! Acertou em %i tentativas"%tentativa)