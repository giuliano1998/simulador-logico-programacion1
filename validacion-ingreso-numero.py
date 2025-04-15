# Función para pedir y validar un número binario como cadena
def pedir_numero_binario(nombre_variable):
    es_binario_valido = False

    while es_binario_valido == False:
        entrada = input(f"Ingrese el valor del {nombre_variable} (solo con 0 y 1): ")

        es_binario_valido = True

        for caracter in entrada:
            if not (caracter == '0' or caracter == '1'):
                es_binario_valido = False
                print("Error: Se ingresó un carácter no válido:", caracter)
                break

    print(f"El valor de {nombre_variable} es válido.")
    return entrada  # retornamos la cadena binaria tal cual

# Pedimos los dos números binarios como cadenas
num1 = pedir_numero_binario("num1")
num2 = pedir_numero_binario("num2")

# Mostramos los valores
print("Número 1 en binario:", num1)
print("Número 2 en binario:", num2)
