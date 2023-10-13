# calcular o peso em diferentes planetas

peso = float(input("Insira o seu peso(KG):"))

planeta = str(input("Escolha o Planeta:\nMercurio\nVenus\nMarte\nJupiter\nSaturno\nUrano\n\n"))

match planeta.upper():
    case "MERCURIO":
        print("Peso em %s é %.2f" %(planeta,peso*0.37))
    case "VENUS":
        print("Peso em %s é %.2f" %(planeta,peso*0.88))
    case "MARTE":
        print("Peso em %s é %.2f" %(planeta,peso*0.38))
    case "JUPITER":
        print("Peso em %s é %.2f" %(planeta,peso*2.64))
    case "SATURNO":
        print("Peso em %s é %.2f" %(planeta,peso*1.15))
    case "Urano":
        print("Peso em %s é %.2f" %(planeta,peso*1.17))
    case _:
        print("Planeta não Identificado")