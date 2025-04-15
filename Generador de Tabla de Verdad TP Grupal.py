def mostrar_tabla_verdad(operacion):
    print("\nTabla de verdad para:", operacion.upper())
    print("A\tB\tResultado")

    for A in [True, False]:
        for B in [True, False]:
            if operacion == "and":
                resultado = A and B
            elif operacion == "or":
                resultado = A or B
            elif operacion == "not":
                # Para NOT, solo se mostrara A, B sera excluido
                print(f"{A}\t-\t{not A}")
                continue
            elif operacion == "xor":
                resultado = A != B
            elif operacion == "nand":
                resultado = not (A and B)
            elif operacion == "nor":
                resultado = not (A or B)
            else:
                print("Operación no válida.")
                return

            print(f"{A}\t{B}\t{resultado}")

# Menu que se le mostrara a el usuario antes de que ingrese un valor
print("Operaciones disponibles: AND, OR, NOT, XOR, NAND, NOR")
operacion = input("Ingresa la operación lógica que deseas usar: ").strip().lower()

mostrar_tabla_verdad(operacion)
