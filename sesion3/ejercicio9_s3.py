#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 9:

Escribe una función elimina_vocales(palabra) que elimine todas las vocales
que aparecen en la palabra.

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

def elimina_vocales(palabra):

    vocales = "aeiouAEIOU"

    solucion = palabra

    # recorremos las vocales, eliminandolas de la solucion
    for vocal in vocales:
        solucion = eliminar_letras(solucion, vocal)

    return solucion

# introducimos los datos
palabra = input("Introduce una palabra: ")

sin_vocales = elimina_vocales(palabra)

print("La palabra introducida sin vocales es {}".format(sin_vocales))

print("\nUtilizando el metodo find de la clase str:")


