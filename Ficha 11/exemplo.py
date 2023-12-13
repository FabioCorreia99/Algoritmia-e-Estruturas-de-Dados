#import tkinter as tk
from tkinter import *

def ler_ficheiro():
    f = open("../ficheiros/paises.txt","r")

    text_box.delete("1.0","end")
    for line in f:
        text_box.insert("end",line)
    f.close()

def escrever_ficheiro():
    f = open("../ficheiros/paises.txt","a")
    pais = pais_entry.get()
    cont = cont_entry.get()
    f.writelines(pais_entry+";"+cont_entry+"\n")
    f.close()
    ler_ficheiro()

window = Tk()

window.title("Herlo, tkinter")
window.geometry("1400x600")

text_box = Text(window, width=40, height=10)
text_box.place(x=10, y=10)

ler_button = Button(window, text="Ler Ficheiro", )
ler_button.place(x=10, y=300)

pais_label = Label(window, text="País:")
pais_label.place(x=10,y=200)
pais_entry = Entry(window, width=20, textvariable="pais")
pais_entry.place(x=40,y=200)

cont_label = Label(window, text="Continente:")
cont_label.place(x=10,y=250)
cont_entry = Entry(window, width=20, textvariable="continente")
cont_entry.place(x=80,y=250)

window.mainloop()