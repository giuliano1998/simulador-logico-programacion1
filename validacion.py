# Este archivo define una función para pedir al usuario un valor binario (0 o 1)

# Función que pide y valida un valor ingresado
def pedir_valor(nombre):
    while True:  # Bucle que se repite hasta que la entrada sea válida
        try:
            # Pide al usuario ingresar un número (ej: A o B)
            valor = int(input(f"Ingresá el valor de {nombre} (0 o 1): "))

            # Verifica si es 0 o 1, si es válido lo devuelve
            if valor in [0, 1]:
                return valor
            else:
                print("Solo se permite 0 o 1.")  # Mensaje de error si no es 0 o 1

        except ValueError:
            # Si el usuario ingresa algo que no es número, muestra error
            print("Entrada inválida. Debe ser un número entero.")
