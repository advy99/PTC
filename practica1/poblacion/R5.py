#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funciones_html
import matplotlib.pyplot as plt
import numpy as np
import R3

def main():

    fichero = "entradas/comunidadesAutonomas.htm"
    pob_com, com_mas_pobladas = R3.com_mas_pobladas(fichero)

    x_labels = [i for i in range(2010, 2018)]

    plt.clf()
    plt.title("Evolución población de las 10 comunidades más pobladas")
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

    plt.legend(bbox_to_anchor=(1,1), loc="upper left", fontsize=7)


    plt.show()




if __name__ == "__main__":
    main()


