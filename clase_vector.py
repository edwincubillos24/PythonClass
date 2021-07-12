#Objetivo crear una clase de nombre vector con dos atributos su tamaño y un arreglo (lista) y definir una serie de métodos
#que realizan operaciones comunes a los vectores

#1. Partiendo de lo aprendido en POO definimos la clase Vector

import random   #omitir inicialmente

class Vector:
    def __init__(self, n):
        self.n = n
        self.v = [0]*(n+1)              #Probar

#2. Vamos a crear un método que llene el vector con números aleatorios desde 1 hasta el valor dado por el usuario
    def construyeVector(self, m, r):        #m tamaño del vector, r rango máximo para los números aleatorios
        self.v[0] = m           #En la posición 0 se almacena el tamaño del vector
        for i in range (1, m+1):            #Empieza desde 1 porque en la posición 0 va el tamaño del vector
            self.v[i] = random.randint(1,r)  #Hay que importar la librería random

#3. Imprimir el vector
    def imprimeVector(self, mensaje="vector sin nombre:\t"):
        print("\n", mensaje, end =" ")
        for i in range(1,self.v[0]+1):
            print(self.v[i], end=",")
        print()

#4. Método que retorne el tamaño del vector
    def tamagno(self):
        return self.n

#5. Método que retorna la cantidad de posiciones utilizadas del vector v[0]
    def posicionesUsadas(self):
        return self.v[0]

#6. Método que agrega un dato al final OJO de los datos que se usan
    def agregaDato(self, dato):
        self.v[0] = self.v[0] + 1
        self.v[self.v[0]] = dato

#7. Asigna número de elementos
    def asignaNumeroElementos(self,m):
        self.v[0] = m

#8. Metodo que retorne el dato correspondiente a una posicion dada
    def retornaDato(self,i):
        return self.v[i]

#9. Metodo que actualice un dato se envia la posición y el dato
    def asignaDato(self,d,i):
        self.v[i] = d

#10 Método que determina  el vector esta lleno o
    def esVacio(self):
        return self.v[0] == 0

#10 Método para determinar si el vector esta lleno o no
    def esLleno(self):
        return self.v[0] == self.n

#11 Método que retorne la posición en la cual se halla un dato dado en el vector
    def buscarDato(self,d):
        i=1
        while i <= self.v[0] and self.v[i] != d:
            i = i + 1
        if i <= self.v[0]:
            return i
        return -1

# 12. Un método para buscar dónde insertar un dato en un
# vector ordenado ascendentemente. buscaDondeInsertar(d):
# retorna la posición en la cual debe quedar el dato d para que
# los datos de V continúen ordenados en forma ascendente.
    def buscaDondeInsertar(self,d):
        i = 1
        while i <= self.v[0] and self.v[i] < d:
            i = i + 1
        return i

#13. Un método para insertar un dato en una posición
#específica. insertar(d, i): inserta el dato d en la posición i de
#V. Recuerde que esto implica mover los datos de V.

    def insertar(self,d,i):
        if self.esLleno():
            print("\nVector lleno, no se puede insertar")
            return
        if i == 0:
            i = self.buscaDondeInsertar(d)  #busca donde se puede insertar para que quede de forma ascendente

