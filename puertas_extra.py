# Este archivo contiene funciones de puertas más avanzadas: XOR, NAND y NOR

# XOR: devuelve 1 si los valores son distintos
def puerta_xor(a, b):
    return 1 if a != b else 0

# NAND: devuelve el inverso de AND
def puerta_nand(a, b):
    return 0 if a == 1 and b == 1 else 1

# NOR: devuelve 1 solo si ambos valores son 0
def puerta_nor(a, b):
    return 1 if a == 0 and b == 0 else 0
