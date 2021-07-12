#Definir una matriz con datos constantes   [filas][columnas]
import random

matriz = [[0,1,2,3],
          [1,2,3,4],
          [5,6,7,8]]

filas = len(matriz)
print(f'El número de filas es {filas}')

columnas = len(matriz[0])
print (f'El número de columnas es {columnas}')

#Acceso a una posición específica
print(matriz[1][2])

#imprimir los valores de la matriz uno por uno
print(matriz[0][0], end = ',')
print(matriz[0][1], end = ',')
print(matriz[0][2], end = ',')
print(matriz[0][3])

print(matriz[1][0], end = ',')
print(matriz[1][1], end = ',')
print(matriz[1][2], end = ',')
print(matriz[1][3])

#Entrada de datos de una matriz por un usuario
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input())

#Creación de datos aleatorios
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(1,100)

#Impresion de los datos de la matriz
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end=',')
    print()

#1. Leer una matriz de 3 x 4 y determinar en que posición está el mayor
mat = [] * 3            #creamos la matriz de 3 x 4
for i in range(3):
    a = [0] * 4
    mat.append(a)

for i in range(3):
    for j in range(4):
        mat[i][j]=int(input(f'Digite el numero para la posicion {i},{j}'))

mayor = mat[0][0]
posFila = 0
posColumn = 0

for i in range(3):
    for j in range(4):
        if mat[i][j] > mayor:
            mayor = mat[i][j]
            posFila = i
            posColumn = j

print(f'El numero mayor es {mayor} y está en la posición {posFila},{posColumn}')

#2. Leer una matriz de 3 x 4 y determinar en que posición está el mayor número par
mat = [] * 3            #creamos la matriz de 3 x 4
for i in range(3):
    a = [0] * 4
    mat.append(a)

bandPares = False
for i in range(3):
    for j in range(4):
        mat[i][j] = int(input(f'Digite el numero para la posicion {i},{j}'))
        if mat[i][j] % 2 == 0:
            bandPares = True

if bandPares:
    mayor = mat[0][0]
    posFila = 0
    posColumn = 0

    for i in range(3):
        for j in range(4):
            if mat[i][j] > mayor and mat[i][j] % 2 == 0:
                mayor = mat[i][j]
                posFila = i
                posColumn = j

    print(f'El numero par mayor es {mayor} y está en la posición {posFila},{posColumn}')
else:
    print("No hay números pares")

#2. Leer una matriz 4x4 y determinar a cuánto es igual la suma de los elementos que se encuentran en su diagonal
mat = [] * 4            #creamos la matriz de 3 x 4
for i in range(4):
    a = [0] * 4
    mat.append(a)

for i in range(4):
    for j in range(4):
        mat[i][j]=int(input(f'Digite el numero para la posicion {i},{j}'))

#opcion1
suma = 0
for i in range(4):                  #i = 3
    suma = suma + mat[i][i]

#opcion2
suma = 0
i = 0
while i < 4:
    suma = suma + mat[i][i]
    i = i + 1

print(f'La suma de la diagonal es {suma}')

#3. Leer una matriz 4x3 y determinar cuántas veces se repite el mayor de los números almacenados en ella
mat = [] * 4            #creamos la matriz de 3 x 4
for i in range(4):
    a = [0] * 3
    mat.append(a)

for i in range(4):
    for j in range(3):
        mat[i][j]=int(input(f'Digite el numero para la posicion {i},{j}'))

mayor = mat[0][0]

for i in range(4):
    for j in range(3):
        if mat[i][j] > mayor:
            mayor = mat[i][j]

print(f'El numero mayor es {mayor}')

contadorNumeroMayor = 0
for i in range(4):
    for j in range(3):
        if mayor == mat[i][j]:
            contadorNumeroMayor = contadorNumeroMayor + 1

print(f'El numero mayor se encuentra {contadorNumeroMayor} veces')

#4. Leer una matriz 4x3 entera y determinar en que posiciones exactas se encuentran los números primos y cuáles son


