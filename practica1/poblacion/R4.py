#!/usr/bin/env python
# -*- coding: utf-8 -*-

import R2
import numpy as np
import funciones_html

"""
Ejercicio R4:

Generar una página web 3 (fichero variacionComAutonomas.html) con una tabla
con la variación de población por comunidades autónomas desde el año 2011 a
2017, indicando variación absoluta, relativa y desagregando dicha información
por sexos, es decir, variación absoluta (hombres, mujeres) y relativa
(hombres, mujeres). Para los cálculos, hay que actuar de manera semejante
que en el apartado R1.
"""

def var_pob_comunidades(fichero):
    """
    Funcion para calcular la variación de la población de las comunidades
    Aunque es la misma operación que en R1, no podemos utilizar la misma funcion
    ya que la tabla es distinta, al no ser de la poblacion total, si no
    de la total y la separada por hombres y mujeres
    """
    # leemos la informacion de las comunidades
    dicc_pob_com = R2.diccionario_pob_comunidades(fichero)

    dicc_var_com = {}

    # para las claves, las comunidades
    for clave in dicc_pob_com:
        # como forma tendrá 7 * 3 = 21 variaciones (total, hombres y mujeres)
        # y 21 * 2, porque son variaciones en total y en absoluto
        dicc_var_com[clave] = np.zeros(42)

        # utilizo un contador aparte porque tengo que ir saltando las
        # posiciones de 2010, ya que no puedo restar 2010 con nada
        contador_array = 0

        # variacion absoluta del total
        for i in range(7):
            dicc_var_com[clave][contador_array] = dicc_pob_com[clave][i] - dicc_pob_com[clave][i+1]
            contador_array += 1

        # variacion absoluta de hombres
        for i in range(8, 15):
            dicc_var_com[clave][contador_array] = dicc_pob_com[clave][i] - dicc_pob_com[clave][i+1]
            contador_array += 1

        # variacion absoluta de mujeres
        for i in range(16, 23):
            dicc_var_com[clave][contador_array] = dicc_pob_com[clave][i] - dicc_pob_com[clave][i+1]
            contador_array += 1

        # variacion relativa del total
        for i in range(7):
            dicc_var_com[clave][contador_array] = (dicc_var_com[clave][i] / dicc_pob_com[clave][i+1]) * 100
            contador_array += 1

        # variacion relativa de hombres
        # usamos i - 1 ya que al rellenar las varaciones, como saltamos el 2010
        # nos quedamos en la posicion 7, no en la 8
        for i in range(8, 15):
            dicc_var_com[clave][contador_array] = (dicc_var_com[clave][i - 1] / dicc_pob_com[clave][i+1]) * 100
            contador_array += 1

        # variacion relativa de mujeres
        # usamos i - 2 ya que al rellenar las varaciones, como saltamos el 2010
        # nos quedamos en la posicion 14, no en la 16
        for i in range(16, 23):
            dicc_var_com[clave][contador_array] = (dicc_var_com[clave][i - 2] / dicc_pob_com[clave][i+1]) * 100
            contador_array += 1

    return dicc_var_com



def main():

    # calculamos el diccionario con la variacion por comunidades
    fichero = "entradas/comunidadesAutonomas.htm"
    dicc_var_com = var_pob_comunidades(fichero)

    # lo escribimos a fichero al igual que otros ejercicios
    cabecera = ["Comunidad", "Abs. T2017", "Abs. T2016", "Abs. T2015","Abs. T2014","Abs. T2013","Abs. T2012","Abs. T2011","Abs. H2017","Abs. H2016","Abs. H2015","Abs. H2014","Abs. H2013","Abs. H2012","Abs. H2011","Abs. M2017","Abs. M2016","Abs. M2015","Abs. M2014","Abs. M2013","Abs. M2012","Abs. M2011","Rel. T2017", "Rel. T2016", "Rel. T2015","Rel. T2014","Rel. T2013","Rel. T2012","Rel. T2011","Rel. H2017","Rel. H2016","Rel. H2015","Rel. H2014","Rel. H2013","Rel. H2012","Rel. H2011","Rel. M2017","Rel. M2016","Rel. M2015","Rel. M2014","Rel. M2013","Rel. M2012","Rel. M2011"]

    ruta_resultado = "resultados/variacionComAutonomas.html"

    funciones_html.diccionario_a_tabla_html(ruta_resultado, dicc_var_com, "Variaciones por comunidad", "Resultados R4: Variaciones por comunidad", cabecera, css = "estilo.css")


if __name__ == "__main__":
    main()
