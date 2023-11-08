#a program that reads the scores of 10 participants in a programming contest (the scores must be validated between 0 and 20, using a try-except structure).

def positiveList(listPont):
    """
        Returns only positive numbers
    """
    j = 0
    for i in range(len(listPont)):#forpara percorrer a lista
        if listPont[j] < 10:#se for negativa
            del listPont[j]#apaga
            i-=1#o index vai reduzir por isso temos que actualizar a var
        else:
            j+=1#var para auxiliar
    return listPont

pontua=[]
for i in range(10):
    try:
        n = int(input("Pontuação:"))
        if n <= 0 and n>= 20:
           raise ValueError
        else:
            pontua.append(n)
    except ValueError:
        print("Tem que ser entre 0 e 20")
        i -= 1
    except:
        print("Erro")
print(positiveList(pontua))