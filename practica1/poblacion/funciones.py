#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import locale


def diccionario_a_tabla_html(ruta, diccionario, titulo, nombre_tabla, cabecera, css = ""):

    locale.setlocale(locale.LC_ALL,'')
    fichero = open(ruta, "w", encoding = "utf-8")



    pagina = """<!DOCTYPE html><html>
    <head><title>"""+ titulo + """</title>
    <link rel="stylesheet" href="  """ + css + """ ">
    <meta charset="utf8"></head>
    <body><h1>""" + nombre_tabla + """</h1>"""

    pagina += """<p><table>
    <tr>"""

    for columna in cabecera:
        pagina += "<th>" + columna + "</th>"

    pagina += "</tr>"

    for clave in diccionario:
        pagina += "<tr><td>" + clave + "</td>"

        for val in diccionario[clave]:
            pagina += "<td>" + locale.format_string("%.2f", val, grouping = True) +  "</td>"

        pagina += "</tr>"

    pagina += "</p></body></html>"

    fichero.write(pagina)
    fichero.close()




if __name__ == "__main__":
    print("Fichero con funciones para la p1")

