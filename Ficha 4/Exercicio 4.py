#Valor medio de n numeros dado pelo utilizador
valor = [0]
def ValorMedio(*num):
    soma = 0
    for i in range(len(num)):
        soma += num[i]
    return soma/len(num)


media = ValorMedio(3,3,3)
print("Media:%.2f"%media)
