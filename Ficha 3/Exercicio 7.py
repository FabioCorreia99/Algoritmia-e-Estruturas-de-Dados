#programa para saber se um numero é primo


numero = int(input("Numero:"))
contagem = 0
if numero <= 1:
    print("Para ser primo tem que ser maior que 1")
    exit()
for i in range(1,numero+1):
    if numero % i == 0:
        contagem += 1 
if contagem == 2:
    print("\t\t%i é primo"%numero)
else:
    print("\t\t%i não é primo"%numero)
 