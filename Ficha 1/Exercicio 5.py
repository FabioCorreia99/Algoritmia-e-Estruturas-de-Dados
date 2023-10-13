# transformar segundos em horas,minutos,segundos
segundos = int(input("Insira os segundo:"))
minutos = 0
horas = 0

while segundos>=60:
    minutos+=1
    segundos-=60
    if minutos>=60:
        horas+=1
        minutos-=60

print("Horas:%d Minutos:%d Segundos:%d"%(horas,minutos,segundos))
