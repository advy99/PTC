#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 10:

Escribe una función es_inversa(palabra1, palabra2) que determine si una
palabra es la misma que la otra pero con los caracteres en orden inverso.
Por ejemplo 'absd' y 'dsba'.

"""


def es_inversa(palabra1, palabra2):
    """
    Funcion que dadas dos cadenas, comprueba si la primera es igual a la segunda
    invertida.
    """
    return palabra1 == palabra2[::-1]

# introducimos los datos
palabra1 = input("Introduce una palabra: ")
palabra2 = input("Introduce otra palabra: ")

son_inversas = es_inversa(palabra1, palabra2)

if son_inversas:
    print("La cadena {} invertida es equivalente a la cadena {}".format(palabra1, palabra2))
else:
    print("La cadena {} invertida NO es equivalente a la cadena {}".format(palabra1, palabra2))


