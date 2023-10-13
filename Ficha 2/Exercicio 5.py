# Ordenar do menor para o maior de 3 numeros

numero1= int(input("Numero 1:"))
numero2= int(input("Numero 2:"))
numero3= int(input("Numero 3:"))

if numero1 >= numero2 and numero1 >= numero3: #numero1 é o maior
    if numero2 >= numero3: # numero3 é o menor
        print(numero3,numero2,numero1)
    else: #numero 2 é o menor
        print(numero2,numero3,numero1) 
elif numero2 >= numero3: # se o numero é o maior, pergunto qual do dois é
    if numero1 >= numero3:
        print(numero3,numero1,numero2) 
    else:
        print(numero1,numero3,numero2)
else: # se nem o munero1 é o maior nem o numero2, so nos rest um
    if numero1 >= numero2:
        print(numero2,numero1,numero3)
    else:
        print(numero1,numero2,numero3)



