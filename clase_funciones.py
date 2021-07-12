def printMenu():
    opcion = int(input("CALCULADORA\n1. SUMAR\n2. RESTAR\n3. Multiplicar\n4. Dividir\n5. Salir"))
    return opcion

def sumar(num1, num2):
    print("La suma es: ",num1 + num2)

def restar(num1,num2):
    print("La resta es: ",num1 - num2)

def multiplicar(num1, num2):
    print("La multiplicación es: ",num1 * num2)

def dividir(num1, num2):
    print("La división es: ",num1 / num2)