# Este archivo contiene las funciones para las puertas lógicas básicas: AND, OR y NOT

# Función para la puerta AND: devuelve 1 solo si ambos valores son 1
def puerta_and(a, b):
    return 1 if a == 1 and b == 1 else 0  # Usa un operador lógico para evaluar y devuelve el resultado

# Función para la puerta OR: devuelve 1 si al menos uno de los valores es 1
def puerta_or(a, b):
    return 1 if a == 1 or b == 1 else 0  # Devuelve 0 solo si ambos son 0

# Función para la puerta NOT: invierte el valor recibido
def puerta_not(a):
    return 1 if a == 0 else 0  # Si es 0 devuelve 1, si es 1 devuelve 0
