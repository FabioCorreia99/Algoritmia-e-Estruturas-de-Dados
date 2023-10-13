#converte polegadas em mm e cm
polegadas = int(input("Indica um numero em polegadas:"))

milimetros = polegadas*25.4

print("O valor em Mm é: %.2f" %milimetros)
print("O valor em Cm é: %.2f" %(milimetros/10))