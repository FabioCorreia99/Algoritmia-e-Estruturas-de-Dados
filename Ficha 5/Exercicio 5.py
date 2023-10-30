#shortName function

def shortName(name):
    """
        Retorna so O Primeiro e Ultimo nome
    """
    name1 = name[:name.find(" ")]#passa para name1 até o primeiro espaço
    name1 = name1 + name[name.rfind(" "):]#passa para name1 começando do fim até o primeiro espaço que encontrar
    return name1

name = str(input("Insira a frase:\n\n\t\t"))
print(shortName(name))