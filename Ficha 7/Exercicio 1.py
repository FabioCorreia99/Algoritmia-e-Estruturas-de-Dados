#criar uma matrix 3x3 e imprimir a mesma e transposta
matriz=[]
for  i in range(3):
    matriz.append([])
    for j in range(3):
        matriz[i].append(input("Linha %d,coluna %d:"%(i+1,j+1)))

print("Matriz Original:\n")
for i in range(3):
    print("\n")
    for j in range(3):
        print(matriz[i][j], end=" ")
        
print("Matriz Transposta:\n")
for i in range(3):
    print("\n")
    for j in range(3):
        print(matriz[j][i], end=" ")
