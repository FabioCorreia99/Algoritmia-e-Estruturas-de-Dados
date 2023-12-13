from tkinter import *
import tkinter as tk

windowns = tk.Tk()

def Tarefas_pendentes():
    Tpen_txt.delete("1.0","end")
    Tpen_txt.insert("1.0",todolist.size())

def Adicionar():
    todolist.insert("end",input_entry.get()+"\n")
    input_entry.delete(0,"end")
    Tarefas_pendentes()

def remover():
    todolist.delete(todolist.curselection())
    Tarefas_pendentes()

def removertudo():
    todolist.delete(0,"end")
    input_entry.delete(0,"end")
    Tarefas_pendentes()

def upload():
    ficheiro = open("texto.txt","r")
    Texto=ficheiro.readlines()
    for linha in Texto:
        todolist.insert("end",linha)
    ficheiro.close()
    Tarefas_pendentes()

def download():
    ficheiro = open("texto.txt","w")
    for i in range(todolist.size()):
        ficheiro.write(todolist.get(i))
    ficheiro.close()
    Tarefas_pendentes()
def ordenar():
    texto=[]
    for i in range(todolist.size()):
        texto.append(todolist.get(i))
    texto.sort()
    todolist.delete(0,"end")
    for linha in texto: 
        todolist.insert("end",linha)
    Tarefas_pendentes()
    
    

windowns.title("Exercicio 3")
windowns.geometry("800x600")

frame_txt = LabelFrame(windowns, width=300, height=350, relief="sunken")
frame_txt.place(x=10,y=20)

todolist= Listbox(frame_txt, width=33,height=19)
todolist.place(x=10,y=20)

frame_input = LabelFrame(windowns, width=300, height=100, relief="sunken")
frame_input.place(x=350,y=20)

input_label = Label(frame_input, text="Tarefa:", fg="blue")
input_label.place(x=20,y=30)

input_entry = Entry(frame_input, width=30)
input_entry.place(x=60,y=30)


btn_add = Button(windowns,width=10, text="Adicionar", command=Adicionar)
btn_add.place(x=360,y=250)

btn_remove = Button(windowns,width=10, text="remove", command=remover)
btn_remove.place(x=450,y=250)

btn_clear = Button(windowns,width=10, text="clear", command=removertudo)
btn_clear.place(x=540,y=250)

btn_upload = Button(windowns,width=10, text="Upload", command=upload)
btn_upload.place(x=360,y=300)

btn_download = Button(windowns,width=10, text="Download", command=download)
btn_download.place(x=450,y=300)

btn_download = Button(windowns,width=10, text="Ordenar", command=ordenar)
btn_download.place(x=540,y=300)

Tpen_label = Label(windowns,text="Nº de Tarefas Pendentes:",fg="blue")
Tpen_label.place(x=350,y=350)

Tpen_txt = Text(windowns,width=3,height=1)
Tpen_txt.place(x=490,y=350)

windowns.mainloop()
