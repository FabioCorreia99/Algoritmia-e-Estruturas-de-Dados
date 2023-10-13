#Calcular o peso ideal de uma pessoa

genero = input("Género(M/F):")
altura = int(input("Altura(cm):"))

match genero.upper(): #lower
    case "F":
        print("Peso ideal:%.2f Kg" %((altura - 100) - (altura - 150)/2))
    case "M":
        print("Peso ideal:%.2f Kg" %((altura - 100) - (altura - 150)/4))