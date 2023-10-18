# Transformar um numero em base numerico em base binaria

numero = int(input("Numero:"))# perguntar numero
resultado= str(" ")# variavel string para guardar o binario
if numero == 0: # if para eliminar a opção 0
    print("0000")
while numero != 1: # loop para percurrer o metodo ate 1 
    if numero % 2 == 0:#se o resto é zero então acrescentar um 0
        numero =int(numero/2)
        resultado =  "0" + resultado
    else:
        numero = int(numero/2)#se o resto não é zero então acrescentar um 1
        resultado =  "1" + resultado
resultado = str(numero) + resultado #acrescentar 1 final 

print(resultado.rjust(5,"0"))

