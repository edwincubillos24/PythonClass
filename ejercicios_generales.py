#Leer un número entrero de tres digitos y determinar si al menos dos de sus tres digitos son iguales

num = int(input("Digite el numero de tres digitos"))
primerDigito = num//100
segundoDigito = (num // 10 ) % 10
tercerDigito = num % 10
