#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 4:

Escribe una función buscar(palabra, sub) que devuelva la posición
en la que se puede encontrar sub dentro de palabra o -1 en caso de que no esté

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



# entrada de datos
palabra = input("Introduce una palabra: ")
sub     = input("Introduce otra palabra (subcadena): ")

# probamos la funcion
posicion = buscar(palabra, sub)

if posicion != -1:
    print("{} encontrado en la posicion {}".format(sub, posicion))
else:
    print("{} no se ha encontrado en la palabra".format(sub))

# utilizamos el metodo de la str para comparar
posicion = palabra.find(sub)

print("\nUtilizando el metodo count de la clase str:")

if posicion != -1:
    print("{} encontrado en la posicion {}".format(sub, posicion))
else:
    print("{} no se ha encontrado en la palabra".format(sub))
