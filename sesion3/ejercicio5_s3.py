#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 5:

Escribe una función num_vocales(palabra) que devuelva el número de vocales
que aparece en la palabra.

"""


def num_vocales(palabra):
    """
    Función para contar el número de vocales en una palabra
    """

    vocales = 0

    # recorremos la palabra
    for letra in palabra:

        # si encontramos alguna vocal, sumamos uno al contador
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or \
           letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            vocales += 1

    return vocales



# entrada de datos
palabra = input("Introduce una palabra: ")

n_vocales = num_vocales(palabra)

print("Se han encontrado {} vocales en la palabra {}".format(n_vocales, palabra))


# copiamos la cadena en mayuscula
palabra_mayus = palabra.upper()

n_vocales = 0

vocales = "AEIOU"

# recorremos las vocales, contandolas
for letra in vocales:
    n_vocales += palabra_mayus.count(letra)


print("\nUtilizando el metodo count de la clase str:")
print("Se han encontrado {} vocales en la palabra {}".format(n_vocales, palabra))



