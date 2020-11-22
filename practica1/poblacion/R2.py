#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funciones_html
import funciones_csv
import numpy as np

def diccionario_pob_comunidades():

    comunidades = funciones_html.leer_comunidades("entradas/comunidadesAutonomas.htm")


    provincias = funciones_html.leer_comunidades_y_provincias("entradas/comunidadAutonoma-Provincia.htm", comunidades)



    cabecera_nueva = "Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010;"

    diccionario_poblacion_provincias = funciones_csv.leer_csv_a_diccionario("entradas/poblacionProvinciasHM2010-17.csv", ";", "Total Nacional", "Notas", cabecera_nueva);

    diccionario_sol = {}

    for comunidad in comunidades:
        if comunidad == "08 Castilla - La Mancha":
            # aparece distinto en los documentos
            diccionario_sol["08 Castilla-La Mancha"] = np.zeros( (24,), np.float64) # 24 valores, 8 años * 3 separaciones
        else:
            diccionario_sol[comunidad] = np.zeros( (24, ), np.float64) # 24 valores, 8 años * 3 separaciones

        #print(comunidad)


    for clave_pob_prov in diccionario_poblacion_provincias:
        if clave_pob_prov != "Provincia" and clave_pob_prov != "Total Nacional":
            comunidad = provincias[clave_pob_prov]

            #print(diccionario_sol[comunidad].astype(np.float64) )
            diccionario_sol[comunidad] += diccionario_poblacion_provincias[clave_pob_prov].astype(np.float64)

    return diccionario_sol

def main():

    diccionario_sol = diccionario_pob_comunidades()

    cabecera = ["Comunidad", "T2017", "T2016", "T2015","T2014","T2013","T2012","T2011","T2010","H2017","H2016","H2015","H2014","H2013","H2012","H2011","H2010","M2017","M2016","M2015","M2014","M2013","M2012","M2011","M2010"]

    ruta_resultado = "resultados/poblacionComAutonomas.html"

    funciones_html.diccionario_a_tabla_html(ruta_resultado, diccionario_sol, "Poblaciones por comunidad", "Resultados R2 y R3: Población por comunidades", cabecera, css = "estilo.css")


if __name__ == "__main__":
    main()
