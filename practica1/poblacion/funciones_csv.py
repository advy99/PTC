#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fichero con funciones auxiliares para leer y escribir ficheros csv
"""

import csv
import numpy as np


def limpiar_csv(fichero, separador, inicio, fin, cabecera):
    """
    Dado un fichero CSV, el separador utilizado, el inicio y el fin de la parte
    util y una cabecera, escribiremos a disco un fichero fichero_final.csv con
    solo la parte entre inicio y fin, añadiendo la cabecera
    """

    # abrimos el archivo en modo lectura
    archivo = open(fichero, "r", encoding="utf-8")

    # lo leemos
    archivo_str = archivo.read()

    # si inicio vale None, sera desde el comienzo
    if inicio == None:
        primero = 0
    else:
        # si no, buscamos la palabra de inicio
        primero = archivo_str.find(inicio)

    # si fin vale None, será hasta el final
    if fin == None:
        ultimo = len(archivo_str)
    else:
        # si no, buscamos el final
        ultimo = archivo_str.find(fin)

    # la seleccion será el intervalo de inicio a fin
    seccion_final = archivo_str[primero:ultimo]

    # nos quedamos sin la extensión del fichero
    nombre_fichero = fichero.split(".")

    # al nombre final será el nombre sin extension + _final.csv
    nombre_final = nombre_fichero[0] + "_final.csv"

    # abrimos el nuevo fichero como escritura
    ficheroFinal = open(nombre_final, "w",encoding="utf8")

    # si tiene cabecera la añadimos
    if cabecera != None:
        ficheroFinal.write(cabecera + '\n' + seccion_final)
    else:
        ficheroFinal.write(seccion_final)

    return nombre_final


def leer_csv_a_diccionario(fichero, separador, inicio = None, fin = None, cabecera = None):

    """
    Funcion para dado un archivo csv y el delimitador utilizado, pasar ese
    fichero a un diccionario. Es posible pasarle en que punto comenzar y
    acabar la lectura del CSV con los parámetros inicio y fin.
    """

    # si nos pasan inicio fin o una cabecera, limpiamos el fichero
    if inicio != None or fin != None or cabecera != None:
        fichero = limpiar_csv(fichero, separador, inicio, fin, cabecera)


    # pasamos lo leido a un diccionario
    diccionario_final = {}

    with open(fichero) as archivo_csv:
        # leemos del csv
        reader = csv.reader(archivo_csv,  delimiter = separador)
        # por cada linea
        for linea in reader:

            # la clave será el primer elemento
            clave = linea[0]

            # al tener un ; al final, hay un ultimo elemento vacio
            # lo dejamos fuera
            valor = np.array(linea[1:-1])

            diccionario_final[clave] = valor


    return diccionario_final

