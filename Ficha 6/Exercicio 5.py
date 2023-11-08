#Create a program that allows you to read the sales volume over the 12 months of the year (from January to December).
#The program must include the calling of 3 functions which return, respectively:
# the month with the highest volume sales
# the month with the lowest sales
# the average sales value
import math

def highestSales(sales):
    """
        Return the month with the highest volume sales
    """
    return int(sales.index(max(sales)))
def LowestSales(sales):
    """
        Return the month with the Lowest volume sales
    """
    return int(sales.index(min(sales)))
def averageSales(sales):
    return float(sum(sales)/12)

data = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
sales=[]
for i in range(12):
    try:
        n = int(input("Faturação do mês de %s:"%data[i]))
        if n < 0:
            raise ValueError
        else:
            sales.append(n)        
    except ValueError:
        print("Erro, digite um numero")
        i-=1
    except:
        print("Erro")
        i-=1
print("Mes de maior faturação: %s"%data[highestSales(sales)])
print("Mes de menor faturação: %s"%data[LowestSales(sales)])
print("Valor Medio de Faturação: %.2f"%averageSales(sales))