# Programa para gerar um numero entre 1700-2020 e disser que é bissexto
import random 

op = "s"
while op.upper() !='N': #Enquanto a opção for sim, vai executar o loop
    ano = random.randint(1900,2020)
    if ano % 4 == 0 : # perguntar se é divisivel por 4
        if ano % 100 == 0:# perguntar se é divisivel por 100
            if ano % 400 == 0:# perguntar se é divisivel por 400
                print("%i é bissexto"%ano)
            else:
                print("%i não é bissexto"%ano)
        else:
            print("%i é bissexto"%ano)
    else:
        print("%i não é bissexto"%ano)
    op = input("Gerar um novo numero?(S/N)")#perguntar se quer continuar
        

