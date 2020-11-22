#!/usr/bin/env python
# -*- coding: utf-8 -*-

import R1
import funciones_html
import numpy as np


def reales_iguales(a, b, epsilon = 0.005):
    return abs(a - b) < epsilon

def main():

    lista_claves = funciones_html.leer_tag_html("entradas/variacionProvincias2011-17.htm", "th")

    pos_inicio = lista_claves.index("Total Nacional")

    lista_claves = lista_claves[pos_inicio:]

    lista_valores = funciones_html.leer_tag_html("entradas/variacionProvincias2011-17.htm", "td")



    for i in range(len(lista_valores)) :
        # lo ponemos en formato numerico, para poder pasarlo a float
        # no separamos los miles, y el separador de decimales es el . y no ,
        lista_valores[i] = lista_valores[i].replace(".","")
        lista_valores[i] = lista_valores[i].replace(",",".")


    diccionario_var_html = {}

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


    son_iguales = True


    i = 0
    while i < len(claves) and son_iguales:
        j = 0
        while j < len(diccionario_sol_R1[claves[i]]) and son_iguales:
            son_iguales = reales_iguales(diccionario_sol_R1[claves[i]][j], diccionario_var_html[claves[i]][j])

            if not son_iguales:
                print(str(claves[i]) + " " + str(j) )
                print( str(diccionario_sol_R1[claves[i]][j]) + " " + str(diccionario_var_html[claves[i]][j]) )
            j += 1

        i += 1

    if son_iguales:
        print("Todos los valores son iguales")
    else:
        print("Hay algún valor distinto")


if __name__ == "__main__":
    main()
