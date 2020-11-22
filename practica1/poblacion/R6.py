#!/usr/bin/env python
# -*- coding: utf-8 -*-

import funciones_html



def main():

    lista_claves = funciones_html.leer_tag_html("entradas/variacionProvincias2011-17.htm", "th")

    pos_inicio = lista_claves.index("Total Nacional")

    lista_claves = lista_claves[pos_inicio:]

    lista_valores = funciones_html.leer_tag_html("entradas/variacionProvincias2011-17.htm", "td")

    diccionario_var_html = {}

    i = 0
    for clave in lista_claves:
        diccionario_var_html[clave] = lista_valores[i:i + 14]
        i += 14

    for clave in diccionario_var_html:
        print(str(clave) + " " + str(diccionario_var_html[clave]) )




if __name__ == "__main__":
    main()
