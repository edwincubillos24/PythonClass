#ciclos

#Realizar un programa que imprima los 5 primeros numeros naturales
print("1, 2, 3, 4, 5")

#Programa que imprima los 10 primeros números naturales
print("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")

#Programa que imprima los 100 primeros números naturales
contador = 1
while contador <= 100:  #i, j, k
    print(contador)
    contador += 1 #contador = contador + 1

#Programa que calcule el promedio de los primeros 100 números naturales
contador = 1        #contador
suma = 0            #acumulador
while contador <= 100:
    suma = suma + contador
    contador = contador + 1
promedio = suma / (contador - 1)
print("El promedio es igual a: ", promedio)

#Programa que solicite un número al usuario y se calcule el promedio desde el 1 hasta ese número dado
limite = int(input("Digite un número"))
suma = 0
i = 1
while i <= limite:
    suma = suma + i
    i = i + 1
promedio = suma / limite
print("El promedio es igual a : ", promedio)

#Realizar un programa que imprima los números pares que hay del 1 al 100
#opcion 1
import time
start_time = time.time()
contador = 1
while contador <= 10000:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1

print("--- %s seconds ---" % (time.time() - start_time))

#opcion2
import time
start_time = time.time()
contador = 2
while contador <= 10000:
    print(contador)
    contador = contador + 2
time = (time.time() - start_time)
print("--- %s seconds ---" % time)

#Programa que imprima los 100 primeros números naturales
contador = 1
while contador <= 100:  #i, j, k
    print(contador)
    contador += 1 #contador = contador + 1

#for

#for i in range(valorInicial, valorFinal, variación):
#instrucciones del ciclo

dato = int(input("Digite el valor máximo"))
for contador in range(4,dato+1,4):         # for (contador = 1; contrador <= 100; contador=contador+1)
    print(contador)                   #    print(contador)

#hacer un inventario de productos de una tienda donde reciba el nombre del producto y reciba la cantidad que hay
nombre = input("Digite el nombre del producto: ")
cantidad = int(input("Digite la cantidad disponible del producto: "))
print(f'Del producto {nombre} se tienen {cantidad} unidades')   #Almacena un solo producto

#solicitar varios productos el nombre y la cantidad
#opcion 1
rango = int(input("Digite la cantidad de productos"))
for i in range(rango):
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))
    print(f'Del producto {nombre} se tienen {cantidad} unidades')

#opcion 2
while True:
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))
    print(f'Del producto {nombre} se tienen {cantidad} unidades')
    continuar = input("Desea ingresar otro producto Digite 1 para si o 2 para no")
    if continuar == '2':
        break

#Estructuras de datos  ( ) , [ ] , { }
#listas [ ] corchetes
listado = [2, 3, 4, 5, 6, 3 , 4]
listado.sort()
print(listado)
print(listado[3])
print(len(listado)) #length tamaño

#Si quiero sumar los valores de esta lista
#opcion 1
suma = 0 #acumulador
i = 0 #contador de posicion no de valor
while i < len(listado):
    suma = suma + listado[i]
    i = i + 1

#opcion2
listado = [2, 3, 4, 5, 6, 3, 4]
suma = 0
for item in listado:
    suma = suma + item
print(suma)

listado = [2, 3, 4, 5, 6, 3, 4]
print(listado)
listado.append(6)
print(listado)
listado.remove(6)
print(listado)
print(dir(listado))

#tupla () parentesis  -> inmutable no puede cambiar  mutable o inmutable
datos = (2,3,4,5)
print(datos)
datos = (1,2,3,4)
print(datos)
list = list (datos)
list.append(8)
datos = tuple(list)
print(datos)


#Sets { } llaves -> Conjuntos
datos = {6, 4, 2, 1}
print(datos)
#print(datos[1])   #error no hay posiciones especificas
datos.add(8)
print(datos)
datos.remove(4)
print(datos)
datos.add(8)
print(datos)

if 2 in datos:
    print("El numero 2 si se encuentra en el conjunto")

datos = {6, 4, 2, 1}
datos2 = {5, 1, 3}
print(datos)
print(datos2)
comunes = datos.intersection(datos2)
print(comunes)
todos = datos.union(datos2)
print(todos)

#Diccionarios -> Es un par llave y valor
datos = {
    'nombre': 'Edwin',
    'apellido': 'Cubillos',
    'cedula': '12345678',
    'edad': 38
}
print(datos)

producto = {
    'nombre': 'fab',
    'cantidad': 2
}

#Agregar elementos al dicccionario
datos = {
    'nombre': 'Edwin',
    'apellido': 'Cubillos',
    'cedula': '12345678',
    'edad': 38
}
print(datos)
datos['correo'] = "edwin@gmail.com"
print(datos)

#imprimir un diccionario
for i in datos:  #imprime la llave
    print(i)

for i in datos.values():   #imprime el valor
    print(i)

for llave, valor in datos.items():  #imprime el par de llave y valor
    print(llave, " \t ", valor)

#hacer un inventario de productos de una tienda donde reciba el nombre del producto y reciba la cantidad que hay
inventario = []         #creamos una lista vacía
while True:             #ciclo infinito
    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad disponible del producto: "))

    producto = {           #creo mi diccionario
        'nombre': nombre,
        'cantidad': cantidad
    }

    inventario.append(producto)

    continuar = input("Desea ingresar otro producto Digite 1 para si o 2 para no")
    if continuar == '2':            #condicion para finalizar el ciclo
        break

for i in inventario:
    print("Del producto", i['nombre'], "usted tienen ",i['cantidad'], "unidades")

