#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio R1:
Calcular la variación de la población por provincias desde el año 2011 a 2017
en términos absolutos y relativos generando la página web 1 (que debe llamarse
variacionProvincias.html)
"""

import funciones_html
import funciones_csv
import numpy as np

def obtener_variacion():
    """
    Funcion para obtener la variación de población del fichero csv que pide el
    ejercicio
    """

    cabecera_nueva = "Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;"

    # leemos el csv
    diccionario_poblacion_provincias = funciones_csv.leer_csv_a_diccionario("entradas/poblacionProvinciasHM2010-17.csv", ";", "Total Nacional", "Notas", cabecera_nueva);

    diccionario_solucion = {}

    # para las distintas claves
    for clave in diccionario_poblacion_provincias:
        # si no es la cabecera
        if clave != "Provincia":
            # obtenemos los datos
            datos = diccionario_poblacion_provincias[clave]

            variaciones = []

            # los datos estan ordenados como T2017, ..., T2010, cogemos
            # los 8 primeros ya que queremos las absolutas
            for i in range(7):
                # calculamos la variacion absoluta
                var_absoluta = float(datos[i]) - float(datos[i + 1])
                variaciones.append(var_absoluta)

            # calculamos la vaciación relativa
            for i in range(7):
                var_relativa = ( float(variaciones[i]) / float(datos[i + 1]) ) * 100.0
                variaciones.append(var_relativa)

            # añadimos los resultados al diccionario
            diccionario_solucion[clave] = variaciones

    return diccionario_solucion

def main():

    # llamamos a la funcion creada
    diccionario_solucion = obtener_variacion()

    # la escribimos en fichero con la función de HTML dada
    ruta_resultado = "resultados/variacionProvincias.html"

    cabecera = ["Provincia", "Abs. 2017", "Abs. 2016", "Abs. 2015", "Abs. 2014", "Abs. 2013", "Abs. 2012", "Abs. 2011","Rel. 2017", "Rel. 2016", "Rel. 2015", "Rel. 2014", "Rel. 2013", "Rel. 2012", "Rel. 2011"]

    funciones_html.diccionario_a_tabla_html(ruta_resultado, diccionario_solucion, "Variaciones poblacion", "Resultados R1: Variaciones por provincia", cabecera, css = "estilo.css")



if __name__ == "__main__":
    main()
