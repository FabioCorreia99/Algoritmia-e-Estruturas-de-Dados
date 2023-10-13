#Calcular IMC e classificar o nivel de obsidade
peso = float(input("Peso(Kg):"))
altura  = (float(input("Altura(m):"))**2)
imc = peso/altura

print("IMC:%.2f"%imc)
if imc< 18.5:
    print("Under Weight")
elif imc< 25:
    print("Healthy")
elif imc< 30:
    print("Overweight")
elif imc< 35:
    print("Overweight Grade 1")
elif imc< 40:
    print("Overweight Grade 2")
else:
    print("Overweight Grade 3")