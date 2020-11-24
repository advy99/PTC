#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio R5:

Usando Matplotlib, para las 10 comunidades elegidas en el punto R3 generar un
gráfico de líneas que refleje la evolución de la población total de cada
comunidad autónoma desde el año 2010 a 2017, salvar el gráfico a fichero e
incorporarlo a la página web 3 del punto R4.
"""

import funciones_html
import matplotlib.pyplot as plt
import numpy as np
import R3
import R4

def grafica_avance_pob(fichero, salida):
    """
    Funcion para dado un fichero de entrada de comunidades y una ruta de salida
    genera una grafica de lineas del avance de las 10 comunidades más pobladas
    """

    # obtenemos la informacion de las comnidades, así como cual está más poblada
    pob_com, com_mas_pobladas = R3.com_mas_pobladas(fichero)

    # etiquetas para el eje X
    x_labels = [i for i in range(2010, 2018)]

    # ponemos el titulo y las etiquetas de los ejes
    plt.clf()
    plt.title("Evolución población de las 10 comunidades más pobladas", fontsize=10)
    plt.xlabel("Año")
    plt.ylabel("Población")

    # para las claves de las más pobladas
    for clave in com_mas_pobladas:
        # seleccionamos la poblacion total
        pob_total = pob_com[clave][:8]

        # le damos la vuelta, porque esta de 2017 a 2010
        # y lo vamos a dibujar de 2010 a 2017
        pob_total = pob_total[::-1]

        # dibujamos con puntos y lineas, para ver mejor los puntos en años concretos
        plt.scatter(x_labels, pob_total, label=clave)
        plt.plot(x_labels, pob_total)

    # ponemos la leyenda
    plt.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize = 5)

    # guardamos la figura, como la leyenda esta fuera, nos aseguramos que la
    # guarda en la imagen con el parametro bbox_inches
    plt.savefig(salida, bbox_inches = "tight", dpi = 600)



def main():

    # generamos la grafica con la funcion anterior
    fichero = "entradas/comunidadesAutonomas.htm"
    ruta_salida = "imagenes/R5.png"

    grafica_avance_pob(fichero, ruta_salida)

    # nos aseguramos que se ha ejecutado R4
    R4.main()

    # insertamos la imagen en el resultado de R4
    ruta_html = "resultados/variacionComAutonomas.html"

    funciones_html.insertar_imagen(ruta_html, "../imagenes/R5.png", 960, 540)



if __name__ == "__main__":
    main()


