#Definición de una clase

class Persona:
    pass            #indica que la clase no tiene nada mas, la crea y se puede utilizar

print(type(Persona))    #indica que es una clase <class 'type'>

#Una clase puede tener atributos: características de la clase 
#y métodos funciones de la clase o comportamientos 

class Persona:
    def __init__(self):     #init nos permite agregar atributos a una clase, self referencia al objeto que se va a crear
        self.nombre = 'Edwin'
        self.apellido = 'Cubillos'
        self.edad = 28                  #se crea una clase que siempre tendra esos datos con los que se inicializa

persona1 = Persona()        #por sintaxis no se pasa self el solo la toma
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

#Ejemplo 2
class Auto:
    def __init__(self):
        self.marca = 'Renault'      
        self.modelo = 2017
        self.color = 'Beige'

auto1 = Auto()              #nuevamente se crea con datos definidos
print(auto1.color)
print(auto1.marca)
print(auto1.modelo)

#Y si quiero crear una clase en la que pueda enviarle los atributos?
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona2 = Persona('Edwin','Cubillos',23)
print(persona2.nombre)
print(persona2.apellido)
print(persona2.edad)

#Solicitar estos datos al usuario
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

nombre = input("Digite el nombre")
apellido = input("Digite el apellido")
edad = int(input("Digite la edad"))
persona3 = Persona(nombre, apellido, edad)
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)

#Se pueden modificar los valores de los atributos una vez se han creado
persona3.nombre = input("Digite el nuevo nombre")
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)

#Y los métodos qué? son acciones que realizan los objetos en este caso imprimir datos
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_datos(self):
        print(f'{self.nombre} {self.apellido}, tiene {self.edad} años')

nombre = input("Digite el nombre")
apellido = input("Digite el apellido")
edad = int(input("Digite la edad"))
persona3 = Persona(nombre, apellido, edad)
persona3.mostrar_datos()

#Atributos dinámicos, se pueden adicionar atributos a un objeto pero solo quedarán en ese objeto y no la clase

telefono = input('Digite el numero de telefono')
persona3.telefono = telefono                            #solo pertenece a ese objeto
persona3.mostrar_datos()
print("Y el teléfono es ", persona3.telefono)


#Realizar un programa que realice las cuatro operaciones aritmeticas a dos numeros usando clases
class Aritmetica:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2 

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        print ('La multiplicación es ',self.num1 * self.num2)
    
    def dividir(self):
        print('La división es',self.num1 / self.num2)

num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo número"))
aritmetica1 = Aritmetica(num1, num2)
print(f'La suma es {aritmetica1.sumar()}')
print(f'la resta es {aritmetica1.restar()}')
aritmetica1.multiplicar()
aritmetica1.dividir()

#Ejercicio TiendaSoft V1.0

def imprimirMenu():
    opcion = int(input("1. Agregar Peluche\n2.Buscar Peluche\n3.Eliminar Peluche\n4. Mostrar Inventario\n5. Realizar Venta\n6. Mostrar Ganacias totales\n7.Salir"))
    return opcion

class Peluche:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

inventario = []
while(True):    
    opcion = imprimirMenu()
    if opcion == 1:
        nombre = input("Digite el nombre del peluche: ")
        cantidad = int(input("Digite la cantidad de peluches: "))
        precio = int(input("Digite el precio del peluche"))
        peluche = Peluche(nombre, cantidad, precio)
        inventario.append(peluche)
    elif opcion == 2:
        nombreABuscar = input("Digite el nombre del pelucha a buscar")
        for peluche in inventario:
            if peluche.nombre == nombreABuscar:
                print(f'El peluche {peluche.nombre} tiene {peluche.cantidad} y su precio es {peluche.precio}')
    elif opcion == 3:
        nombreABuscar = input("Digite el nombre del peluche a eliminar")
        for peluche in inventario:
            if peluche.nombre == nombreABuscar:
                print(f'Se encontró el peluche {peluche.nombre} con tiene {peluche.cantidad} y su precio es {peluche.precio}')
                eliminar = input("Desea eliminarlo s / n")
                if eliminar == 's':
                    inventario.remove(peluche)
                    print("Peluche eliminado de forma exitosa")
    elif opcion == 4:
        for peluche in inventario:
            print(f'El peluche {peluche.nombre} tiene {peluche.cantidad} y su precio es {peluche.precio}')   
    elif opcion == 7:
        print("Hasta la vista")
        break
