import numpy as np

Matriz = []
valor = 0
print('Ingrese los valores de la nuevaMatriz: ')
for i in range(3):
    for j in range(4):
        valor = int(input(f"Ingrese el valor de la posición [{i+1}][{j+1}]:  "))
        Matriz.append(valor)
nuevaMatriz = np.array(Matriz)
nuevaMatriz = np.resize(nuevaMatriz, (3,4))
print("\n")
for i in range(3):
    if (i != 0):
        print("\n")
    for j in range(4):
        print(f"{nuevaMatriz[i][j]}\t", end="")


def ne(ea, pa, eccp, ecrp, P_anterior):
    ne = (ea*pa - eccp*ecrp)/P_anterior
    return ne

#Resolvemos el primer paso del método.
ne11 = ne(nuevaMatriz[1][1], nuevaMatriz[0][0], nuevaMatriz[0][1], nuevaMatriz[1][0], 1)
ne12 = ne(nuevaMatriz[1][2], nuevaMatriz[0][0], nuevaMatriz[0][2], nuevaMatriz[1][0], 1)
ne13 = ne(nuevaMatriz[1][3], nuevaMatriz[0][0], nuevaMatriz[0][3], nuevaMatriz[1][0], 1)
ne21 = ne(nuevaMatriz[2][1], nuevaMatriz[0][0], nuevaMatriz[0][1], nuevaMatriz[2][0], 1)
ne22 = ne(nuevaMatriz[2][2], nuevaMatriz[0][0], nuevaMatriz[0][2], nuevaMatriz[2][0], 1)
ne23 = ne(nuevaMatriz[2][3], nuevaMatriz[0][0], nuevaMatriz[0][3], nuevaMatriz[2][0], 1)
nuevaMatriz[1][0] = 0
nuevaMatriz[2][0] = 0
nuevaMatriz[1][1] = ne11
nuevaMatriz[1][2] = ne12
nuevaMatriz[1][3] = ne13
nuevaMatriz[2][1] = ne21
nuevaMatriz[2][2] = ne22
nuevaMatriz[2][3] = ne23
print("\n\n\n")
for i in range(3):
    if (i != 0):
        print("\n")
    for j in range(4):
        print(f"{nuevaMatriz[i][j]}\t", end="")

#Resolvemos el segundo paso del método.
ne02 = ne(nuevaMatriz[0][2], nuevaMatriz[1][1], nuevaMatriz[0][1], nuevaMatriz[1][2], nuevaMatriz[0][0])
ne03 = ne(nuevaMatriz[0][3], nuevaMatriz[1][1], nuevaMatriz[0][1], nuevaMatriz[1][3], nuevaMatriz[0][0])
ne22 = ne(nuevaMatriz[2][2], nuevaMatriz[1][1], nuevaMatriz[1][2], nuevaMatriz[2][1], nuevaMatriz[0][0])
ne23 = ne(nuevaMatriz[2][3], nuevaMatriz[1][1], nuevaMatriz[1][3], nuevaMatriz[2][1], nuevaMatriz[0][0])
nuevaMatriz[0][1] = 0
nuevaMatriz[2][1] = 0
nuevaMatriz[0][0] = nuevaMatriz[1][1]
nuevaMatriz[0][2] = ne02
nuevaMatriz[0][3] = ne03
nuevaMatriz[2][2] = ne22
nuevaMatriz[2][3] = ne23
print("\n\n\n")
for i in range(3):
    if (i != 0):
        print("\n")
    for j in range(4):
        print(f"{nuevaMatriz[i][j]}\t", end="")

#Resolvemos el tercer paso del método.
ne03 = ne(nuevaMatriz[0][3], nuevaMatriz[2][2], nuevaMatriz[0][2], nuevaMatriz[2][3], nuevaMatriz[1][1])
ne13 = ne(nuevaMatriz[1][3], nuevaMatriz[2][2], nuevaMatriz[1][2], nuevaMatriz[2][3], nuevaMatriz[1][1])
nuevaMatriz[0][3] = ne03
nuevaMatriz[1][3] = ne13
nuevaMatriz[0][0] = nuevaMatriz[2][2]
nuevaMatriz[1][1] = nuevaMatriz[2][2]
nuevaMatriz[0][2] = 0
nuevaMatriz[1][2] = 0
print("\n\n\n")
for i in range(3):
    if (i != 0):
        print("\n")
    for j in range(4):
        print(f"{nuevaMatriz[i][j]}\t", end="")
x = nuevaMatriz[0][3]/nuevaMatriz[0][0]
y = nuevaMatriz[1][3]/nuevaMatriz[1][1]
z = nuevaMatriz[2][3]/nuevaMatriz[2][2]
print(f"\n\nResultados: ")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")