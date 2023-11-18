#searchNumber(list, searchValue) 

def searchNumber(list, searchValue):
    """
        return the positions where the search value is found, in the list
    """
    numero = ""
    for i in range(len(list)):
        if list[i] == searchValue:
            numero = numero + " " + str(i)
    return numero
i=0
list=[]
while i <10:
    try:
        list.append(int(input("Numero:")))  
        i+=1
    except ValueError:
        print("Erro,tem que inserir um numero")
    except:
        print("Erro")

try:
        n =(int(input("Numero a procurar:")))  
except ValueError:
        print("Erro,tem que inserir um numero")
except:
    print("Erro")

if searchNumber(list,n) == "":
    print("Não parece na lista")
else:
    print("Aparece nas posições:%s"%searchNumber(list,n))