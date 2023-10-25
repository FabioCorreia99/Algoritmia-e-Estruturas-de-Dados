#Programa para dizer se um numero é abundant

def abundant(num):
    """
    Função para calcular se um numero é abundante
    """
    soma = 0
    for i in range(1,num,1):
        if num % i == 0:
            soma += i
            if soma > num:
                return True
    return False    
        
numero = int(input("Numero:"))
if abundant(numero) ==  True:
    print("%d is an abundant number"%numero)
else:
    print("%d is NOT an abundant number"%numero)

