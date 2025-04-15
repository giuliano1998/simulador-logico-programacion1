# Paso 1) Definimos la funcion para la puerta AND
# La cual devuelve 1 solo si ambos valores (a y b) son 1 (true)
def puerta_and(a, b):
    return 1 if a == 1 and b == 1 else 0

# Paso 2) Definimos la funcion para la puerta OR
# La cual devuelve 1 si al menos uno de los valores (a o b) es 1 (true)
def puerta_or(a, b):
    return 1 if a == 1 or b == 1 else 0

# Paso 3) Definimos la función para la puerta NOT
# La cual invierte el valor: si es 0 devuelve 1, si es 1 devuelve 0
def puerta_not(a):
    return 1 if a == 0 else 0

# Paso 4) Creamos una función, la cual se usa para probar todas las funciones anteriores
# Imprime por pantalla los resultados de cada operación lógica
def pruebas():
    print("AND:")  # Título para la sección AND
    print("0 AND 0 =", puerta_and(0, 0))  # Imprime el resultado de 0 AND 0
    print("0 AND 1 =", puerta_and(0, 1))  # Imprime el resultado de 0 AND 1
    print("1 AND 0 =", puerta_and(1, 0))  # Imprime el resultado de 1 AND 0
    print("1 AND 1 =", puerta_and(1, 1))  # Imprime el resultado de 1 AND 1
    
    print("\nOR:")  # Salto de línea y título para sección OR
    print("0 OR 0 =", puerta_or(0, 0))    # Imprime el resultado de 0 OR 0
    print("0 OR 1 =", puerta_or(0, 1))    # Imprime el resultado de 0 OR 1
    print("1 OR 0 =", puerta_or(1, 0))    # Imprime el resultado de 1 OR 0
    print("1 OR 1 =", puerta_or(1, 1))    # Imprime el resultado de 1 OR 1

    print("\nNOT:")  # Salto de línea y título para sección NOT
    print("NOT 0 =", puerta_not(0))      # Imprime el resultado de NOT 0
    print("NOT 1 =", puerta_not(1))      # Imprime el resultado de NOT 1

# Esta línea se asegura de que las pruebas se ejecuten
# solo si el archivo se ejecuta directamente (no si se importa en otro)
if __name__ == "__main__":
    pruebas()