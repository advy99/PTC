#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sesion 1 - Ejercicio 2

Programa que pide la base y altura de un triangulo y muestra por pantalla
el area del triangulo

"""

# pedimos la base y la pasamos a float
base = input("Introduce la base del triangulo: ")
base = float(base)

# pedimos la altura y la pasamos a float
altura = input("Introduce la altura del triangulo: ")
altura = float(altura)

# el area es base * altura / 2
area = base * altura / 2


# mostramos el resultado
print("El area del triangulo es: {} ".format( area ))

