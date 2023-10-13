#Calcular MHR

genero = input("Género(M/F):")
if genero.upper()!= "F" and genero.upper() != "M":
    print("Genero nao identificado")
    exit()
idade = int(input("Idade:"))

if genero.upper() == "F":
        print("MHR = %i"%(226 - idade))
else:
        print("MHR = %i"%(220 - idade))



