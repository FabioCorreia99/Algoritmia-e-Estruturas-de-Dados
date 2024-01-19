from tkinter import *
import tkinter as tk 

def IMC():
    Resultado.set(peso.get() / altura.get()*altura.get()) 
    

windows = tk.Tk()

windows.title("Exercicio 4")
windows.geometry("800x600")
# Frame Inputs
frame_input = LabelFrame(windows, relief="raised", width=180, height=130)
frame_input.place(x=40,y=40)

peso = DoubleVar()
altura = IntVar()
Resultado = DoubleVar()
#------------ Labels
peso_label = Label(frame_input, text="Peso:", fg="blue")
peso_label.place(x=15,y=20)

altura_label = Label(frame_input, text="Altura(cm):", fg="blue")
altura_label.place(x=15,y=80)
#------------- Entrys
peso_entry = Entry(frame_input, width=10, textvariable=peso)
peso_entry.place(x=90,y=20)

altura_entry = Entry(frame_input, width=10, textvariable=altura)
altura_entry.place(x=90,y=80)
#
# Frame Result
frame_result = LabelFrame(windows,relief="raised",width=180,height=100)
frame_result.place(x=40,y=180)

result_label = Label(frame_result, text="Índice de Massa Corporal",fg="blue")
result_label.place(x=18,y=2)

result_entry = Entry(frame_result,state=DISABLED, width=10, textvariable=Resultado)
result_entry.place(x=40,y=40)

imc_button = Button(windows, height=3,width=10, text="Calcular \n IMC", command=IMC)
imc_button.place(x=250,y=100)

exit_button = Button(windows, height=3,width=10,text="Sair", command= windows.quit())
exit_button.place(x=250,y=180)

windows.mainloop()