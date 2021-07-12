#Prueba 1

from clase_vector import Vector    #del archivo clase_vector importamos la clase Vector, esto trae sus atributos y metodos
import random

n = int(input("Digite el tamaño del vector: "))       #solicitamos tamaño del vector
v = Vector(n)                                       #se instancia el objeto de tipo Vector

#Prueba 2
v.construyeVector(n//2,100)    #se envía la cantidad de posiciones a utilizar y el limite superior

#Prueba 3
v.imprimeVector()

#Prueba 4
print("El tamaño del vector es ",v.tamagno())

#Prueba 5
print("La cantidad de posiciones utilizadas es: ",v.posicionesUsadas())

#Prueba 6
v.agregaDato(28)
v.imprimeVector("Prueba de agregar un dato")

#Prueba 7
v.asignaNumeroElementos(4)
v.imprimeVector("Prueba cambiar numero de elementos")

#Prueba 8
print("Quiero ver el dato de la posicion 3", v.retornaDato(3))

#Prueba 9
v.asignaDato(10,1)
v.imprimeVector("prueba de asignaDato")

#Prueba 10
print("El vector se encuetnra vacio? ", v.esVacio())

#Prueba 11
print("El vector se encuentra lleno? ", v.esLleno())