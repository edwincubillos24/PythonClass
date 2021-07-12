#Objetivo crear una clase de nombre Vector con dos atributos: tamaño y un vector y vamos a definir
#una serie de métodos que hacen operaciones con ese vector
#Definir la clase Vector
import random

class Vector:
    def __init__(self,n):       #n es el tamaño del vector
        self.n = n
        self.v = [0]*(n+1)

    def construyeVector(self,m,r):      #m tamaño de los datos que voy a llenar, r rango máximo para números aleatorios
        self.v[0] = m                   #En la posición 0 debo almacenar la cantidad de datos que se usan
        for i in range(1, m+1):
            self.v[i] = random.randint(1,r)

#1. Un método que retorne la capacidad del arreglo V. tamagno(): retorna el valor del dato privado n.
    def tamagno(self):
        return self.n

#2. Un método que retorne el número de elementos en el vector. posicionesUsadas():
    # retorna el número de posiciones utilizadas, es decir, retorna V[0].

    def posicionesUsadas(self):
        return self.v[0]

#3. Un método para actualizar el número de elementos del vector. asignaNumeroElementos(m):
# actualiza el contenido de V[0].

    def asignarNumeroElementos(self,m):
        self.v[0] = m

#4. Un método que retorne el dato correspondiente a una posición dada. retornaDato(i): retorna el
# dato que se halla en la posición i de V.

    def retornaDato(self,i):
        return self.v[i]

#5. Un método que actualice el dato correspondiente a una posición dada. asignaDato(d, i): almacena
# el dato d en la posición i de V.

    def asignaDato(self,d,i):
        self.v[i] = d

#6. Un método para imprimir los datos del vector. imprimeVector(): recorre V mostrando el contenido de cada posición.
    def imprimeVector(self):
        for i in range(1,self.v[0]+1):
            print(self.v[i], end=",")

#7. Un método para determinar si el vector está vacío o no. esVacio(): retorna verdadero si V[0]
# es cero, falso de lo contrario.
    def esVacio(self):
        return self.v[0] == 0

#8. Un método para determinar si el vector está lleno o no. esLleno(): retorna verdadero si V[0]
# es igual a n, falso de lo contrario.
    def esLleno(self):
        return self.v[0] == self.n

#9 . Un método para insertar un dato al final del vector agregaDato(d): inserta el dato d a
# continuación del último dato en V.

    def agregarDato(self,d):
        if self.esLleno():
            print("No puede agregar mas datos, esta lleno")
        else:
            self.v[0] = self.v[0]+1
            self.v[self.v[0]] = d


