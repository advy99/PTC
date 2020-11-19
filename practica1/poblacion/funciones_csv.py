#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import numpy as np


def limpiar_csv(fichero, separador, inicio, fin, cabecera):

    archivo = open(fichero, "r", encoding="utf-8")

    archivo_str = archivo.read()

    if inicio == None:
        primero = 0
    else:
        primero = archivo_str.find(inicio)

    if fin == None:
        ultimo = len(archivo_str)
    else:
        ultimo = archivo_str.find(fin)

    seccion_final = archivo_str[primero:ultimo]

    nombre_fichero = fichero.split(".")

    nombre_final = nombre_fichero[0] + "_final.csv"

    ficheroFinal = open(nombre_final, "w",encoding="utf8")

    if cabecera != None:
        ficheroFinal.write(cabecera + '\n' + seccion_final)
    else:
        ficheroFinal.write(seccion_final)

    return nombre_final


def leer_csv_a_diccionario(fichero, separador, inicio = None, fin = None, cabecera = None):

    """
    Funcion para dado un archivo csv y el delimitador utilizado, pasar ese fichero a un diccionario. Es posible pasarle en que punto comenzar y acabar la lectura del CSV con los parámetros inicio y fin.
    """

    if inicio != None or fin != None or cabecera != None:
        fichero = limpiar_csv(fichero, separador, inicio, fin, cabecera)


    diccionario_final = {}

    with open(fichero) as archivo_csv:
        reader = csv.reader(archivo_csv,  delimiter = separador)
        for linea in reader:

            provincia = linea[0]

            # al tener un ; al final, hay un ultimo elemento vacio
            # lo dejamos fuera
            poblacion = np.array(linea[1:-1])

            diccionario_final[provincia] = poblacion

            print(linea)
            print("\n\n")


    return diccionario_final

