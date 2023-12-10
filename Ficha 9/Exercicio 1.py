#APP para inserir paises/consultar Países/continentes/nº de paises

def add_pais():
    """
        Adiciona Pais caso nao esteja no file
    """
    paises = open("C:\\Users\\fabio\\OneDrive\\Documentos\\Algoritmia e Estruturas de Dados\\Ficha 9\\files\\paises.txt","r", encoding="utf-8")
    ficheiro = paises.readlines()# Abre o ficheiro e copia para uma variavel todo o contéudo
    paises.close()# fecha o ficheiro
    pais = str(input("\t\tPaís\t: "))# ler o pais
    continente = str(input("\t\tContinente  : "))# ler o continente
    for linha in ficheiro:#variavel para percorrer as linhas
        val = linha.split(";")# dividir em sub strings 
        if pais.lower() == val[0].lower():# pergunta de ja existe no file
            print("Esse país ja existe em Sistema")
            input("Prima <ENTER> para continuar...")
            return
    paises = open("C:\\Users\\fabio\\OneDrive\\Documentos\\Algoritmia e Estruturas de Dados\\Ficha 9\\files\\paises.txt","a", encoding="utf-8")
    paises.write(pais+";"+continente+"\n")# se nao existe acrescenta no file
    paises.close()

def Listagem():
    """
        Lista Todos os paises
    """
    paises = open("C:\\Users\\fabio\\OneDrive\\Documentos\\Algoritmia e Estruturas de Dados\\Ficha 9\\files\\paises.txt","r", encoding="utf-8")
    linha = paises.readline()# Abrir file
    print("\tPaíses\t\t\tContinente")
    print("-------------------------------------------")
    while linha != "":# while para percorrer todas as linhas
        aux = linha.split(";")# dividir em sub strings
        print("\t%s\t\t%s"%(aux[0],aux[1]))#imprimir o pais e o continente
        linha= paises.readline()#ler nova linha
    paises.close()#fechar file
    input("Prima <ENTER> para continuar...")#input para dar tempo ao utilizador

def List_Cotinente(continente):
    """
        Lista paises por Continente
    """
    i=False
    paises = open("C:\\Users\\fabio\\OneDrive\\Documentos\\Algoritmia e Estruturas de Dados\\Ficha 9\\files\\paises.txt","r", encoding="utf-8")
    ficheiro = paises.readlines()# Abrir Ficheiro e guarda todo o seu conteudo
    paises.close()#fecha o file
    print("\tPaíses\t\t\tContinente")
    print("-------------------------------------------")
    for linha in ficheiro:#for para percorrer todo o ficheiro
        aux = linha.split(";")# variavel para dividir em sub strings
        aux[1] = aux[1].replace("\n","")#como é o fim da linha tirar o  \n para a comparar
        if continente.lower() == aux[1].lower():#pergunta se são iguais
            print("\t%s\t\t%s"%(aux[0],aux[1]))#imprime
            i=True#variavel para saber se tem dados ou nao
    if i == False:#se nao tiver paises do contimente que inseriu print erro
        input("\n\nNão Existem Dados desse Continente...\nPrima <ENTER> para continuar...")#input para dar tempo ao utilizador
        return
    input("Prima <ENTER> para continuar...")#input para dar tempo ao utilizador

def n_paises():
    """
        Imprime n paises para cada continente
    """
    continente=[]
    paises = open("C:\\Users\\fabio\\OneDrive\\Documentos\\Algoritmia e Estruturas de Dados\\Ficha 9\\files\\paises.txt","r", encoding="utf-8")
    ficheiro = paises.readlines()# Abrir Ficheiro e guarda todo o seu conteudo
    paises.close()#fecha o file
    # for para percorrer todo o file e guardar numa variavel todos os continentes sem repetir
    for linha in ficheiro:#variavel para percorrer as linhas
        val = linha.split(";")# dividir em sub strings 
        val[1] = val[1].replace("\n","")
        if val[1] not in continente:# pergunta de ja existe no file
            continente.append(val[1])#acrescenta
    #
    try:#ler quantas vezes o utilizador quer imprimir
        n = int(input("Insira quantos Paises deseja imprimir por Continente:"))
        if(n<1):#tem que ser positivo
            raise ValueError    
    except ValueError:
        print("Insira um numero Inteiro e possitivo")
    except:
        print("Erro")
    aux = 0
    #
    for i in range(len(continente)):#for para percorrer os continentes
        print("-------------------------------------------")
        print("\tPaíses do Continente:%s\n\n"%continente[i])
        for linha in ficheiro:# e para percorrer os paises
            val = linha.split(";")# dividir em sub strings 
            val[1] = val[1].replace("\n","")
            if continente[i] == val[1]:#verifica se o continente do pais é igual
                print("\t%s\t\t%s"%(val[0],val[1]))#imprime
                aux+=1#soma no contador
            if aux == n:#se o contador chegar ao valor do cliente, para e passa para o proximo continente
                break
        print("\n\n")
        aux=0
    #
    input("Prima <ENTER> para continuar...")#input para dar tempo ao utilizador

op=-1
#     ----- Menu Inicial -----
while op != 0:
    print("\n\n\n\n\n\n\n\n")
    print("MENU:\n")
    print("1 - Inserir Países\n2 - Consulta Países\n3 - Consulta por continente\n4 - Consulta nº países\n0 - Sair")
    try:    
        op = int(input())
        if op < 0 or op >4:
            raise ValueError
        if op == 1:
            add_pais()
        if op == 2:
            Listagem()
        if op == 3:
            continente = str(input("\t\tContinente:"))#perguntar o continente para procura
            List_Cotinente(continente)
        if op == 4:
            n_paises()
    except ValueError:
        print("Opção não valida")
        input("Prima <ENTER> para continuar...")#input para dar tempo ao utilizador
    except:
       print("ERROR")
       input("Prima <ENTER> para continuar...")#input para dar tempo ao utilizador
#     ----- Menu Inicial -----