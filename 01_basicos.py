"""Sesión 1 — Elementos básicos del lenguaje (A.1.1)

    Tipos básicos de datos (int, float, str, bool), constantes y variables, input(), print().
    Operadores aritméticos, de comparación y lógicos; expresiones y f-strings.
    Comentarios y estilo PEP 8.
    Práctica: "Ficha de bienvenida": pedir nombre y saldo inicial y mostrarlos formateados.
    Producto: 01_basicos.py."""

nombre = input ("Escribe tu nombre: ")
apellido = input ("Escribe tu apellido: ")
saldo = float(input ("Ingrese su saldo incial: "))

print(f"Nombre: (nombre)")
print(f"Apellido: (apellido)")
print(f"Saldo inicial: (saldo)")




print(f"Bienvenido {nombre} {apellido} su saldo {saldo:.2f}€")