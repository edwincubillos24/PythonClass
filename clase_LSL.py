class nodoSimple:
    def __init__(self, d = None):  #Se crea una variable y se le da el valor None porque no se le quiere asignar ningún valor no es NULL
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

class LSL:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def primerNodo(self):
        return self.primero

    def ultimoNodo(self):
        return self.ultimo

    def esVacia(self):
        return self.primero == None  #si es None es porque no se ha asignado nada y esta vacío

    def finDeRecorrido(self, p):
        return p == None        #recibe una posición y este retorna si es igual a None

    def recorrerLista(self):
        p = self.primerNodo()
        while not self.finDeRecorrido(p):
            print(p.retornarDato(), end=',')
            p = p.retornarLiga()

    def agregarDato(self,d):
        x = nodoSimple(d)
        p = self.primerNodo()
        if p == None:
            self.primero = x
            self.ultimo = x
        else:
            self.ultimo.liga = x
            self.ultimo = x

    def buscarDondeInsertar(self,d):
        p = self.primerNodo()
        y = None
        while not self.finDeRecorrido(p) and p.retornarDato() < d:
            y = p
            p = p.retornarLiga
        return y

    def insertar(self,d,y):
        x = nodoSimple(d)
        self.conectar(x,y)

    def conectar(self,x,y):
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

    def longitud(self):
        p = self.primerNodo()
        n = 0
        while not self.finDeRecorrido(p):
            n = n + 1
            p = p.retornarLiga()
        return n

    def buscarDato(self,d,y):
        x = self.primerNodo()
        while not self.finDeRecorrido(x) and x.retornarDato() != d:
            y.asignarDato(x)
            x = x.retornarLiga()
        return x

    def borrar(self, x, y= None):
        if x == None:
            print("Dato no está en la lista")
            return
        if y == None:
            if x != self.primero:
                print("Falta el anterior dato a borrar")
                return
            else:
                y = y.retornarDato()
            self.desconectar(x,y)

    def desconectar(self,x,y):
        if y == None:
            self.primero = x.retornarLiga()
            if self.esVacia():
                self.ultimo = None
            else:
                y.asignarLiga(x.retornarLiga())
                if x == self.ultimo:
                    self.ultimo = y


a = LSL()
for i in range(1,5):
    d = input("Entre dato: ")
    y = a.buscarDondeInsertar(d)
    a.insertar(d,y)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head

    def add(self, key):         #agregar al principio
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
            self.last  = nodo
        else:
            nodo.next = self.head
            self.head = nodo

    def append(self,key):
        nodo = Node(key)
        if not self.isEmpty():
            self.head = nodo
        else:
            self.last.next = nodo
            self.last = nodo

    def print(self):
        i = self.head
        while i:
            print(i.data, end=' -> ')
            i = i.next
        print()

ll = LinkedList()
ll.add(2)
ll.add(3)
ll.append(6)
ll.append(8)
ll.print()
