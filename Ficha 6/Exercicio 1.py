#aboveAverage function
numeros = []
def aboveAverage(numeros):
    """
        function that receives a list of 10 integers (numbers entered by the user) and
returns how many of these numbers are above the average.
    """
    cont = 0
    media =float(sum(numeros)/10)
    for i in range(len(numeros)):
    # for number in numbers
        if numeros[i] > media:
            cont += 1
    return cont
numeros = []
for i in range(10):
    try:
        numeros.append(int(input("Numero:")))
    except ValueError: 
        print("Erro:Não é um numero")
        i -= 1
        print(i)
    except:
        print("erro")
print("A lista tem %d numeros acima da media"%aboveAverage(numeros))