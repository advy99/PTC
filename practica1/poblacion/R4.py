#!/usr/bin/env python
# -*- coding: utf-8 -*-

import R3
import numpy as np
import funciones_html

def main():
    dicc_pob_com, _ = R3.main()

    dicc_var_com = {}

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
            dicc_var_com[clave][contador_array] = (dicc_pob_com[clave][i] / dicc_pob_com[clave][i+1]) * 100
            contador_array += 1

        # variacion relativa de hombres
        for i in range(8, 15):
            dicc_var_com[clave][contador_array] = (dicc_pob_com[clave][i] / dicc_pob_com[clave][i+1]) * 100
            contador_array += 1

        # variacion relativa de mujeres
        for i in range(16, 23):
            dicc_var_com[clave][contador_array] = (dicc_pob_com[clave][i] / dicc_pob_com[clave][i+1]) * 100
            contador_array += 1


    cabecera = ["Comunidad", "Abs. T2017", "Abs. T2016", "Abs. T2015","Abs. T2014","Abs. T2013","Abs. T2012","Abs. T2011","Abs. H2017","Abs. H2016","Abs. H2015","Abs. H2014","Abs. H2013","Abs. H2012","Abs. H2011","Abs. M2017","Abs. M2016","Abs. M2015","Abs. M2014","Abs. M2013","Abs. M2012","Abs. M2011","Rel. T2017", "Rel. T2016", "Rel. T2015","Rel. T2014","Rel. T2013","Rel. T2012","Rel. T2011","Rel. H2017","Rel. H2016","Rel. H2015","Rel. H2014","Rel. H2013","Rel. H2012","Rel. H2011","Rel. M2017","Rel. M2016","Rel. M2015","Rel. M2014","Rel. M2013","Rel. M2012","Rel. M2011"]

    ruta_resultado = "resultados/variacionComAutonomas.html"

    funciones_html.diccionario_a_tabla_html(ruta_resultado, dicc_var_com, "Variaciones por comunidad", "Resultados R4: Variaciones por comunidad", cabecera, css = "estilo.css")

    return dicc_var_com

if __name__ == "__main__":
    main()
