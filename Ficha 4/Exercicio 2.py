# Programa para fazer uma função para somar entre dois numeros


def somatorio (inicio,fim):
    """
    Soma todos os numeros entre o entrevalo dos inseridos
    """
    if fim < inicio:
        temp = inicio
        inicio = fim
        fim = temp

    num = 0
    for i in range(inicio, fim+1):
        num += i 
    print("Soma:%d"%num)
somatorio(1,3)
somatorio(3,6)
  

