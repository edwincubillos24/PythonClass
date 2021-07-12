def funcion1():
    print("Ingreso por el método 1")
    x = 5 + funcion2()
    return x


def funcion2():
    print("Ingreso por el método 2")
    x = 3 + funcion3()
    return x


def funcion3():
    print("Ingreso por el método 3")
    x = 7
    return x


x = funcion1()
print(x)


def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


print( factorial(5) )

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)

print("\nElementos desencolados de la cola")
print(stack.pop())
print("\nDespués de eliminar los elementos")
print(stack)

#pilas con listas
class Pila:
    def __init__(self):
        self.arreglo=[]
    def apilar(self, x):
        self.arreglo.append(x)
    def desapilar(self):
        try:
            return self.arreglo.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    def es_vacia(self):
        return self.arreglo == []
    def muestraPila(self):
        for i in self.arreglo:
            print(i, end=", ")
        print()

p = Pila()
print("Es vacia?",p.es_vacia())
p.apilar(1)
print("Es vacia?",p.es_vacia())
p.muestraPila()
p.apilar(6)
p.apilar(4)
p.apilar(7)
p.muestraPila()
p.desapilar()
p.muestraPila()

#pilas usando LSL

#Nodo
class nodoSimple:
    def __init__(self, d = None):
        self.dato = d
        self.liga = None
    def asignarDato(self, d):
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

class pila(LSL):
    def __init__(self):
        LSL.__init__(self)

    def apilar(self, d):
        self.insertar(d)

    def muestraPila(self):
        self.recorrerLista()

    def desapilar(self):
        p = self.primerNodo()
        d = p.retornarDato()
        self.borrar(p)
        return d

a = pila()
a.apilar("a")
a.apilar("e")
a.apilar("i")
a.apilar("o")
a.recorrerLista()
b = a.esVacia()
print("\n Está vacía?", b)
d = a.desapilar()
print("\ndato desapilado", d)
a.recorrerLista()