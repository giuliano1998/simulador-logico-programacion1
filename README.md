# 🔌 Simulador de Puertas Lógicas + Generador de Tabla de Verdad

Este proyecto es un **simulador interactivo** desarrollado en Python que permite aplicar operaciones de lógica booleana básicas y avanzadas, así como generar automáticamente **tablas de verdad** para diferentes puertas lógicas.

Realizado como **trabajo práctico grupal** para la materia **Programación 1**.

---

## 🧠 ¿Qué hace este programa?

✅ Simula el comportamiento de las puertas lógicas:
- **Básicas**: AND, OR, NOT
- **Avanzadas**: XOR, NAND, NOR

✅ Permite al usuario:
- Ingresar valores binarios (0 o 1)
- Aplicar una operación lógica y ver su resultado
- Generar tablas de verdad completas para cualquier puerta lógica
- Interactuar fácilmente desde un **menú por consola**

---

## 📂 Estructura del Proyecto

 simulador-logico-programacion1/ 
 ├── main.py
 Punto de entrada del programa con menú interactivo ├── puertas_logicas.py 
 Funciones de puertas AND, OR, NOT ├── puertas_extra.py 
 Funciones de puertas XOR, NAND, NOR ├── validacion.py 
 Función para validar ingreso binario del usuario ├── tabla_verdad.py 
 Generador de tablas de verdad según operación ├── README.md 
 Documentación del proyecto

## ▶️ ¿Cómo usarlo?

### 🔹 Requisitos
Python 3 instalado en tu computadora

### 🔹 Instrucciones
1. Cloná el repositorio:
   ```bash
   git clone https://github.com/giuliano1998/simulador-logico-programacion1.git
   cd simulador-logico-programacion1

2. Ejecutá el programa principal:

python main.py

3. Seguí las instrucciones en pantalla para:

-Aplicar operaciones lógicas

-Ver resultados

-Generar tablas de verdad

# 🧪 Ejemplo de uso

--- MENÚ PRINCIPAL ---
1. Puerta AND
2. Puerta OR
3. Puerta NOT
...
Elegí una opción: 1
Ingresá el valor de A (0 o 1): 1
Ingresá el valor de B (0 o 1): 0
Resultado AND: 0

# 👥 Integrantes del grupo
-Giuliano Raschetti 
-Facundo Milano 
-Cristian Paolucci
-Lautaro Pez
-Estefania Nelson 

# Bibliografia 
-Material de Materia Programacion 1 y Matematica 1; UTN (https://tup.sied.utn.edu.ar/)
- [Documentación oficial de Python](https://docs.python.org/3/)
- [W3Schools - Python Operators](https://www.w3schools.com/python/python_operators.asp)
- [Programiz - Python Logical Operators](https://www.programiz.com/python-programming/operators#logical)
- [GeeksForGeeks - Logic Gates in Python](https://www.geeksforgeeks.org/logic-gates-in-python/)
- [Khan Academy - Lógica booleana y puertas lógicas](https://es.khanacademy.org/computing/computer-science/cryptography/logic-gates/a/logic-gates-review)
- Apuntes y contenidos de la cátedra de Programación 1


# Aclaracion Importante 
Realizacion del trabajo de manera grupal durante los encuentros sincronicos con aporte de todos los integrantes para un posterior push hacia la rama principal. 
Cual fue el aporte de cada integrante? 
-Giuliano Raschetti : Creacion de repositorio y puertas logicas.py.
-Facundo Milano : Creacion de validacion.py.
-Cristian Paolucci : Creacion de main.py.
-Lautaro Pez : Creacion de tabla_verdad.py
-Estefania Nelson : Creacion de puertas_extra.py

A nivel grupal se desarrollo la creacion del README con aporte en forma conjunta de la bibliografia ya adjuntada. 

