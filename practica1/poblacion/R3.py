#!/usr/bin/env python
# -*- coding: utf-8 -*-


import funciones_html
import matplotlib.pyplot as plt
import numpy as np
import R2

def com_mas_pobladas(fichero):

    diccionario_pob_comunidades = R2.diccionario_pob_comunidades(fichero)

    diccionario_pob_media_comunidades = {}

    for clave in diccionario_pob_comunidades:
        media = 0

        for i in range(8):
            media += diccionario_pob_comunidades[clave][i]

        media /= 8

        diccionario_pob_media_comunidades[clave] = media

    # ordenamos el diccionario
    com_pob_ordenadas = sorted(diccionario_pob_media_comunidades.items(), key=lambda x: x[1], reverse=True)

    mas_pobladas_media = []

    for i in range(10):
        mas_pobladas_media.append(com_pob_ordenadas[i][0])



    return diccionario_pob_comunidades, mas_pobladas_media



def grafica_mas_poblada(fichero, ruta_salida):
    diccionario_pob_comunidades, mas_pobladas_media = com_mas_pobladas(fichero)

    grupos = np.arange( len(mas_pobladas_media) )

    pob_hombres = []
    pob_mujeres = []

    for comunidad in mas_pobladas_media:
        pob_hombres.append(diccionario_pob_comunidades[comunidad][8])
        pob_mujeres.append(diccionario_pob_comunidades[comunidad][16])


    ancho_barra = 0.35

    plt.clf()
    plt.title("Población por hombres y mujeres en 2017\n de las 10 comunidades más pobladas en media desde 2010 a 2017", fontsize = 8)


    plt.xlabel("Comunidades autonomas")
    plt.ylabel("Población en 2017")

    plt.yticks(np.arange(0, np.max(pob_mujeres), step = 1000000))

    plt.bar(grupos, pob_hombres, ancho_barra, color="orange", label="Hombres")
    plt.bar(grupos + ancho_barra, pob_mujeres, ancho_barra, color="c", label="Mujeres")


    plt.xticks(grupos + ancho_barra/2, mas_pobladas_media, rotation = 10, fontsize = 4)
    plt.legend()


    plt.savefig(ruta_salida, dpi = 400)

def main():

    fichero = "entradas/comunidadesAutonomas.htm"

    ruta_salida_fig = "imagenes/R3.png"

    grafica_mas_poblada(fichero, ruta_salida_fig)

    # nos aseguramos que se ha ejecutado R2
    R2.main()

    ruta_html = "resultados/poblacionComAutonomas.html"

    funciones_html.insertar_imagen_antes_tabla(ruta_html, "../imagenes/R3.png", 960, 540)



if __name__ == "__main__":
    main()
