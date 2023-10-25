# actualizar o programa de Fibonacci para acrescentar uma função


def FibonacciFuncion(termo):
    """
    Recebe n termos para imprime a sequencia de fibonacci 
    """
    antNum1 = 1
    antNum2 = 0
    num = 1
    if termo == 1:  # 1º termo
        print("0\n")
        return()
    elif termo == 2:# 2º Termo
        print("0 1\n")
        return()
    else:
        print("0 1", end=" ")
    for i in range(2,termo):
        print("%i"%num, end=" ")
        antNum2 , antNum1 = antNum1 , num #actualizar as variaveis
        num = antNum1 + antNum2 # somar os dois numeros anteriores
    print("\n")


termo = int(input("Numero de Termos:"))
FibonacciFuncion(termo)
FibonacciFuncion(5)
FibonacciFuncion(10)