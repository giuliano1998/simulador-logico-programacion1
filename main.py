# Importamos funciones de puertas lógicas básicas (AND, OR, NOT)
from puertas_logicas import puerta_and, puerta_or, puerta_not

# Importamos funciones de puertas lógicas adicionales (XOR, NAND, NOR)
from puertas_extra import puerta_xor, puerta_nand, puerta_nor

# Importamos función que valida entrada del usuario (solo acepta 0 o 1)
from validacion import pedir_valor

# Importamos la función que genera tablas de verdad para distintas puertas
from tabla_verdad import generar_tabla

# Definimos el menú principal del programa
def menu():
    while True:  # Bucle que se repite hasta que el usuario elija salir
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Puerta AND")
        print("2. Puerta OR")
        print("3. Puerta NOT")
        print("4. Puerta XOR")
        print("5. Puerta NAND")
        print("6. Puerta NOR")
        print("7. Ver tabla de verdad")
        print("0. Salir")

        # Se pide al usuario que elija una opción
        opcion = input("Elegí una opción: ")

        # Opción 1: simular puerta AND
        if opcion == "1":
            a = pedir_valor("A")  # Pedimos valor A
            b = pedir_valor("B")  # Pedimos valor B
            print(f"Resultado AND: {puerta_and(a, b)}")  # Mostramos resultado

        # Opción 2: simular puerta OR
        elif opcion == "2":
            a = pedir_valor("A")
            b = pedir_valor("B")
            print(f"Resultado OR: {puerta_or(a, b)}")

        # Opción 3: simular puerta NOT
        elif opcion == "3":
            a = pedir_valor("A")
            print(f"Resultado NOT: {puerta_not(a)}")

        # Opción 4: simular puerta XOR
        elif opcion == "4":
            a = pedir_valor("A")
            b = pedir_valor("B")
            print(f"Resultado XOR: {puerta_xor(a, b)}")

        # Opción 5: simular puerta NAND
        elif opcion == "5":
            a = pedir_valor("A")
            b = pedir_valor("B")
            print(f"Resultado NAND: {puerta_nand(a, b)}")

        # Opción 6: simular puerta NOR
        elif opcion == "6":
            a = pedir_valor("A")
            b = pedir_valor("B")
            print(f"Resultado NOR: {puerta_nor(a, b)}")

        # Opción 7: generar tabla de verdad para operación lógica seleccionada
        elif opcion == "7":
            op = input("¿Qué operación? (and/or/not/xor/nand/nor): ").lower()
            generar_tabla(op)  # Llama a la función de tabla de verdad

        # Opción 0: salir del programa
        elif opcion == "0":
            print("¡Gracias por usar el simulador!")
            break  # Rompe el bucle y termina el programa

        # Cualquier otra opción se considera inválida
        else:
            print("Opción inválida. Intentá de nuevo.")

# Punto de entrada: ejecuta el menú solo si este archivo es el principal
if __name__ == "__main__":
    menu()
