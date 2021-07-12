#Colas con listas
#FIFO First In First Out

queue = []          #crear una cola vacia
queue.append('a')   #encolar
queue.append('b')
queue.append('c')
print(queue)
queue.pop(0)
print(queue)
queue.pop(0)
print(queue)

#Colas con Listas Enlazadas
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

    def agregarDato (self, d):
        x = nodoSimple(d) #cambio
        p = self.primerNodo()
        if p == None:
            self.primero = x
            self.ultimo = x
        else:
            self.ultimo.liga = x
            self.ultimo = x

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

#init: Crea una cola vacia con listas enlazadas
#encolar: Agregar un elemento como último en la cola.
#desencolar: Elimina el primer elemento de la cola y devuelve su valor, si la cola esta vacía muestra un mensaje

class ColaLSL(LSL):

    def __init__(self):         #init
        LSL.__init__(self)

    def encolar(self,d):        #encolar
        self.agregarDato(d)

    def desencolar(self):       #desencolar
        if self.esVacia():
            print('Cola vacía, no hay elementos para desencolar')
            return None
        d = self.primero.retornarDato()
        p = self.primerNodo()
        self.borrar(p)
        return d

a = ColaLSL()
print(f'Esta vacía la cola ? {a.esVacia()}')
a.encolar('a')
a.encolar('b')
a.encolar('c')
a.encolar('d')
d = a.desencolar()
print(f'Dato desencolado es {d}')




