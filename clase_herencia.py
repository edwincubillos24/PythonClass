#Clase Padre Persona, tiene sus propias atributos y métodos ->  nombre y edad
#Clase Hija Empleado Hereda los atributos y métodos de la Clase Persona -> sueldo

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self,sueldo):
        self.sueldo = sueldo

empleado1 = Empleado(50000)
print(empleado1.nombre)                     #Se genera un error que nombre no es un atributo de Empleado

#corrección
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)      # metodo que permite acceder a los métodos de la clase padre
        self.sueldo = sueldo

empleado1 = Empleado('James',25,50000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#metodo str
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: {self.nombre} Edad: {self.edad}'      #sin este método imprime la posición en memoria

persona1 = Persona('Pedro','35')
print(persona1)

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)      # metodo que permite acceder a los métodos de la clase padre
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'

empleado1 = Empleado('Pedro', 35, 50000)
print(empleado1)

#Ejercicio Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo.
# La clase padre debe tener los siguientes atributos y métodos
# Vehiculo (Clase Padre): -Atributos (color, ruedas) -Métodos ( __init__() y __str__ )
# Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo): -Atributos ( velocidad (km/hr) ) -Métodos ( __init__() y __str__() )
# Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo): -Atributos ( tipo (urbana/montaña/etc ) -Métodos ( __init__() y __str__() )

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", Velocidad (km/hr): " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: " + self.tipo


vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)

coche = Coche("Azul", 4, 150)
print(coche)

bicicleta = Bicicleta("Blanca", 2, "Urbana")
print(bicicleta)

#Herencia Multiple
class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def info(self):
        print("Soy Figura Geométrica")

class Color:
    def __init__(self, color):
        self.color = color

    def info(self):
        print("Soy Color")

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def info(self):                     #Agregar al final del ejercicio
        print("Soy un cuadrado")

c1 = Cuadrado(4,6,"Rojo")
print(c1.ancho)
print(c1.color)
print(c1.area())
c1.info()

color = Color("Azul")
color.info()

figura = FiguraGeometrica(3,4)
figura.info()