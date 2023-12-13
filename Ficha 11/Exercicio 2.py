from tkinter import *
from tkinter import messagebox
import tkinter as tk


def calculo_pesoIdeal():
    if genero.get() == "homem":
        pesoIdeal = (altura.get()-100)-(altura.get()-150)/4
    elif genero.get() == "mulher":
        pesoIdeal = (altura.get()-100)-(altura.get()-150)/2
    else:
        messagebox.showerror("Erro","Erro. Tem que escolher um genero")
        return
    peso_text.delete("1.0","end")
    peso_text.insert("1.0",pesoIdeal)
    
windows = tk.Tk()

windows.title("Exercicio 2")
windows.geometry("800x600")

altura_label = Label(windows, text="Altura em cm:", fg="blue")
altura_label.place(x=50,y=50)

altura = IntVar()
altura_entry= Entry(windows, width=15, textvariable= altura)
altura_entry.place(x=130,y=50)

frame_genero = LabelFrame(windows, text="Género", relief="sunken", width=200, height=150, fg="Blue")
frame_genero.place(x=50, y=120)

frame_result = LabelFrame(windows, relief="sunken", width=200, height=150, fg="Blue")
frame_result.place(x=400, y=120)

genero = StringVar()

checkH = Radiobutton(frame_genero, text="homem",value="homem", variable=genero)
checkH.place(x=10,y=10)
checkM = Radiobutton(frame_genero, text="Mulher",value="mulher", variable=genero)
checkM.place(x=10,y=60)


btn_calculo = Button(windows,height=10 ,text="Calcular Peso Ideal",  command= calculo_pesoIdeal)
btn_calculo.place(x=265,y=120)

peso_label = Label(frame_result, fg="blue",text="Peso Ideal em Kg")
peso_label.place(x=45,y=30)

peso_text = Text(frame_result, width=11, height=1)
peso_text.place(x=45,y=50)


windows.mainloop()