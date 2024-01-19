#imports
from tkinter import *
import tkinter as tk

def guardar_ficheiro():
    """
        Guarda Texto no Ficheiro
    """
    ficheiro = open("texto.txt","w")#abre o ficheiro
    ficheiro.write(txtTexto.get("1.0","end"))#escreve no ficheiro todo conteudo
    ficheiro.close()#fecha o ficheiro

def Limpar():
    """
        Apaga texto na caixa de texto
    """
    txtTexto.delete("1.0","end")#apaga todo o conteudo na caixa de texto

def ler_ficheiro():
    """
        Lê o ficheiro e coloca todo o seu conteudo na caixa de texto
    """
    ficheiro= open("texto.txt","r")#abre o ficherio
    txtTexto.insert("1.0",ficheiro.read())#escreve o conteudo do ficheiro na caixa de texto
    ficheiro.close()#fecha o ficheiro
#Invocar Tk()
windows = tk.Tk()

windows.title("Exercicio 1")#Titlo
windows.geometry("800x600")#Tamanho
#Caixa de Texto
txtTexto = Text(windows, width=55, height=20, relief="sunken", bd=3)
txtTexto.place(x=200,y=20)
#
#Botões
btn_guardar = Button(windows,width = 20,height= 2, text="Guardar Ficheiro",command= guardar_ficheiro)#Botão para guardar
btn_guardar.place(x= 20, y= 50)

btn_limpar = Button(windows,width= 20,height= 2,text="Limpar", command=Limpar)#Botão para limpar
btn_limpar.place(x=20, y=150)

btn_Ler= Button(windows, width= 20, height=2, text="Ler Ficheiro", command=ler_ficheiro)#Botão para Ler
btn_Ler.place(x=20, y=250)
#

windows.mainloop()