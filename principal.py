from Vector import Vector

n = int(input('Digite el tamaño del vector: '))
v = Vector(n)

v.construyeVector(n//2,100)

v.imprimeVector()

#Prueba del metodo 1
print("\nLa capacidad del vector es ",v.tamagno())

#Prueba del metodo 2
print("\nLas posiciones utilizadas del vector son: ",v.posicionesUsadas())

#Prueba del metodo 3
v.asignarNumeroElementos(3)

#Prueba del método 4
print("\nEl dato que esta en la posición 2 es: ",v.retornaDato(2))
v.imprimeVector()

#Prueba del método 5
v.asignaDato(24,3)
v.imprimeVector()

#prueba del método 7
print("\n El vector se encuentra vacio? ",v.esVacio())

#prueba del método 8
print("\n El vector se encuentra lleno? ",v.esLleno())

#prueba del método 9
v.agregarDato(30)
v.imprimeVector()