import math



def sales_dec_media_order(sales,dates):
    """
        order the inputs, gibe average and the closest day
    """
    diff= math.inf
    prox =0
    order = sales.copy()
    data = dates.copy()
    # print da ordem decresente
    while len(order)>0:
        n = order.index(max(order))
        print("%s\t\t\t%s"%(order[n],data[n]))
        del order[n]
        del data[n]
    # print da media
    print("Nº medio de visitas diarias:%.2f"%(sum(sales)/7)) 
    # printe do dia mais proximo da media
    media = sum(sales)/7
    for i in range(7):
        if abs(sales[i]-media) < diff:
            prox = i
            diff= abs(sales[i]-media)
    print("Dia mais proximo do valor medio:%s"%dates[prox]) 
    #
data = ["Segunda","Terça","Quarta","Quinta","Sexta","Sabado","Domingo"]
sales = []
i=0
while i<7:
    try:
        sales.append(int(input("Visitas de %s:"%data[i])))
        i+=1
    except ValueError:
        print("Erro: Insira um numero")
    except:
        print("Error")
sales_dec_media_order(sales,data)