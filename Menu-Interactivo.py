suma = 's'
resta = 'r'
multiplicacion = 'm'
binario = 'b'
octal = 'o'
hexadecimal = 'h'

print ("MENU PRINCIPAL")
nombre = input("Ingrese su nombre ")
op_aritmetica = input(f"Hola {nombre}.¿Qué deseas hacer? ('s' Suma. 'r' Resta. 'm' Multiplicacion) ")
conversion = input("¿Qué tipo de conversión deseas hacer: ('b' binario. 'o' octal. 'h' hexadecimal )  ")
num1 = int(input("Ingresa el primer número entero "))
num2 = int(input("Ingresa el segunado número entero "))

if op_aritmetica == 's':
    resultado = num1 + num2
    operacion = "Suma"
elif op_aritmetica == 'r':
    resultado = num1 - num2
    operacion = "Resta"
elif op_aritmetica == 'm':
    resultado = num1 * num2
    operacion = "Multiplicación"

if conversion == 'b':
    print (f"El resultado de la {operacion} en binario es:  {bin(resultado) [2: ]}")
elif conversion == 'o':
     print (f"El resultado de la {operacion} en octal es:  {oct(resultado) [2: ]}")
elif conversion == 'h':
     print (f"El resultado de la {multiplicacion} en hexadecimal es:  {hex(resultado) [2: ]}")




















