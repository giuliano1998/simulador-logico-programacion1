#Se define opraciones y conversiones válidas
suma = 's'
resta = 'r'
multiplicacion = 'm'
binario = 'b'
octal = 'o'
hexadecimal = 'h'

#Se imprime por pantalla título del menú interactivo
print ("MENU PRINCIPAL")

#Se solicita a usuario el ingreso de su nombre
nombre = input("Ingrese su nombre ")

#Se saluda y concatena nombre a usuario, y se solicita que operación aritmética desea
op_aritmetica = input(f"Hola {nombre}.¿Qué deseas hacer? ('s' Suma. 'r' Resta. 'm' Multiplicacion) ")

#Se solicita a usuario que ingrese tipo de conversión
conversion = input("¿Qué tipo de conversión deseas hacer: ('b' binario. 'o' octal. 'h' hexadecimal )  ")

#Se requiere a usuario que ingrese dos números
num1 = int(input("Ingresa el primer número entero "))
num2 = int(input("Ingresa el segunado número entero "))

#Se verifica operación aritmética elegida y se calcula resultado
if op_aritmetica == 's':
    resultado = num1 + num2
    operacion = "Suma"
elif op_aritmetica == 'r':
    resultado = num1 - num2
    operacion = "Resta"
elif op_aritmetica == 'm':
    resultado = num1 * num2
    operacion = "Multiplicación"
#Si usuario ingresa operación inválida
else:
    print("Operación aritmética no válida")

#Se calcula resultado sin prefijo, para mostrar por pantalla solo el número, pero aclarando que tipo de conversión se hizo 

#Conversión a binario y resultado se imprime por pantalla
if conversion == 'b':
    print (f"El resultado de la {operacion} en binario es:  {bin(resultado) [2: ]}")
#Conversión a octal y resultado se imprime por pantalla
elif conversion == 'o':
     print (f"El resultado de la {operacion} en octal es:  {oct(resultado) [2: ]}")
#Conversión a hexadecimal y resultado se imprime por pantalla. Se utiliza función upper() para que hexadecimal salga con mayúscula
elif conversion == 'h':
     print (f"El resultado de la {operacion} en hexadecimal es:  {hex(resultado) [2: ].upper()}")
#Si usuario ingresa opción para conversión no válida
else:
    print ("Tipo de conversión no es válida")



















