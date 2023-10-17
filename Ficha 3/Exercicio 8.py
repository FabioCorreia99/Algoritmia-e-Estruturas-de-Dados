 # Programa para dar n termos da sequência de fibonacci

termo = int(input("\t\tNº de termos a imprimir:"))
num = int(1)
antNum1 = int(1)
antNum2 = int(0)
if termo == 1:  # 1º termo
    print("0")
    exit()
elif termo == 2:# 2º Termo
    print("0 1")
    exit()
else:
    print("0 1", end=" ") 
for i in range(2,termo):
    print("%i"%num, end=" ")
    antNum2 , antNum1 = antNum1 , num #actualizar as variaveis
    num = antNum1 + antNum2 # somar os dois numeros anteriores
    


