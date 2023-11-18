#Given a list of N elements (N must be requested from the user), create a function that orders the list and allows you to generate another list without duplicate values


def Sort_and_EliminateDupli(list):
    order=[]
    for i in range(len(list)):
        if list[i] not in order:
            order.append(list[i])
    order.sort()
    return order
list=[]
i =0
try:
    n = int(input("Insira a quantidade da Lista:"))
except ValueError:
    print("ERRO Insira um Numero ERRO")
except:
    print("Error")

while i < n:
    try:
        numero = input("Numero:") 
        list.append(numero)
        i+=1
    except ValueError:
        print("Erro, insira um numero")
    except:
        print("ERROR")
print(Sort_and_EliminateDupli(list))
