# Este archivo genera la tabla de verdad según el tipo de operación lógica elegida

# Importamos las funciones de puertas lógicas
from puertas_logicas import puerta_and, puerta_or, puerta_not
from puertas_extra import puerta_xor, puerta_nand, puerta_nor

# Función que genera e imprime la tabla de verdad
def generar_tabla(op):
    print(f"\nTabla de verdad para {op.upper()}")  # Muestra el título de la tabla

    # Si la operación es NOT, se usa solo una variable de entrada
    if op == "not":
        print("A | NOT")
        for a in [0, 1]:  # Solo recorre 0 y 1
            print(f"{a} | {puerta_not(a)}")  # Imprime resultado

    # Si es una operación binaria (2 entradas)
    else:
        print("A B | Resultado")
        for a in [0, 1]:
            for b in [0, 1]:
                # Llama a la función correspondiente según el tipo de puerta
                if op == "and":
                    r = puerta_and(a, b)
                elif op == "or":
                    r = puerta_or(a, b)
                elif op == "xor":
                    r = puerta_xor(a, b)
                elif op == "nand":
                    r = puerta_nand(a, b)
                elif op == "nor":
                    r = puerta_nor(a, b)
                else:
                    print("Operación no válida.")  # Control por si el usuario ingresa mal la operación
                    return
                # Muestra la combinación y su resultado
                print(f"{a} {b} | {r}")
