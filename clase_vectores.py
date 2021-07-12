#vectores

#Crear un programa que reciba 10 números y calcule su suma

i = 0  #contador
suma = 0   #acumulador
while i < 10:
    numero = int(input(f"Digite el {i+1} número: "))
    suma = suma + numero
    i = i + 1
print(f"El valor de la suma es {suma}")

suma = 0
for i in range(0,10,1):
    numero = int(input(f"Digite el {i + 1} número: "))
    suma = suma + numero
    i = i + 1
print(f"El valor de la suma es {suma}")

#Crear un programa que reciba 10 números y calcule su suma y después imprima cada uno de los números digitados

suma = 0
for i in range(0,10,1):
    numero = int(input(f"Digite el {i + 1} número: "))
    suma = suma + numero
    i = i + 1
print(f"El valor de la suma es {suma}")

#Vectores
#Definicion e inicialización de vectores

vector = [0]*(10)
print(vector)
print(vector[9])
vector[8] = 4
print(vector[8])

vector = [0]*(10)   #definir mi vector
suma = 0            #inicializo mi acumulador
for i in range(10):         #Entrada de datos
    vector[i] = int(input(f'Digite el {i+1} número'))

for i in range(10):         #imprimer los datos que digitó el usuario
    print(f'El {i+1} que usted digitó es {vector[i]}')

i = 0                       #imprime la posición del vector y su respectivo valor
while i<10:
    print(f'En la posicion {i} del vector esta el valor {vector[i]}')
    i = i + 1

for i in range(10):         #Calcula e imprime la suma de los datos
    suma = suma + vector[i]
print ("La suma es: ", suma)

print(vector)

print("El número de datos que tiene el vector es ", len(vector))

#Crear una función que reciba un arreglo y un número (tamaño del arreglo)
#El usuario debe digitar el tamaño del arreglo y llenarlo con numeros aleatorios entre 1 a 99

import random

def llenadoArreglo(arreglo, n):
    for i in range (0,n):
        arreglo[i] = random.randint(1,99)

n = int(input("Digite el tamaño del vector: "))
arreglo = [0]*n
print(arreglo)
llenadoArreglo(arreglo,n)
print(arreglo)

#Crear un programa que cree un vector de n posiciones dadas por el usuario con numeros aleatorios
# e imprima los pares

import random

def llenadoArreglo(arreglo, n):
    for i in range (0,n):
        arreglo[i] = random.randint(1,99)

n = int(input("Digite el tamaño del vector: "))
arreglo = [0]*n
llenadoArreglo(arreglo, n)
print(arreglo)
for i in range(0,n):
    if arreglo[i] % 2 == 0:
        print(arreglo[i])

#Crear un programa que cree un vector de n posiciones dadas por el usuario con numeros aleatorios
# almacene en un vector los números pares, en otro los numeros impares  y luego imprima los pares
#Opcion 1
import random

def llenadoArreglo(arreglo, n):
    for i in range (0,n):
        arreglo[i] = random.randint(1,99)

n = int(input("Digite el tamaño del vector: "))
arreglo = [0]*n
llenadoArreglo(arreglo, n)
print(arreglo)
contPares = 0
contImpares = 0
for i in range(0,n):            #Se recorre el arreglo para saber si el numero es par o impar e incrementar el cont
    if arreglo[i] % 2 == 0:
        contPares = contPares+1
    else:
        contImpares = contImpares + 1

numerosPares = [0] * contPares         #inicializar los vectores respectivos con la memoria necesaria
numerosImpares = [0] * contImpares

contPares=0
contImpares=0
for i in range(0,n):
    if arreglo[i] % 2 == 0:
        numerosPares[contPares] = arreglo[i]
        contPares = contPares+1
    else:
        numerosImpares[contImpares] = arreglo[i]
        contImpares = contImpares + 1
print("Numeros pares: ",numerosPares)
print("Numeros impares: ",numerosImpares)

#opcion2
import random

def llenadoArreglo(arreglo, n):
    for i in range (0,n):
        arreglo[i] = random.randint(1,99)

n = int(input("Digite el tamaño del vector: "))
arreglo = [0]*n
llenadoArreglo(arreglo, n)
print(arreglo)
numerosPares = []
numerosImpares = []
for i in range(0,n):            #Se recorre el arreglo para saber si el numero es par o impar e incrementar el cont
    if arreglo[i] % 2 == 0:
        numerosPares.append(arreglo[i])
    else:
        numerosImpares.append(arreglo[i])
print("Numeros pares: ",numerosPares)
print("Numeros impares: ",numerosImpares)
print("Numeros pares ordenados: ",numerosPares.sort())
print(numerosPares)
print(type(numerosPares))

#Python no soporta arrays por lo que una opcion es usar list como lo mencionamos
#para usar el concepto de arrays se hace uso de la libreria numpy
import numpy as np

arreglo = np.array([1,2,3,4,5])
print(arreglo)
print(type(arreglo))

#Repitiendo el ejemplo con arrays
import random
import numpy as np

def llenadoArreglo(arreglo, n):
    for i in range (0,n):
        arreglo[i] = random.randint(1,99)

n = int(input("Digite el tamaño del vector: "))
#arreglo = np.zeros(n)  #inicializa el vector de n posiciones con 0
#print(arreglo)
arreglo = np.zeros(n, int)
print(arreglo)
llenadoArreglo(arreglo, n)
print(arreglo)
contPares = 0
contImpares = 0
for i in range(0,n):            #Se recorre el arreglo para saber si el numero es par o impar e incrementar el cont
    if arreglo[i] % 2 == 0:
        contPares = contPares+1
    else:
        contImpares = contImpares + 1

numerosPares = np.zeros(contPares)         #inicializar los vectores respectivos con la memoria necesaria
numerosImpares = np.zeros(contImpares)

contPares=0
contImpares=0
for i in range(0,n):
    if arreglo[i] % 2 == 0:
        numerosPares[contPares] = arreglo[i]
        contPares = contPares+1
    else:
        numerosImpares[contImpares] = arreglo[i]
        contImpares = contImpares + 1
print("Numeros pares: ",numerosPares)
print("Numeros impares: ",numerosImpares)