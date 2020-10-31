#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 2:

Escribe una función eliminar_letras(palabra, letra) que devuelva una versión
de palabra que no contiene el carácter letra ninguna vez.

"""


def eliminar_letras(palabra, letra):
    """
    Funcion para, dada una palabra, eliminar las apariciones de una letra dada
    """

    solucion = ""

    # recorremos la palabra
    for caracter in palabra:
        # cada vez que encontramos un caracter que no coincide con la letra
        # lo añadimos a la solucion
        if letra != caracter:
            solucion += caracter

    return solucion



# entrada de datos
palabra = input("Introduce una palabra: ")
letra   = input("Introduce una letra: ")

# probamos la funcion
sin_letra = eliminar_letras(palabra, letra)

print("La entrada era: {}, tras eliminar la letra: {} el resultado es: {}".format(palabra, letra, sin_letra))


# comparamos con el metodo count de str
sin_letra = palabra.replace(letra, '')

print("\nUtilizando el metodo count de la clase str:")
print("La entrada era: {}, tras eliminar la letra: {} el resultado es: {}".format(palabra, letra, sin_letra))
