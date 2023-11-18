#Implement the rainfall function that receives the list of rainfall for each month (by input), and prints this same data (rainfall list), but sorted in descending order of rainfall.

def rainfall(rain,dates):
    """
        order the inputs
    """
    
    while len(rain)>0:
        n = rain.index(max(rain))
        print("%s\t\t\t%s"%(rain[n],dates[n]))
        del rain[n]
        del dates[n]
    
data = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
rain = []
i=0
while i<12:
    try:
        rain.append(int(input("Pluviosidade no mês de %s:"%data[i])))
        i+=1
    except ValueError:
        print("Erro: Insira um numero")
    except:
        print("Error")
rainfall(rain,data)