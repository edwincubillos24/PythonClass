#Definir una matriz con datos constantes
mat = [[0,1,2,3],
       [4,5,6,7],
       [8,9,10,11],
       [12,13,14,15]]

#imprimir el tamaño -> Número de filas
m = len(mat)
print("Número de filas", m)

#imprimir el número de columnas
n = len(mat[0])
print("Número de columnas",n)

#Para imprimir una matriz primero se debe recorrer las columnas de cada una de las filas, se inicia por la fila 0 columna 1, luego fila 0 columna2
print(mat[0][0], end=',')
print(mat[0][1], end=',')
print(mat[0][2], end=',')
print(mat[0][3])

print(mat[1][0], end=',')           #Luego se pasa a la
print(mat[1][1], end=',')
print(mat[1][2], end=',')
print(mat[1][3])

#Si observamos hay un incremento en las posiciones de 0 a su tamaño en las columnas y luego de 0 a su tamaño en las filas, esto se puede sistematizar
#para hacerlo de forma automática

for i in range(m):
    for j in range(n):
        print(mat[i][j], end=',')
    print()

#Definir una matriz e inicializarla con ceros
mat = [] * 6
for i in range(6):
    a = [0] * 8         #en Realidad es un vector
    mat.append(a)

m = len(mat)
print("Número de filas: ",m)
n = len(mat[0])
print("Número de columnas: ",n)

#Como recorremos la matriz?
for i in range(0, m):
    for j in range(0, n):
        print(mat[i][j], end=',')

#Si queremos que el usuario digite el tamaño de la matriz primero le debemos pedir el número de filas y luego el número de columnas
filas = int(input("Digite el número de filas"))
columnas = int(input("Digite el número de columnas"))

mat = []*filas
for i in range(filas):
    a = [0] * columnas
    mat.append(a)

#llenemos la matriz con datos aleatorios
import random
for i in range(filas):
    for j in range(columnas):
        mat[i][j] = random.randint(0,9)

for i in range(filas):
    for j in range(columnas):
        print(mat[i][j], end=',')
    print()

#Por último si queremos que el usuario digite también los valores de cada uno de las posiciones de la matriz
for i in range(filas):
    for j in range(columnas):
        mat[i][j] = int(input(f'Digite el valor de la fila {i} columna {j}'))

