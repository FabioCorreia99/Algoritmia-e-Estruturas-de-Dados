#GenerateNumbers
import random

def generateNumbers(lowerLimit, upperLimit, numbers):
    """
        Função para gerar o meuro milhoes
    """
    number=[]
    i = 0
    while i < numbers:
        n=(random.randint(lowerLimit,upperLimit))#numero aleatorio
        if n not in number:#nao queremos numeros repetidos
            number.append(n)#se nao tiver add na lista
            i+=1
    number.sort()
    return number
opcao="S"
while opcao.upper() == "S":#enquanto o utilizador por S
    print("Chave do Euromilhões:",generateNumbers(1,50, 5)) # generates 5 numbers between 1 and 50
    print("Estrelas:",generateNumbers(1,12,2)) # generates 2 numbers between 1 and 12 (stars)
    try:
        opcao = input("Deseja gerar nova chave?(S/N)")#pergunta se quer fazer de novo
        if opcao.upper() != "S" and opcao.upper() != "N":
            raise ValueError
    except ValueError:
        print("Erro ---> S ou N")
    except:
        print("Erro")
        break