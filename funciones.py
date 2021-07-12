#Funciones - Cómo se definen

def sumar():                #def es palabra reservada
    print(5+3)              #sumar es el nombre de la función

sumar()   #se debe crear la función antes de llamarla

#Funciones - Parámetros

def sumar(num1, num2):
    print(num1 + num2)

numero1 = int(input("Digite el primer número ")) #4
numero2 = int(input("Digite el segundo número ")) #5
sumar(numero1,numero2)#opcion1

sumar(num2 = numero2, num1 = numero1)   #opcion2, se especifica a que variable local le asigno que valor

#Funciones que retornan valores
def sumar(num1, num2):
    total = num1 + num2
    return total

x = int(input("Digite el primer número "))
y = int(input("Digite el segundo número "))
suma = sumar(x,y)
print(suma)

#funciones dentro de funciones
def resta(num1, num2):
    total = num1 - num2
    return total

def sumar(num1, num2):
    total = resta(2,3) + num2
    return total

x = int(input("Digite el primer número "))
y = int(input("Digite el segundo número "))
suma = sumar(x,y)
print(suma)

#Programa que calcule el número mayor de dos números
def mayor(num1, num2):
    if num1 < num2:
        return num2
    else:
        return num1

numero1 = int(input("Digite el primer número "))
numero2 = int(input("Digite el segundo número "))
if numero1 != numero2:
    numeroMayor = mayor(numero1,numero2)
    print("El número mayor es", numeroMayor)
else:
    print("Los números son iguales")

#Python permite retornar varias variables

#Programa que calcule el cociente y el residuo de dos números por medio de funciones
def division(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo

numero1 = int(input("Digite el primer número "))
numero2 = int(input("Digite el segundo número "))
if (numero2 == 0):
    print("Valor de divisor invalido no puede ser 0")
else:
    x, y = division(numero1, numero2)
    if y != 0:
        print(F'El cociente es {x}, el residuo es {y}')
    else:
        print(F'El cocinete es {x}')

"""Realizar un programa que pida dos números enteros y muestre en pantalla el siguiente menú
CALCULADORA
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. DIVIDIR
5. SALIR
SELECCIONE UNA OPCION
El usuario debe digitar un número y el programa realiza el cálculo respectivo y muestra el resultado
en pantalla"""

def entradaDatos():
    num1 = int(input("Digite el primer número: "))
    num2 = int(input("Digite el segundo número: "))
    return num1, num2

def mostrarMenu():
    opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
    return opcion

def suma(numero1,numero2):
    suma = numero1 + numero2
    return suma

def resta(numero1,numero2):
    print("La resta es: ", numero1 - numero2)

def multiplicacion(numero1, numero2):
    print("La multiplicación es: ", numero1 * numero2)

def division(numero1, numero2):
    print("La división es: ", numero1 / numero2)

while(True):
    numero1,numero2 = entradaDatos()
    opcion = mostrarMenu()
    if opcion == 1:
        total = suma(numero1,numero2)
        print ("la suma es ",total)
    elif opcion == 2:
        resta(numero1,numero2)
    elif opcion == 3:
        multiplicacion(numero1,numero2)
    elif opcion == 4:
        division(numero1,numero2)
    elif opcion == 5:
        print("Hasta la vista")
        break
    else:
        print("Opción invalida")

#Extrayendo las funciones a un archivo mathFunctions.py

import mathFunctions

while(True):
    numero1,numero2 = mathFunctions.entradaDatos()
    opcion = mathFunctions.mostrarMenu()
    if opcion == 1:
        total = mathFunctions.suma(numero1,numero2)
        print ("la suma es ",total)
    elif opcion == 2:
        mathFunctions.resta(numero1,numero2)
    elif opcion == 3:
        mathFunctions.multiplicacion(numero1,numero2)
    elif opcion == 4:
        mathFunctions.division(numero1,numero2)
    elif opcion == 5:
        print("Hasta la vista")
        break
    else:
        print("Opción invalida")



