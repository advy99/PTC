#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio R3:

Usando Matplotlib, para las 10 comunidades con más población media de 2010 a
2017, generar un gráfico de columnas que indique la población de hombres y
mujeres en el año 2017, salvar el gráfico a fichero e incorporarlo a la
página web 2 del punto R2.
"""

import funciones_html
import matplotlib.pyplot as plt
import numpy as np
import R2

def com_mas_pobladas(fichero, num_com = 10):
    """
    Dado un fichero de comunidades y un numero de comunidades, obtener
    las num_com comunidades más pobladas en media.
    """

    # utilizando la funcion de R2, leemos en un diccionario la información
    # de la poblacion de todas las comunidades
    diccionario_pob_comunidades = R2.diccionario_pob_comunidades(fichero)

    diccionario_pob_media_comunidades = {}

    # para todas las comunidades leidas
    for clave in diccionario_pob_comunidades:
        media = 0

        # calculamos la media de cada comunidad
        for i in range(8):
            media += diccionario_pob_comunidades[clave][i]

        media /= 8

        # almacenamos las medias
        diccionario_pob_media_comunidades[clave] = media

    # ordenamos el diccionario por el valor, no las claves
    com_pob_ordenadas = sorted(diccionario_pob_media_comunidades.items(), key=lambda x: x[1], reverse=True)

    mas_pobladas_media = []

    # añadimos a la lista el nombre de las más pobladas
    for i in range(num_com):
        mas_pobladas_media.append(com_pob_ordenadas[i][0])


    # devolvemos la información de todas las comunidades, así como las claves de
    # las más pobladas
    return diccionario_pob_comunidades, mas_pobladas_media



def grafica_mas_poblada(fichero, ruta_salida):
    """
    Funcion que dado un fichero de comunidades, y una ruta de salida, hace
    una grafica de barras con la población por hombres y mujeres
    de las 10 comunidades más pobladas
    """

    # buscamos las diez comunidades mas pobladas
    diccionario_pob_comunidades, mas_pobladas_media = com_mas_pobladas(fichero)

    grupos = np.arange( len(mas_pobladas_media) )

    pob_hombres = []
    pob_mujeres = []

    # guardamos la información de las más pobladas en el orden dado
    for comunidad in mas_pobladas_media:
        # como nos pide de 2017 por hombres y mujeres, los 8 primeros datos son
        # el total del 2017 al 2010, los siguientes 8 por hombres, y los 8
        # siguientes de mujeres. Queremos el valor en la novena posicion, el 8
        # que son los hombres de 2017, y el valor de la decimoseptima posicion
        # que son las mujeres de 2017
        pob_hombres.append(diccionario_pob_comunidades[comunidad][8])
        pob_mujeres.append(diccionario_pob_comunidades[comunidad][16])


    # hacemos el grafico
    ancho_barra = 0.35

    plt.clf()
    plt.title("Población por hombres y mujeres en 2017\n de las 10 comunidades más pobladas en media desde 2010 a 2017", fontsize = 8)


    plt.xlabel("Comunidades autonomas")
    plt.ylabel("Población en 2017")

    # ponemos un paso en y de 1e6, para que aparezca exacta la escala
    plt.yticks(np.arange(0, np.max(pob_mujeres), step = 1000000))

    # dibujamos por barras tanto los hombres como las mujeres
    plt.bar(grupos, pob_hombres, ancho_barra, color="orange", label="Hombres")
    plt.bar(grupos + ancho_barra, pob_mujeres, ancho_barra, color="c", label="Mujeres")


    # ponemos el paso en x al ancho de barra/2 para que aparezca enre las dos barras
    plt.xticks(grupos + ancho_barra/2, mas_pobladas_media, rotation = 10, fontsize = 4)
    plt.legend()

    # guardamos la figura en la ruta dada
    plt.savefig(ruta_salida, dpi = 400)

def main():

    # generamos la imagen con la función creada
    fichero = "entradas/comunidadesAutonomas.htm"

    ruta_salida_fig = "imagenes/R3.png"

    grafica_mas_poblada(fichero, ruta_salida_fig)

    # nos aseguramos que se ha ejecutado R2 ya que insertaremos ahi la imagen
    R2.main()

    ruta_html = "resultados/poblacionComAutonomas.html"

    # insertamos la imagen. Es importante que la ruta de la imagen sea relativa
    # a la ruta de donde está el html
    funciones_html.insertar_imagen(ruta_html, "../imagenes/R3.png", 960, 540)



if __name__ == "__main__":
    main()
