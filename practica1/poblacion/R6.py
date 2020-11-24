#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio R6:

Usando como entrada la página web 1 generada en el apartado 1 llamada
variacionProvincias.html y el fichero proporcionado variacionProvincias2011-17.html hay que
implementar un programa que compare los datos de variación de población de 2011 a 2017 (absoluta y
relativa) de ambos ficheros para comprobar que son los mismos valores en cada caso. Despúes usar el
fichero comunidadesAutonomasBis.html para generar una versión Bis de las páginas web 2 (ver R2
y R3) y web 3 (ver R4 y R5) con sus respectivos gráficos debiendo llamarse
poblacionComAutonomasBis.html y variacionComAutonomasBis.html respectivamente.
"""

import R1
import R2
import R3
import R4
import R5
import funciones_html
import numpy as np


def reales_iguales(a, b, epsilon = 0.005):
    """
    Función para comparar reales, para evitar problemas de representacion
    """
    return abs(a - b) < epsilon

def main():

    # leemos las claves
    lista_claves = funciones_html.leer_tag_html("entradas/variacionProvincias2011-17.htm", "th")

    # nos quedamos con las que pertenecen a datos, desde Total Nacional al final
    pos_inicio = lista_claves.index("Total Nacional")

    lista_claves = lista_claves[pos_inicio:]

    # leemos los valores, que están almacenados en td
    lista_valores = funciones_html.leer_tag_html("entradas/variacionProvincias2011-17.htm", "td")



    # para los valores, que están representados separados por puntos con miles
    # y los decimales con comas, los transformamos para poder hacer casting
    # al tipo float y poder trabajar con ellos
    for i in range(len(lista_valores)) :
        # lo ponemos en formato numerico, para poder pasarlo a float
        # no separamos los miles, y el separador de decimales es el . y no ,
        lista_valores[i] = lista_valores[i].replace(".","")
        lista_valores[i] = lista_valores[i].replace(",",".")


    diccionario_var_html = {}

    # guardamos los datos leidos del html en arrays de NumPy
    # constan de 14 valores
    i = 0
    for clave in lista_claves:
        diccionario_var_html[clave] = np.array(lista_valores[i:i + 14], np.float64)
        i += 14


    # leemos el diccionario de R1 y lo pasamos a un array de numpy
    diccionario_sol_R1 = R1.obtener_variacion()

    claves = []
    for clave in diccionario_sol_R1:
        diccionario_sol_R1[clave] = np.array(diccionario_sol_R1[clave], np.float64)
        claves.append(clave)


    # miramos si hay algun valor distinto
    son_iguales = True

    i = 0
    # para todas las claves
    while i < len(claves) and son_iguales:
        j = 0
        # para cada elemento de cada clave
        while j < len(diccionario_sol_R1[claves[i]]) and son_iguales:
            # miramos si son iguales
            son_iguales = reales_iguales(diccionario_sol_R1[claves[i]][j], diccionario_var_html[claves[i]][j])

            j += 1

        i += 1

    # mostramos el resultado en pantalla
    if son_iguales:
        print("R6: Todos los valores son iguales")
    else:
        print("R6: Hay algún valor distinto")




    # poblacion comunidades bis

    fichero_com = "entradas/comunidadesAutonomasBis.htm"

    # llamamos al metodo de R2
    dicc_pob_com_bis = R2.diccionario_pob_comunidades(fichero_com)

    # escribimos en un html el resultado
    cabecera = ["Comunidad", "T2017", "T2016", "T2015","T2014","T2013","T2012","T2011","T2010","H2017","H2016","H2015","H2014","H2013","H2012","H2011","H2010","M2017","M2016","M2015","M2014","M2013","M2012","M2011","M2010"]

    ruta_resultado = "resultados/poblacionComAutonomasBis.html"

    funciones_html.diccionario_a_tabla_html(ruta_resultado, dicc_pob_com_bis, "Poblaciones por comunidad bis", "Resultados R6: Población por comunidades bis", cabecera, css = "estilo.css")


    # generamos la grafica con el metodo de R3
    ruta_salida_fig = "imagenes/R3_bis.png"

    R3.grafica_mas_poblada(fichero_com, ruta_salida_fig)


    # la metemos en el fichero generado antes
    ruta_html = "resultados/poblacionComAutonomasBis.html"

    funciones_html.insertar_imagen(ruta_html, "../imagenes/R3_bis.png", 960, 540)



    # generamos el resultado utilizando el metodo de R4
    dicc_var_com = R4.var_pob_comunidades(fichero_com)

    # escribimos a un html el resultado
    cabecera = ["Comunidad", "Abs. T2017", "Abs. T2016", "Abs. T2015","Abs. T2014","Abs. T2013","Abs. T2012","Abs. T2011","Abs. H2017","Abs. H2016","Abs. H2015","Abs. H2014","Abs. H2013","Abs. H2012","Abs. H2011","Abs. M2017","Abs. M2016","Abs. M2015","Abs. M2014","Abs. M2013","Abs. M2012","Abs. M2011","Rel. T2017", "Rel. T2016", "Rel. T2015","Rel. T2014","Rel. T2013","Rel. T2012","Rel. T2011","Rel. H2017","Rel. H2016","Rel. H2015","Rel. H2014","Rel. H2013","Rel. H2012","Rel. H2011","Rel. M2017","Rel. M2016","Rel. M2015","Rel. M2014","Rel. M2013","Rel. M2012","Rel. M2011"]

    ruta_resultado = "resultados/variacionComAutonomasBis.html"

    funciones_html.diccionario_a_tabla_html(ruta_resultado, dicc_var_com, "Variaciones por comunidad", "Resultados R6: Variaciones por comunidad bis", cabecera, css = "estilo.css")



    # generamos la grafica con el metodo de R3
    ruta_salida_fig = "imagenes/R5_bis.png"


    R5.grafica_avance_pob(fichero_com, ruta_salida_fig)

    # la metemos en el fichero generado antes

    funciones_html.insertar_imagen(ruta_resultado, "../imagenes/R5_bis.png", 960, 540)


if __name__ == "__main__":
    main()
