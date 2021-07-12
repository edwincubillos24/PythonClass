#Clases: POO
#moto:  marca : String, color : String, cilindraje : Int,  modelo : Int   -> Atributos
#       acelarar, frenar, pinchar, apagar, encerder -> Métodos o funciones

class Moto:
    pass        #indica que la clase no tiene atributos ni métodos y ya se puede utilizar

print(type(Moto))

##Con atributos
class Moto:                         #clase: modelo de un objeto de la vida real
    def __init__(self):
        self.marca = 'Auteco'
        self.color = 'Gris'
        self.cilindraje = 180
        self.modelo = 2021

moto1 = Moto()                      #objeto: Instancia de una clase
print(moto1.marca)
print(moto1.color)
print(moto1.cilindraje)
print(moto1.modelo)

#El usuario va a crear su inventario de motos
class Moto:
    def __init__(self,marca, color, cilindraje, modelo):
        self.marca = marca
        self.color = color
        self.cilindraje = cilindraje
        self.modelo = modelo

marca = input("Digite la marca de la moto: ")
color = input("Digite el color de la moto: ")
cilindraje = int(input("Digite el cilindraje de la moto: "))
modelo = int(input("Digite el modelo de la moto: "))
moto1 = Moto(marca, color, cilindraje, modelo)
print(f'La moto es de una marca {moto1.marca} color {moto1.color}, modelo {moto1.modelo} y cilindraje {moto1.cilindraje}')

#Realizar un programa que almacene los contactos telefonicos: nombre, fecha nac, telefono e email
class Contacto:
    def __init__(self,nombre, fechaNac, telefono, email):
        self.nombre = nombre            #atributos, características, propiedades
        self.fechaNac = fechaNac
        self.telefono = telefono
        self.email = email

    def mostrar_datos(self):            #funciones ó métodos
        print(f'nombre: {self.nombre}, fecha Nacimiento: {self.fechaNac}, telefono: {self.telefono}, email: {self.email}')

agenda = []
while(True):
    nombre = input("Digite el nombre del contacto")
    fechaNac = input("Digite la fechad de nacimiento")
    telefono = input("Digite el telefono")
    email = input("Digite el correo electrónico")
    contacto = Contacto(nombre, fechaNac, telefono, email)
    contacto.mostrar_datos()
    agenda.append(contacto)
    opcion = input("Desea adicionar otro contacto? s / n")
    if opcion == 'n':
        print("Hasta la vista")
        break
    for item in agenda:
        print(item.mostrar_datos())

#Ejercicio 7 Taller POO

class Peluchito:
    def __init__(self, nombre, cantidad, valor):
        self.nombre = nombre
        self.cantidad = cantidad
        self.valor = valor

    def mostrar_peluchito(self):
        print(f'Peluche: {self.nombre}, Cantidad: {self.cantidad}, Valor: {self.valor}')

def imprimirMenu():
    opcion = int(input("1.Agregar Peluche\n2.Buscar Peluche\n3.Eliminar Peluche\n4. Mostrar Inventario\n5. Realizar Venta\n6.Mostar Ganancia\n7.Salir"))
    return opcion

inventario = []
while(True):
    opcion = imprimirMenu()
    if opcion == 1:
        nombre = input("Digite el nombre del peluche: ")
        cantidad = int(input("Digite la cantidad de ese peluche: "))
        valor = int(input("Digite el valor de ese peluche: "))
        peluche = Peluchito(nombre=nombre, cantidad=cantidad, valor=valor)
        inventario.append(peluche)
    elif opcion == 2:
        nombreABuscar = input("Digite el nombre del peluche a buscar: ")
        existeElPeluche = False
        for peluche in inventario:
            if peluche.nombre == nombreABuscar:
                peluche.mostrar_peluchito()
                existeElPeluche = True
        if existeElPeluche == False:
            print("El peluche no existe")
    elif opcion == 3:
        nombreABuscar = input("Digite el nombre del peluche a eliminar: ")
        existeElPeluche = False
        for peluche in inventario:
            if peluche.nombre == nombreABuscar:
                confirmacion = input(F'Confirma que desea eliminar el peluche {peluche.nombre} s / n')
                if confirmacion == 's':
                    inventario.remove(peluche)
                existeElPeluche = True
        if existeElPeluche == False:
            print("El peluche no existe")
    elif opcion == 4:
        for peluche in inventario:
            peluche.mostrar_peluchito()
    elif opcion == 7:
        print("Hasta la vista Baby")
        break
    else:
        print("Opción Invalida")












