#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 6:

Escribe una función vocales(palabra) que devuelva las vocales que aparecen
en la palabra.

"""

def buscar(palabra, sub):
    """
    Funcion para, dada una palabra, buscar la subcadena sub dentro de esta
    """

    # inicializamos las variables
    encontrado = False
    posicion = 0

    # mientras no lo encuentre, y nos quede palabra
    while not encontrado and posicion < len(palabra) - len(sub) + 1 :
        # probamos la posicion por la que vamos
        encontrado = palabra[posicion:(posicion+len(sub))] == sub

        # si todavia no lo hemos encontrado, avanzamos en la cadena
        if not encontrado:
            posicion += 1

    # si no lo ha encontrado devolvemos -1
    if encontrado == False:
        posicion = -1

    return posicion

def vocales(palabra):
    """
    Función que devuelve las vocales que aparecen en pantalla
    """

    vocales = "aeiouAEIOU"
    solucion = ""

    # recorremos las vocales
    for vocal in vocales:
        # si encontramos una vocal, la añadimos a la solucion
        if buscar(palabra, vocal) != -1:
            solucion += vocal + " "

    return solucion


# entrada de datos
palabra = input("Introduce una palabra: ")

vocales = vocales(palabra)

print("Se han encontrado las vocales {} en la palabra {}".format(vocales, palabra))





# hacemos lo mismo, pero con la funcion find de la clase str
vocales = "aeiouAEIOU"
solucion = ""

for vocal in vocales:
    if palabra.find(vocal) != -1:
        solucion += vocal + " "

print("\nUtilizando el metodo count de la clase str:")

print("Se han encontrado las vocales {} en la palabra {}".format(solucion, palabra))


