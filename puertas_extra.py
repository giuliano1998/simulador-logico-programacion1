"""
Programa que agrega puertas extra(xor,nand,nor).
"""

print("Puertas logicas extras")

a = int(input("Ingrese el primer bit (0): "))
b = int(input("Ingrese el segundo bit (1): "))

xor = a^b
nand = int(not (a and b))
nor = int(not (a or b))

print("Resultado de puertas logicas extras")
print(f"{xor}")
print(f"{nand}")
print(f"{nor}")