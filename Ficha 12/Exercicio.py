#Imports
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import datetime as data

def ler_ficheiro():
        """
            le ficheiro para uma variavel
        """
        lista=[]#lista 
        i=0#var auxiliar
        ficheiro = open("./files/acessos.txt","r")#abre ficheiro
        for linhas in ficheiro:#percorre todo ficheiro
            lista.append([])#add lista na lista
            linha = linhas.split(";")#divide o conteudo
            linha[3] = linha[3].replace("\n","")#retira o \n no final da linha
            for j in range(4):#preenche alista com os dados
                    lista[i].append(linha[j])
            i+= 1
        ficheiro.close()#fecha o ficheiro
        return lista #retorna a lista


class App:
    def Consulta(self):
        """
            Window Consulta
        """
        
        original_frame.withdraw() # Fecha Window do menu
        #formação da window
        self.top = Toplevel()
        self.top.geometry("750x330")
        self.top.title("Entradas e Saídas")
        self.top.focus_force() #Força toda a interação com a janela actual
        self.top.grab_set()

        # Painel
        panel1 = LabelFrame(self.top, width=200, height=300, relief="sunken")
        panel1.place(x=15,y=20)

        # Frame Tipo de Movimento
        lframe = LabelFrame(panel1,width=160,height=100,bd="3",text="Tipo de Movimento",fg="blue", relief="sunken")
        lframe.place(x=5,y=5)
        self.cb1 = BooleanVar()
        self.cb2 = BooleanVar()
        ck1 = Checkbutton(lframe, text="Entrada", variable=self.cb1)
        ck1.place(x=15,y=15)
        ck2 = Checkbutton(lframe, text="Saida", variable=self.cb2)
        ck2.place(x=15,y=40)

        # Frame Utilizador
        lframe2 = LabelFrame(panel1, width=160, height=100, bd=3, text="Por Utilizador", fg="blue", relief="sunken")
        lframe2.place(x=5,y=120)
        lbl_utilizador = Label(lframe2, text="Número:")
        lbl_utilizador.place(x=15,y=5)
        self.utilizador = StringVar()
        utili_entry = Entry(lframe2,width=20,textvariable=self.utilizador)
        utili_entry.place(x=10,y=25)

        # Painel 2
        panel2 = LabelFrame(self.top, width=460, height=250, bd="3",relief="sunken")
        panel2.place(x=220,y=20)

        # TreeView para consulta de movimentos
        global tree 
        tree = ttk.Treeview(panel2, selectmode="browse", columns=("Número","Data","Hora","Movimento"), show="headings")

        tree.column("Número", width=100, anchor="c")
        tree.column("Data", width=100, anchor="c")
        tree.column("Hora", width=100, anchor="c")
        tree.column("Movimento", width=140, anchor="c")
        tree.heading("Número", text="Número")
        tree.heading("Data", text="Data")
        tree.heading("Hora", text="Hora")
        tree.heading("Movimento", text="Movimento")
        tree.place(x=5,y=5)

        # Buttoes -Consultar- -Sair-
        btn_consultar = Button(panel1,width=10,height=3,text="Consultar", command=self.FiltrarTree)
        btn_consultar.place(x=5,y=230)
        btn_sair = Button(panel1,width=10,height=3,text="Sair", command=self.fechar)
        btn_sair.place(x=90,y=230)
        
        self.PreencherTree()#preencher tree

    def PreencherTree(self):
        lista= ler_ficheiro()#cria a lista com os dados do ficheiro
        tree.delete(*tree.get_children()) #apaga o conteudo 
        for i in range(len(lista)):#preenche com todo o conteudo do ficheiro        
            tree.insert("","end", values= (lista[i][0],lista[i][1],lista[i][2],lista[i][3]))
        
    def FiltrarTree(self):
        tree.delete(*tree.get_children())#Apagar todos os valores
        lista = ler_ficheiro()#le o ficheiro
        aux= "" # variavel auxiliar para as check boxes
        #-----------------Confirmação dos dados----------------------
        if self.cb1.get() == True and self.cb2.get() == True:#se as duas tiverem 'checked' dá um valor á variavel 
            aux="t"
        else:
            if self.cb1.get() == True:# se a box entrada tiver check dá um valor á variavel
                aux = "Entrada"
            if self.cb2.get() == True:# se a box saida tiver check dá um valor á variavel
                aux = "Saida"
        #-----------------------------------------------------
        if aux=="t":#confirma se as duas boxes estão 'check'
            for i in range(len(lista)):#for para percorrer a lista        
                if self.utilizador.get()=="" or self.utilizador.get()==lista[i][0]:#confirma o input da procura por numero de aluno
                    tree.insert("","end", values= (lista[i][0],lista[i][1],lista[i][2],lista[i][3]))#print
        #-------------------------------------------------------------------------------------------
        else:
            for i in range(len(lista)):#for para percorrer a lista         
                if self.utilizador.get()=="" or self.utilizador.get()==lista[i][0]:#confirma o input da procura por numero de aluno
                    if lista[i][3] == aux:# confirma se o valor é igual á box que o utilizador deu check
                        tree.insert("","end", values= (lista[i][0],lista[i][1],lista[i][2],lista[i][3]))#print
           

    def movimentos(self):
            """
                Window Movimentos
            """
            original_frame.withdraw() # Fecha Window do menu

            self.top = Toplevel()
            self.top.geometry("750x310")
            self.top.title("Entradas e Saídas")
            self.top.focus_force() #Força toda a interação com a janela actual
            self.top.grab_set() #Força quetodos os eventos estejam enquadrados no componente atual 
            #Labels
            lbl_numero = Label(self.top, text="Número de Estudante:")
            lbl_numero.place(x=20,y=15)

            txt_label = Label(self.top,text="Histórico de movimentos", fg="blue")
            txt_label.place(x=450,y=15)

            #Entry Numero de utilizador
            self.numero = IntVar()
            self.txt_numero = Entry(self.top, width= 20, textvariable=self.numero)
            self.txt_numero.place(x=150,y=15)

            #LabelFrame
            lframe = LabelFrame(self.top, width=200, height= 130, text="Género",fg="blue",relief="sunken")
            lframe.place(x=15,y=50)

            #radiobutton
            self.selected = StringVar()
            self.selected.set("Entrada")
            rd1 = Radiobutton(lframe, text="Entrada", value="Entrada", variable= self.selected)
            rd1.place(x=15,y=20)
            rd2 = Radiobutton(lframe, text="Saida", value="Saida", variable= self.selected)
            rd2.place(x=15,y=50)

            #Button
            btn_registar = Button(self.top, width=10,height=3,text="Registar", command=self.registar)
            btn_registar.place(x=250,y=80)

            btn_sair = Button(self.top, width=10,height=3,text="Sair", command=self.fechar)
            btn_sair.place(x=250,y=140)

            #ListBox
            self.txt_List= Listbox(self.top, width=45,height=15)
            self.txt_List.place(x=375,y=50)

            

    def __init__(self,window, img):
        self.window = window

        # Implementar Menu
        barra_Menu = Menu(self.window)

        barra_Menu.add_command(label="Movimentos", command = self.movimentos)# Window Movimentos
        barra_Menu.add_command(label="Consulta", command=self.Consulta)# Window consulta
        barra_Menu.add_command(label="Sair", command= window.quit)# Sair  
        window.configure(menu = barra_Menu)

        #Lable
        lbl = Label(window, text="Gestão de Presenças")
        lbl.place(x=450,y=120)

        #container Canvas
        ctn_canvas = Canvas(window, width=400, height=280, bd=4, relief="sunken")
        ctn_canvas.place(x=0,y=0)
        ctn_canvas.create_image(200,150, image = img)
        
    def fechar(self):
         """
            fecha a window e abre a main window
         """
         self.top.destroy()
         original_frame.update()
         original_frame.deiconify()
    def registar(self):
        """
            Coleta os dados e guarda num ficheiro e numa caixa de texto, confirmando se é um input valido
        """
        lista_txt=[]
        ano = data.datetime.now()#lê data
        # confirma se tem pelo menos um input
        if(self.txt_List.size()>0):
            lista_txt = ler_ficheiro()#guarda o historico numa lista de lista
            #Confirma se o ultimo input do aluno não é entrada
            if(self.selected.get()=="Entrada"):# confirma se o aluno entrou e não saiu
                for i in range(self.txt_List.size()-1,-1,-1):#percorre a partir do fim
                    if(self.numero.get() == int(lista_txt[i][0])):
                        if(lista_txt[i][3]=="Entrada"): 
                            messagebox.showerror("Entrada Invalida","Aluno Ja entrou")
                            return
            #Confima se o ultimo input é entrada do aluno, se nao da erro
            aux=True#variavel para saber se o aluno tem historico
            if(self.selected.get()=="Saida"):
                aux = False#actualiza a variavel ja que é input de saida
                for i in range(self.txt_List.size()-1,-1,-1):
                    if(self.numero.get() == int(lista_txt[i][0])):
                        aux= True#actualiza pois existe historico
                        if(lista_txt[i][3]=="Saida"):#confirma se o ultimo input é saida
                            messagebox.showerror("Saida Invalida","Aluno Ja Saiu")#se for dá erro, pois nao pode sair duas vezes
                            return
                        else:
                            break# se nao for está tudo bem
            if not aux: # se nao tiver historico, é porque nunca entrou, então o input de saida é invalido
                messagebox.showerror("Saida Invalida","Aluno não entrou para sair")
                return
            #------------------------------------------------------------------------------                
        self.txt_List.insert("end",str(self.numero.get())+";"+ano.strftime("%Y-%m-%d")+";"+ano.strftime("%H-%M-%S")+";"+self.selected.get()+"\n")#apresentao input no texto
        #guarda no ficheiro de input em input
        ficheiro = open("./files/acessos.txt","a")
        ficheiro.write(str(self.numero.get())+";"+ano.strftime("%Y-%m-%d")+";"+ano.strftime("%H-%M-%S")+";"+self.selected.get()+"\n")
        ficheiro.close()
                    
                


        


window = tk.Tk()
window.title("Exercicio da Ficha 12")
window.geometry("700x300")

img = ImageTk.PhotoImage(Image.open("C:/Users/fabio/OneDrive/Documentos/Algoritmia e Estruturas de Dados/Ficha 12/1920x1080-Information-Technology-Person-PNG.png"))
original_frame = window#guarda a main window

if not os.path.exists("./files"):#Confirma se o path existe, cria se nao
    os.mkdir("files")


ficheiro = open("./files/acessos.txt","w")#optei por resetar sempre que abre pois não fala nada de fazer botão de reset
ficheiro.close()

App(window, img)

window.mainloop()