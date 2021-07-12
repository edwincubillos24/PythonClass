#Condicionales simples
"""== igual que True False
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que
!= diferente"""

#Programa que reciba un número e imprime si es par
numero = int(input("Digite el número: "))
if numero % 2 == 0:
    print("El número es par")

#Programa que reciba un número, imprima si es par o si es múltiplo de 3
numero = int(input("Digite el número: "))
if numero % 2 == 0:
    print(f'El número {numero} es par')
if numero % 3 == 0:
    print("El número es múltiplo de 3")

#Programa que reciba un número e imprime si ese número es par o si es impar
numero = int(input("Digite el número: "))
if numero % 2 != 0:
    print("El número es impar")
else:
    print("El número es par")

#Condiciones compuestas
""" and -> Y        true true = true
                    true false = false
                    false true = false
                    false false = false
    or -> O         true true = true
                    true false = true
                    false true= true
                    false false = false
    not ->          true = false
                    false = true"""

#Programa que reciba un número, imprima si es par y si es múltiplo de 3
numero = int(input("Digite el número: "))  #5
if numero % 2 == 0 and numero % 3 == 0:
    print("El número es par y también es múltiplo de 3")
else:
    print("El número no cumple la condición")

#Programa que reciba un número, imprima si es par o si es múltiplo de 3
numero = int(input("Digite el número: "))
if numero % 2 == 0 or numero % 3 == 0 :
    print(f'El número es par {numero%2==0} y el número es múltiplo de 3 {numero%3==0}')
else:
    print("El número no es par")
if numero % 3 == 0:
    print("El número es múltiplo de 3")
else:
    print("El número no es múltiplo de 3")

"""Realizar un programa que pida dos números enteros y muestre en pantalla el siguiente menú
CALCULADORA
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. DIVIDIR
5. SALIR
SELECCIONE UNA OPCION
El usuario debe digitar un número y el programa realiza el cálculo respectivo y muestra el resultado
en pantalla"""

#opcion 1
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
if opcion == 1:
    print("La suma es: ", numero1 + numero2)
if opcion == 2:
    print("La resta es: ", numero1 - numero2)
if opcion == 3:
    print("La multiplicación es: ", numero1 * numero2)
if opcion == 4:
    print("La división es: ", numero1 / numero2)
if opcion == 5:
    print("Hasta la vista")

#opcion 2 -> Condicionales anidados
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
if opcion == 1:
    print("La suma es: ", numero1 + numero2)
else:
    if opcion == 2:
        print("La resta es: ", numero1 - numero2)
    else:
        if opcion == 3:
            print("La multiplicación es: ", numero1 * numero2)
        else:
            if opcion == 4:
                print("La división es: ", numero1 / numero2)
            else:
                if opcion == 5:
                    print("Hasta la vista")
                else:
                    print("Opción invalida")

#opcion 3 elif
band = True
#ciclo inicio
numero1 = int(input("Digite el primer número: "))
numero2 = int(input("Digite el segundo número: "))
opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
if opcion == 1:
    print("La suma es: ", numero1 + numero2)
elif opcion == 2:
    print("La resta es: ", numero1 - numero2)
elif opcion == 3:
    print("La multiplicación es: ", numero1 * numero2)
elif opcion == 4:
    print("La división es: ", numero1 / numero2)
elif opcion == 5:
    print("Hasta la vista")
    band = False
else:
    print("Opción invalida")

