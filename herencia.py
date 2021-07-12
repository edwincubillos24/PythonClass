#Herencia
#Clase -> Abstracción - Modelo de un objeto de la vida real
# atributos -> Cualidades -> color, modelo, marca,
# y metodos -> Funciones o acciones ->

class Persona:                                          #Clase Padre
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def imprimirDatos(self):
        print(f'Nombre: {self.nombre}, edad: {self.edad}, telefono {self.telefono}')

class Empleado(Persona):                                         #Clase Hijo
    def __init__(self, nombre, edad, telefono, salario, empresa):
        super().__init__(nombre, edad, telefono)
        self.salario = salario
        self.empresa = empresa

    def imprimirDatosEmpleado(self):
        print(f'Salario: {self.salario}, Empresa: {self.empresa}')

class Estudiante(Persona):                                        #Clase Hijo
    def __init__(self, nombre, edad, telefono, carrera, universidad):
        super().__init__(nombre, edad, telefono)
        self.carrera = carrera
        self.universidad = universidad

    def imprimirDatosEstudiante(self):
        print(f'Carrera: {self.carrera}, Universidad: {self.universidad}')

empleado1 = Empleado (telefono = '3146561244', salario = 5000000, edad = 28 , empresa = 'Pragma', nombre = 'James')
empleado1.imprimirDatos()
empleado1.imprimirDatosEmpleado()

estudiante1 = Estudiante (telefono = '312456789', edad = 30, nombre = 'Juan', carrera = 'Sicología', universidad = 'Luis Amigo')
estudiante1.imprimirDatos()
estudiante1.imprimirDatosEstudiante()

#Ejemplo 2
#Ejercicio Definir una clase padre llamada vehículo y dos clases llamadas carro y bicicleta
#vehiculo - atributos: color, ruedas métodos: __init__
#coche - atributos: velocidad método: __init__
#bicicleta - atributos: tipo (urbana / montaña / ruta) __init__

class Vehiculo():
    def __init__(self,color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + " Ruedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

class Bicicleta(Vehiculo):
    def __init__(self,  color, ruedas, tipo):
        super().__init__(color,ruedas)
        self.tipo = tipo

vehiculo = Vehiculo("Rojo", 4)
print (vehiculo)
print(f'color: {vehiculo.color}, ruedas: {vehiculo.ruedas}')

coche = Coche ("Azul", 4, 200)
print(f'color: {coche.color}, ruedas: {coche.ruedas}, velocidad: {coche.velocidad} km/h')

bicicleta = Bicicleta("Negra", 2, "MTB")
print(f'color: {bicicleta.color}, ruedas: {bicicleta.ruedas}, tipo: {bicicleta.tipo}')

#Programa completo: Inventario de un supermercado
#Producto -> atributos: nombre, precio, marca, cantidad, fechaDeVencimiento
#Lacteos -> atributos: volumen, tipo (entero, deslactosado, descremado), presentacion (caja, bolsa, vaso)
#Detergente -> atributos: tipoDeUso (cocina, baño,ropa), presentacion (liquido, polvo, barra)
#Licores -> atributos: tipo (cerveza, whisky), origen (nacional, importando), porcentajeAlcohol

class Producto():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return "Nombre: " + self.nombre + ", Precio: " + str(self.precio) + ", Cantidad: " + str(self.cantidad)

class Lacteos(Producto):
    def __init__(self,nombre, precio, cantidad, volumen, tipo, presentacion):
        super().__init__(nombre, precio, cantidad)
        self.volumen = volumen
        self.tipo = tipo
        self.presentacion = presentacion

    def __str__(self):
        return super().__str__() + ", Volumen: " + str(self.volumen) + ", tipo: " + self.tipo + ", presentacion: " + self.presentacion

def imprimirMenu():
    opcion = int(input("1. Agregar Producto\n2. Buscar Producto\n3. Eliminar Producto\n4. Actualizar Producto\n5. Mostrar inventario\n6. Salir"))
    return opcion

lacteosList = []
detergentesList = []
licoresList = []
while (True):
    opcion = imprimirMenu()
    if opcion == 1:
        tipo = int(input("Seleccione el tipo de producto:\n1. Lacteo\n2. Detergente\n3. Licores"))
        if tipo == 1:  #Lacteo
            nombre = input("Digite el nombre")
            precio = int(input("Digite el precio"))
            cantidad = int(input("Digite la cantidad"))
            volumen = int(input("Digite el volumen"))
            tipo = input("Digite el tipo")
            presentacion = input("Digite la presentación")
            lacteo = Lacteos(nombre, precio, cantidad, volumen, tipo, presentacion)
            lacteosList.append(lacteo)
        elif tipo == 2: #Detergente
            nombre = input("Digite el nombre")
            precio = int(input("Digite el precio"))
            cantidad = int(input("Digite la cantidad"))

        elif tipo == 3: #Licor
            nombre = input("Digite el nombre")
            precio = int(input("Digite el precio"))
            cantidad = int(input("Digite la cantidad"))

    elif opcion == 5:   #Mostrar inventario
        print("-------------Lacteos--------")
        for lacteo in lacteosList:
            print(lacteo.__str__())
        print("-------------Detergentes--------")

        print("-------------Licores-------------")
    elif opcion == 6:
        print("Gracias totales")
        break
    else:
        print("Opción invalida")

#Herencia Multiple
class FigurasGeometricas:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def info(self):
        print("Soy Figura Geométrica")

figura = FigurasGeometricas(3,4)
figura.info()

class Color:
    def __init__(self,color):
        self.color = color

    def info(self):
        print("Soy un color")

color = Color ('Blue')
color.info()

class Cuadrado(FigurasGeometricas, Color):
    def __init__(self, alto, ancho, color):
        FigurasGeometricas.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def info(self):                     #Polimorfismo
        print("Soy un cuadrado")

    def info(self, palabra):                                    #Sobrecarga
        print(f'{palabra} Soy un cuadrado')

    def area(self):
        return self.alto * self.ancho

cuadrado = Cuadrado (4,6,'rojo')
print(cuadrado.alto)
print(cuadrado.ancho)
print(cuadrado.color)
cuadrado.info("Hola")

#Ejemplo Polimorfismo
class Animal:                       #Padre, Primaria, superclase
    def __init__(self,nombre):
        self.nombre = nombre

    def sonido(self):
        return "Error - las subclases son las que tienen sonido"

    def imprimirSonido(self):
        return self.sonido()

class Gato(Animal):             #Clase hija, subclase, derivada
    def __init__(self,nombre):
        super().__init__(nombre)

    def sonido(self):
        return "Miau Miau"

class Perro(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)

    def sonido(self):
        return "Guau Guau"

gatoConBotas = Gato("Jackie")
gatoFelix = Gato("Jackie")
perro1 = Perro("Cheese")

print(gato1.sonido())
print(perro1.sonido())
print(gato1.imprimirSonido())

animal = Animal("Pepe")
print(animal.sonido())
animal.imprimirSonido()










