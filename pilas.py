def funcion1():
    x = 5 + funcion2()          #L2
    print("ingreso por el método 1")
    return x

def funcion2():
    x = 3 + funcion3()          #L3
    print("Ingreso por el método 2")
    return x

def funcion3():
    print("Ingreso por el método 3")
    x = 7
    return x

x = funcion1()  #L1
print (x)

#Recursión
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

factorial(5)

#Pilas con listas
stack = []          #crear una pila vacía
stack.append('a')   #apilar
stack.append('e')
stack.append('i')
print(stack)
stack.pop()         #Desapilar
print(stack)
stack.pop()
print(stack)

#Clase Pila ->
#init: Inicializar una pila nueva y vacia
#apilar: Agrega un elemento a la pila
#desapilar: Elimina el tope de la pila y lo devuelve (El elemento que se devuelve siempre es el último que se agrego)
#imprimirPila: Recorre la pila y muestra los datos
#estaVacia: Devuelve True o False según la pila este vacía o este llena

class Pila:
    def __init__(self):
        self.arreglo = []           #init

    def apilar(self,x):             #apilar
        self.arreglo.append(x)

    def desapilar(self):
        self.arreglo.pop()

    def imprimirPila(self):
        for i in self.arreglo:
            print(i, end=",")
        print()

    def estaVacia(self):
    #    return len(self.arreglo) == 0   opcion1
        return self.arreglo == []       #opcion2

p=Pila()
print(p.estaVacia())
p.imprimirPila()
p.apilar(4)
p.imprimirPila()
p.apilar(5)
p.imprimirPila()
p.desapilar()
p.imprimirPila()
print(p.estaVacia())

#Pilas usando la clase ListasEnlazadas
#Retomamos el codigo de la clase de ListasEnlazadas

#Nodo
class nodoSimple:
    def __init__(self, d = None):
        self.dato = d
        self.liga = None        #puntero o conector al siguiente nodo
    def asignarDato(self, d):           #setters y getters
        self.dato = d
    def asignarLiga(self, x):
        self.liga = x
    def retornarDato(self):
        return self.dato
    def retornarLiga(self):
        return self.liga

#Clase LSL
class LSL:
    def __init__(self): #Constructor
        self.primero = None
        self.ultimo = None

    def insertar (self, d, y=None): #cambio
        x = nodoSimple(d) #cambio
        self.conectar(x, y)

    def conectar (self, x, y):
        if y == None:
            if self.primero == None:
                self.ultimo = x
            else:
                x.asignarLiga(self.primero)
            self.primero = x
            return
        x.asignarLiga(y.retornarLiga())
        y.asignarLiga(x)
        if y == self.ultimo:
            self.ultimo = x

    def primerNodo (self):
        return self.primero

    def finDeRecorrido (self, p):
        return p == None

    def esVacia (self):
        return self.primero == None

    def recorrerLista (self):
        p = self.primerNodo()
        while not self.finDeRecorrido(p):
            print(p.retornarDato(), end = ", ")
            p = p.retornarLiga()

    def borrar (self, x, y = None):
        if x == None:
            print("Dato no está en la lista")
            return
        if y == None:
            if x != self.primero:
                print("Falta el anterior del dato a borrar")
                return
        else:
            y = y.retornarDato()
        self.desconectar(x,y)

    def desconectar(self, x, y):
        if y == None:
            self.primero = x.retornarLiga()
            if self.esVacia():
                self.ultimo = None
        else:
            y.asignarLiga(x.retornarLiga())
            if x == self.ultimo:
                self.ultimo = y

#init: Inicializar una pila nueva y vacia
#apilar: Agrega un elemento a la pila
#desapilar: Elimina el tope de la pila y lo devuelve (El elemento que se devuelve siempre es el último que se agrego)
#imprimirPila: Recorre la pila y muestra los datos
#estaVacia: Devuelve True o False según la pila este vacía o este llena

class PilaLSL(LSL):

    def __init__(self):         #init
        LSL.__init__(self)

    def apilar(self,d):         #apilar
        self.insertar(d)

    def imprimirPila(self):     #imprimir
        self.recorrerLista()

    def desapilar(self):
        p = self.primerNodo()
        d = p.retornarDato()
        self.borrar(p)
        return d

a = PilaLSL()
a.apilar('a')
a.apilar('e')
a.apilar('i')
a.recorrerLista()
a.desapilar()
a.recorrerLista()

#Crear un programa que muestre un menú donde el usuario pueda seleccionar entre:
#1. Apilar
#2. Desapilar
#3. Imprimir el contenido de la pila
#0. Salir

