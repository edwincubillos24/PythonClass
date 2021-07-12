def entradaDatos():
    num1 = int(input("Digite el primer número: "))
    num2 = int(input("Digite el segundo número: "))
    return num1, num2

def mostrarMenu():
    opcion = int(input("CALCULADORA\n1.SUMAR\n2.RESTAR\n3.MULTIPLICAR\n4.DIVIDR\n5.SALIR\nSELECCIONE UNA OPCIÓN"))
    return opcion

def suma(numero1,numero2):
    suma = numero1 + numero2
    return suma

def resta(numero1,numero2):
    print("La resta es: ", numero1 - numero2)

def multiplicacion(numero1, numero2):
    print("La multiplicación es: ", numero1 * numero2)

def division(numero1, numero2):
    print("La división es: ", numero1 / numero2)

def imprimir():
    print("dta")