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


