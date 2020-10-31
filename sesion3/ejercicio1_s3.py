#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 1:

Escribe una función contar_letras(palabra, letra) que devuelva el numero de
veces que aparece una letra en una palabra

"""


def contar_letras(palabra, letra):
    """
    Funcion para, dada una palabra, contar las apariciones de una letra dada
    """
    apariciones = 0

    # recorremos la palabra
    for caracter in palabra:
        # cada vez que encontramos un caracter que coincide con la letra
        # sumamos uno al contador
        if letra == caracter:
            apariciones += 1

    return apariciones



# entrada de datos
palabra = input("Introduce una palabra: ")
letra   = input("Introduce una letra: ")

# probamos la funcion
apariciones = contar_letras(palabra, letra)

print("En la palabra {}, la letra {} aparece {} veces".format(palabra, letra, apariciones))

# comparamos con el metodo count de str
apariciones = palabra.count(letra)

print("\nUtilizando el metodo count de la clase str:")
print("En la palabra {}, la letra {} aparece {} veces".format(palabra, letra, apariciones))

