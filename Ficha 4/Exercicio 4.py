#Valor medio de n numeros dado pelo utilizador
valor = [0]
def ValorMedio(*num):
    """
        Somar media de n numeros
    """
    soma = 0
    for i in range(len(num)):
        soma += num[i]
    return soma/len(num)

print("Media:%.2f"%ValorMedio(3,3,3))
