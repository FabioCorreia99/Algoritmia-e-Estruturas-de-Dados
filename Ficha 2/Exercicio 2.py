#classificar um triangulo pelos lados

lado1= float(input("Medida do 1 Lado:"))
lado2= float(input("Medida do 2 Lado:"))
lado3= float(input("Medida do 3 Lado:"))

if lado1 == lado2 and lado1 == lado3:
    print("O triangulo é Equilatero")
elif lado1 == lado2 or lado1 == lado3:
    print("O tringulo é isósceles")
else:
    print("O triangulo é escaleno")
