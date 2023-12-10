import random

def inicializar(n):
    matriz=[]
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(random.randint(10,100))
            print(matriz[i][j])
    return matriz

def tranposta(*matriz,n):
    for i in range(n):
        print("\n")
        for j in range(n):
            print(matriz[j][i], end=" ")

matriz=[]
op=-1
while op != 0:
    print("\n\n\n\n\n")
    print("1 - Inicializar matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior Valor")
    print("0 - Sair")
    try:
        op=int(input("Escolha uma da opções:"))
        if op<0 or op>3:
            raise ValueError
        if op == 1:
            try:
                n = int(input("Dimensão da matriz:"))
                if n<=0:
                    raise ValueError
                matriz=(inicializar(n))
                print("Matriz Gerada:")
                for i in range(n):
                    print("\n")
                    for j in range(n):
                        print(matriz[i][j], end=" ")
                input()
            except ValueError:
                print("Tem que ser um numero POSITIVO e MAIOR que 1")
            except:
                print("Error")
                input()
        if op == 2:
            tranposta(matriz,n)
    except ValueError:
        print("Opção não valida")
    except:
        print("ERROR")
        input()