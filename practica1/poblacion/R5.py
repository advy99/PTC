#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funciones_html
import matplotlib.pyplot as plt
import numpy as np
import R3
import R4

def grafica_avance_pob(fichero, salida):
    pob_com, com_mas_pobladas = R3.com_mas_pobladas(fichero)

    x_labels = [i for i in range(2010, 2018)]

    plt.clf()
    plt.title("Evolución población de las 10 comunidades más pobladas", fontsize=10)
    plt.xlabel("Año")
    plt.ylabel("Población")

    for clave in com_mas_pobladas:
        # seleccionamos la poblacion total
        pob_total = pob_com[clave][:8]

        # le damos la vuelta, porque esta de 2017 a 2010
        # y lo vamos a dibujar de 2010 a 2017
        pob_total = pob_total[::-1]

        plt.scatter(x_labels, pob_total, label=clave)
        plt.plot(x_labels, pob_total)

    plt.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize = 5)


    plt.savefig(salida, bbox_inches = "tight", dpi = 600)



def main():

    fichero = "entradas/comunidadesAutonomas.htm"
    ruta_salida = "imagenes/R5.png"

    grafica_avance_pob(fichero, ruta_salida)

    R4.main()

    ruta_html = "resultados/variacionComAutonomas.html"

    funciones_html.insertar_imagen_antes_tabla(ruta_html, "../imagenes/R5.png", 960, 540)



if __name__ == "__main__":
    main()


