from tkinter import *
import tkinter as tk

def guardar_ficheiro():
    ficheiro = open("texto.txt","w")
    ficheiro.write(txtTexto.get("1.0","end"))
    ficheiro.close()

def Limpar():
    txtTexto.delete("1.0","end")

def ler_ficheiro():
    ficheiro= open("texto.txt","r")
    txtTexto.insert("1.0",ficheiro.read())
    ficheiro.close()

windows = tk.Tk()

windows.title("Exercicio 1")
windows.geometry("800x600")

txtTexto = Text(windows, width=55, height=20, relief="sunken", bd=3)
txtTexto.place(x=200,y=20)

btn_guardar = Button(windows,width = 20,height= 2, text="Guardar Ficheiro",command= guardar_ficheiro)
btn_guardar.place(x= 20, y= 50)

btn_limpar = Button(windows,width= 20,height= 2,text="Limpar", command=Limpar)
btn_limpar.place(x=20, y=150)

btn_Ler= Button(windows, width= 20, height=2, text="Ler Ficheiro", command=ler_ficheiro)
btn_Ler.place(x=20, y=250)



windows.mainloop()