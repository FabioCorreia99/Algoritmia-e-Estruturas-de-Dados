# calcular o fatorial de um numero
numero =int(input("Insira um numero:"))
fatorial = 1
if numero == 0:
    print("O Fatorial de 0 é 1")
    exit()
if numero<0:
    print("Não existe fatorial de numeros negatigos")
    exit()
for numero in range(numero,0,-1):
    fatorial *= numero
print("O fatorial é %d"%fatorial)