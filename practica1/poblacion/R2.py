#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funciones_html
import funciones_csv
import numpy as np

"""
Ejercicio R2:

Usando el listado de comunidades autónomas que podemos obtener del fichero
comunidadesAutonomas.html, así como de las provincias de cada comunidad
autónoma que podemos obtener de comunidadAutonoma-Provincia.html y los datos
de poblacionProvinciasHM2010-17.csv, hay que generar una página web 2
(fichero poblacionComAutonomas.html) con una tabla con los valores de
población de cada comunidad autónoma en cada año de 2010 a 2017, indicando
también los valores desagregados por sexos (de manera semejante a como
aparece en el fichero poblacionProvinciasHM2010-17.csv)
"""

def diccionario_pob_comunidades(fichero_comunidades):
    """
    Función para calcular la población total, de hombres y de mujeres de las
    comunidades dadas por un fichero
    """

    # leemos las comunidades del fichero dado
    comunidades = funciones_html.leer_comunidades(fichero_comunidades)

    # leemos los datos de las provincias
    provincias = funciones_html.leer_provincias("entradas/comunidadAutonoma-Provincia.htm")



    cabecera_nueva = "Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;"

    # leemos el csv de provincias
    diccionario_poblacion_provincias = funciones_csv.leer_csv_a_diccionario("entradas/poblacionProvinciasHM2010-17.csv", ";", "Total Nacional", "Notas", cabecera_nueva);

    diccionario_sol = {}

    # para todas las comunidades
    for comunidad in comunidades:
        # rellenamos con ceros la solucion

        # tenemos en cuenta un error en los html y csv dados - aparecen los
        # nombres que usamos como clave de distinta forma
        if comunidad == "08 Castilla - La Mancha":
            # aparece distinto en los documentos
            diccionario_sol["08 Castilla-La Mancha"] = np.zeros( (24,), np.float64) # 24 valores, 8 años * 3 separaciones
        else:
            diccionario_sol[comunidad] = np.zeros( (24, ), np.float64) # 24 valores, 8 años * 3 separaciones



    # para todas las claves, es decir, provincias
    for clave_pob_prov in diccionario_poblacion_provincias:
        # si la provincia actual no es la cabecera ni el total nacional
        if clave_pob_prov != "Provincia" and clave_pob_prov != "Total Nacional":
            # obtenemos la comunidad de la provincia actual
            comunidad = provincias[clave_pob_prov]

            # si la comunidad de la provincia actual está entre las comunidades
            # que queremos tener en cuenta
            if comunidad in comunidades:
                # sumamos la población de esa provincia a la comunidad
                diccionario_sol[comunidad] += diccionario_poblacion_provincias[clave_pob_prov].astype(np.float64)

    return diccionario_sol

def main():

    # calculamos la poblacion de las comunidades del fichero dado utilizando
    # la función anterior
    fichero = "entradas/comunidadesAutonomas.htm"

    diccionario_sol = diccionario_pob_comunidades(fichero)


    # escribimos el resultado en el fichero de resultados pedido
    cabecera = ["Comunidad", "T2017", "T2016", "T2015","T2014","T2013","T2012","T2011","T2010","H2017","H2016","H2015","H2014","H2013","H2012","H2011","H2010","M2017","M2016","M2015","M2014","M2013","M2012","M2011","M2010"]

    ruta_resultado = "resultados/poblacionComAutonomas.html"

    funciones_html.diccionario_a_tabla_html(ruta_resultado, diccionario_sol, "Poblaciones por comunidad", "Resultados R2 y R3: Población por comunidades", cabecera, css = "estilo.css")


if __name__ == "__main__":
    main()
