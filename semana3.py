#Funciones - Definir funciones

def sumar():         #def palabra reservada que indica que estamos creando una función
    print(5+3)       #sumar es el nombre de la función

sumar()   #se debe crear primero la función primero y luego llamarla

#Funciones con parámetros

def sumar(num1, num2):
    print(num1 + num2 )

num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo número"))
sumar(num1, num2)

#Funciones que retorna valores

def sumar(num1, num2):
    suma = num1 + num2
    return suma

x = int(input("Digite el primer número"))
y = int(input("Digite el segundo numero"))
suma = sumar(x, y)          #opcion1
suma = sumar(num1=x, num2=y)#opcion2 permite mejor lectura de código
print(suma)

#Programa que calcule el máximo de dos números

def maximo(num1,num2):
    if num1 < num2:
        return num2
    else:
        return num1

num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo numero"))
suma = sumar(num1, num2)
print(suma)

#Parámetros por defecto
#Programa que lea 2 o 3 números y sume los números dígitados
def sumar(num1, num2, num3=0):
    suma = num1 + num2 + num3
    return suma

x = int(input("Digite el primer número"))
y = int(input("Digite el segundo numero"))
suma = sumar(x, y)
print("la suma es ", suma)
z = int(input("Digite el tercer número"))
suma = sumar(x,y,z)
print("la suma es ",suma)

#Python permite el retorno de varias variables
#Programa que calcule el cociente y el residuo de dos números por medio de una función
def division(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo

num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo numero"))
x, y = division(num1,num2)
print(F'El cociente es {x} y el residuo es {y}')

#Variables Globales y Locales Explicar

#Cuantas funciones se pueden utilizar?

"""Realizar un programa que pida dos números enteros por teclado y muestre en pantalla
el siguiente menú
CALCULADORA
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. DIVIDIR
5. SALIR

SELECCIONE UNA OPCIÓN
El usuario debe elegir una opción y el programa deberá mostrar el resultado en pantalla 
utilizar una función para cada uno """

def printMenu():
    opcion = int(input("CALCULADORA\n1. SUMAR\n2. RESTAR\n3. Multiplicar\n4. Dividir\n5. Salir"))
    return opcion

def sumar(num1, num2):
    print("La suma es: ",num1 + num2)

def restar(num1,num2):
    print("La resta es: ",num1 - num2)

def multiplicar(num1, num2):
    print("La multiplicación es: ",num1 * num2)

def dividir(num1, num2):
    print("La división es: ",num1 / num2)

while(True):
    opcion = printMenu()
    numero1 = int(input("Digite el primer número: "))
    numero2 = int(input("Digite el segundo número: "))    
    if (opcion == 1):
        sumar(numero1, numero2)
    elif (opcion == 2):
        restar(numero1, numero2)
    elif (opcion == 3):
        multiplicar(numero1, numero2) 
    elif (opcion == 4):
        dividir(numero1, numero2)
    elif (opcion == 5):
        print("Hasta la vista")
        break

    #con funciones externas

import functions

while(True):
    opcion = printMenu()
    numero1 = int(input("Digite el primer número: "))
    numero2 = int(input("Digite el segundo número: "))    
    if (opcion == 1):
        functions.sumar(numero1, numero2)
    elif (opcion == 2):
        functions.restar(numero1, numero2)
    elif (opcion == 3):
        functions.multiplicar(numero1, numero2) 
    elif (opcion == 4):
        functions.dividir(numero1, numero2)
    elif (opcion == 5):
        print("Hasta la vista")
        break


#Vectores
#Definción e inicialización de vectores 

vector = [0] * (10) #0 posiciones de 0 a 9
print(vector)

vector[2] = 4  #operación de asignación

print(vector[2]) #Acceder a un dato específico

#Y cual es la diferencia entre listas y vectores
#vector arreglo de una sola direccion, los datos son homogéneos: todos int, float
#       La forma en que se almacena en la memoria es consecutivo, uno tras otro
#listas son datos heterogéneos, float, int, string etc, en memoria los datos pueden
#       distribuidos
#Si quiero insertar un dato en la mitad de una lista solo se cambia una referencia en memoria y listo
#Si quiero insertar un dato en la mitad de un vector debo hacer corrimientos
#Si quiero recorrer y procesar datos es más óptimo vectores por que son consecutivos

#Realizar un programa qu