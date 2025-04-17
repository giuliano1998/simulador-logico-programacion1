# Función para pedir y validar un número binario como entero (0 o 1)
def pedir_numero_binario(nombre_variable):
    #Abrimos estructura repetitiva para que no se pueda avanzar hasta ingresar un valor valido
    while True:
        try:
            #Pedimos el valor de entrada definiendolo como int para que ya python controle una serie de valores de entrada
            entrada = int(input(f"Ingrese el valor del {nombre_variable} (solo 0 o 1): "))

            #Verificamos que el numero ingresado este en el rango deseado
            if entrada not in (0, 1):
                print("Error: Solo se permite ingresar 0 o 1.")
                continue

            print(f"El valor de {nombre_variable} es válido.")
            return entrada

        except ValueError:
            print("Error: Debe ingresar un número entero válido (0 o 1).")




