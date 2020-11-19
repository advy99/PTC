#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funciones
import funciones_csv
import numpy as np


cabecera_nueva = "Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;"

diccionario_poblacion_provincias = funciones_csv.leer_csv_a_diccionario("entradas/poblacionProvinciasHM2010-17.csv", ";", "Total Nacional", "Notas", cabecera_nueva);

diccionario_solucion = {}

for clave in diccionario_poblacion_provincias:
    if clave != "Provincia":
        datos = diccionario_poblacion_provincias[clave]

        variaciones = []

        # los datos estan ordenados como T2017, ..., T2010
        for i in range(7):
            var_absoluta = float(datos[i]) - float(datos[i + 1])
            variaciones.append(var_absoluta)

        for i in range(7):
            var_relativa = ( float(datos[i]) / float(datos[i + 1]) ) * 100.0
            variaciones.append(var_relativa)

        diccionario_solucion[clave] = variaciones

ruta_resultado = "resultados/variacionProvincias.html"

cabecera = ["Provincia", "2017", "2016", "2015", "2014", "2013", "2012", "2011","2017", "2016", "2015", "2014", "2013", "2012", "2011"]

funciones.diccionario_a_tabla_html(ruta_resultado, diccionario_solucion, "Variaciones poblacion", "Resultados", cabecera, css = "estilo.css")


