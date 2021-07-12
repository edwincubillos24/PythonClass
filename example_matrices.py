# Leer una matriz de 5 x3 entera y determinar en que fila esta el mayor número primo

mat = [[200,150,25],
       [7,9,13],
       [8,25,24],
       [26,101,12],
       [13,17,19]]

for filas in range(5):
    for columnas in range(3):
        print(mat[filas][columnas], end =',')
    print()

posMayorPrimoFila = 0
posMayorPrimoColum = 0
primoMayor = mat[0][0]

for filas in range(5):
    for columnas in range(3):
        if mat[filas][columnas] > primoMayor:
            contadorDivisores = 0
            for i in range(1,mat[filas][columnas]+1):           #3  1 hasta 3  -> 1 2 3
                if mat[filas][columnas] % i == 0:                                                                  #verificar si es primo
                    contadorDivisores = contadorDivisores + 1
            if contadorDivisores == 2:
                primoMayor = mat[filas][columnas]
                posMayorPrimoFila = filas
                posMayorPrimoColum = columnas

print(f'El número mayor es {primoMayor} y esta en la fila {posMayorPrimoFila} y columna {posMayorPrimoColum}')

# Leer una matriz de 5 x3 entera y determinar en que posiciones y que numeros primos hay

mat = [[200,150,225],
       [7,9,13],
       [8,25,24],
       [26,101,12],
       [13,17,19]]

class Primos:
    def __init__(self, numero, fila, columna):
        self.numero = numero
        self.fila = fila
        self.columna = columna

listPrimos = []
for filas in range(5):
    for columnas in range(3):

        contDivisores = 0
        for i in range(1, mat[filas][columnas]+1):            #Validar que es número primo
            if mat[filas][columnas] % i == 0:
                contDivisores = contDivisores + 1
        if contDivisores == 2:
            primo = Primos(numero= mat[filas][columnas], fila= filas, columna=columnas)
            listPrimos.append(primo)

for primo in listPrimos:
    print(f'El numero {primo.numero} esta en la fila {primo.fila} y columna {primo.columna}')

#y donde esta el numero mayor primo
mayorPrimo = listPrimos[0].numero

for primo in listPrimos:
    if primo.numero > mayorPrimo:
        mayorPrimo = primo.numero

print(f'El primo mayor es {mayorPrimo}')

listNumero = []
listFilas = []
listColumnas = []

for filas in range(5):
    for columnas in range(3):

        contDivisores = 0
        for i in range(1, mat[filas][columnas]+1):            #Validar que es número primo
            if mat[filas][columnas] % i == 0:
                contDivisores = contDivisores + 1
        if contDivisores == 2:
            listNumero.append(mat[filas][columnas])
            listFilas.append(filas)
            listColumnas.append(columnas)

for i in range (len(listNumero)):
    print(f'El numero {listNumero[i]} esta en la fila {listFilas[i]} y columna {listColumnas[i]}')

#Leer una matriz 5 x 3 y mostrar cuales números se repiten y cuantas veces

mat = [[200,150,8],
       [7,9,13],
       [8,25,8],
       [26,12,12],
       [13,12,8]]

numerosRepetidos = []
cantidadRepeticiones = []
for filas in range (5):             #filas = 1
    for columnas in range (3):      #columnas =2
        numero = mat[filas][columnas] #numero = 200

        contador = 0
        isSaved = False
        for i in range (5):
            for j in range (3):
                if numero == mat[i][j]:
                    contador = contador + 1
                    if contador > 1:
                        if numero not in numerosRepetidos:
                            numerosRepetidos.append(numero)
                            isSaved = True
        if isSaved:
            cantidadRepeticiones.append(contador - 1)


for k in range (len(numerosRepetidos)):
    print(f'El numero {numerosRepetidos[k]} se repite {cantidadRepeticiones[k]}')

mat =  [[3,4,5,6],
        [5,6,7,8],
        [5,6,7,8],
        [7,8,7,6]]

diagonalPpal = 0
for i in range (4):
    diagonalPpal = diagonalPpal + mat[i][i]

diagonalSec = 0
diagonalSec = diagonalSec + mat[0][3]
diagonalSec = diagonalSec + mat[1][2]
diagonalSec = diagonalSec + mat[2][1]
diagonalSec = diagonalSec + mat[3][0]
diagonalSec = 0
for i in range (4):
    for j in range (3,-1,-1):
        diagonalSec = diagonalSec + mat[i][j]