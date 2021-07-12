#vector que recibe diez numeros y retorna la posicion donde se encuentra el número mayor
vector = [1,2,3,4,5,6,7,8,9,10]     #Se crea un vector con sus datos

vector = [0]*10

for i in range (10):            #El usuario digita los numeros
    vector[i] = int(input(f'Escriba el {i+1} números entero'))

import random
for i in range (10):            #Se llena el vector con números aleatorias
    vector[i] = random.randint(1,9)

for i in range (10):            #imprimir
    print(f'En la posicion {i+1} esta el dato {vector[i]}')

#cual es el numero mayor y en que posición esta
mayor = vector[0]           #8
posicionMayor = 0           #2

for i in range(10):             # i = 5
    if vector[i] >= mayor:
        mayor = vector[i]
        posicionMayor = i

print("El número mayor es ",mayor)
print("Esta en la posición ",posicionMayor)

#Cual es el numero menor y en que posicion esta
menor = vector[0]
posicionMenor = 0

for i in range(10):
    if vector[i] < menor:
        menor = vector[i]
        posicionMenor = i

print("El número menor es ",menor)
print("Esta en la posición ",posicionMenor)

#Programa que indique en posición esta el mayor número par leido
mayor = vector[0]           #8
posicionMayor = 0           #2

for i in range(10):             # i = 5
    if vector[i] >= mayor and vector[i] % 2 == 0:
        mayor = vector[i]
        posicionMayor = i

print("El número mayor es ",mayor)
print("Esta en la posición ",posicionMayor)
print(len(vector))

#Leer 10 numeros enteros y determinar en que posiciones se encuentran los números terminados en 4
vector = [0]*(10)
for i in range(10):
    vector[i] = int(input("Digite el numero"))

for i in range(10):
    if vector[i] % 10 == 4:
        print(i, end=',')

#Leer 10 números enteros y determinar cuales son números primos
#dos divisores 1 y el numero
n = int(input("Digite el tamaño del vector"))
vector = [0] * n

for i in range(n):
    vector[i] = int(input())

for i in range(n):
    print (i)
    divisores = 0
    for j in range (1, vector[i]+1):
        if vector[i] % j == 0:
            divisores = divisores + 1

    if divisores > 2:
        print(f'El número {vector[i]} no es primo y la posicion es {i}')
    else:
        print(f'El número {vector[i]} es primo')

#LNumeros primos con Funciones
def esPrimo(num):
    divisores = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisores = divisores + 1
    return divisores > 2

n = int(input("Digite el tamaño del vector"))
vector = [0] * n

for i in range(n):
    vector[i] = int(input())

for i in range(n):
    if esPrimo(vector[i]):
        print(f'El número {vector[i]} es primo')
    else:
        print(f'El número {vector[i]} no es primo y la posicion es {i}')



