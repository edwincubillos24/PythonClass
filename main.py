import math

print("Hola Python")
currentYear = 2021
PI = 3.1416
print("El año actual es:" + " " + str(currentYear), str(PI))
print(f"El año actual es {currentYear} y el valor de la constante es {PI}")

numero1 = 4
numero2 = 5
suma = numero1 + numero2
print(f'El valor de la suma es: {suma}')
resta = numero1 - numero2
print(f'El valor de la resta es: {resta}')
producto = numero1 * numero2
print(f'El producto es: {producto}')
div = 10 // 3 #división entera
print(f'La división es: {div}')
div = 10 / 3 #división normal
print(f'La división es: {div}')
modulo = 25 % 2
print(f'El módulo es: {modulo}')
potencia = 2 ** 3
print(f'El valor de la potencia es: {potencia}')

#raiz cuadrada
raiz = round(4 ** (1/2),2) #raiz con potencia
print(f'El valor de la raiz es: {raiz}')

raiz = pow(9,1/2) #raiz con pow
print(f'El valor de la raiz es: {raiz}')
raiz = math.sqrt(16) #raiz con funcion sqrt

print(f'El valor de la raiz es: {raiz}')

operacion1 = 5 + 2 - 9 ** 2 ** 2
print(f'El valor de la operacion es: {operacion1}')

# ( )
# **
# * /
# + -

#operadores de comparación <, >, ==, !=, <=, >=   True  False
variable = 3 == 5
print (f'la operación es {variable}')
print(type(variable))
variable = 3 == 3
print (f'la operación es {variable}')
variable = 9 >= 9
print (f'la operación es {variable}')

#1. Lea desde el teclado el nombre y la edad de cualquier persona e imprima tanto
#el nombre como la edad

#lectura de teclado
nombre = input("Digite su nombre: ")
edad = int(input("Digite su edad: "))
print("Su nombre es" + nombre + "y su edad es " + str(edad))
print (f'Su nombre es {nombre} y su edad es {edad} años')

#2. Lea dos números. Calcule la suma e imprima la suma y los dos números.

numero1 = int(input("Digite el primero número: "))  #entrada de información
numero2 = int(input("Digite el segundo número"))

suma = numero1 + numero2  #proceso de información

print(f'La suma de {numero1} con {numero2} es igual a {suma}') #salida de datos

"""#47 Escribir un programa para convertir una medida dada en pies a sus
equivalentes en:
1. Yardas
2. Pulgadas
3. Centímetros
4. Metros
(1 pie =12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54cm, 1m= 100cm). Leer el 
número de pies e imprimir el número de yardas, pies, pulgadas, centímetros y 
metros."""

pies = float(input("Digite la medida inicial en pies: "))
pulgadas = 12 * pies
print (f'La medida en pulgadas es {pulgadas}')

import math
a = 2
b = 9
c = 3
x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2*a)
print(x1)

numero1= int(input("Ingrese algún número:"))
numero2= int(input("Ingrese otro número: "))
resultado= numero1 + numero2
print("Su resultado es" + resultado)

numero1= int(input("Ingrese algún número:"))
numero2= int(input("Ingrese otro número: "))
resultado= numero1+ numero2
print(f'su resultado es {resultado}')


