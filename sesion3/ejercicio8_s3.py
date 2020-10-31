#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 8:

Escribe una función inicio_fin_vocal(palabra) que determine si una palabra
empieza y acaba con una vocal.

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

def inicio_fin_vocal(palabra):
    """
    Funcion que comprueba su una palabra comienza y acaba por vocales
    """

    vocales = "aeiouAEIOU"

    # si la primera posicion y la ultima posicion es encontrada entre las
    # vocales, empieza y acaba por vocales
    empieza_y_acaba_por_vocal = buscar(vocales, palabra[0]) != -1 and buscar(vocales, palabra[-1]) != -1

    return empieza_y_acaba_por_vocal


# introducimos los datos
palabra = input("Introduce una palabra: ")

# probamos la funcion
solucion = inicio_fin_vocal(palabra)

if solucion:
    print("La palabra comienza y acaba por vocales")
else:
    print("La palabra no comienza y acaba por vocales")




print("\nUtilizando el metodo find de la clase str:")
vocales = "aeiouAEIOU"

if vocales.find(palabra[0]) != -1 and vocales.find(palabra[-1]) != -1:
    print("La palabra comienza y acaba por vocales")
else:
    print("La palabra no comienza y acaba por vocales")

