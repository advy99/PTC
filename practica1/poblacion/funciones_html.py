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


def insertar_imagen_antes_tabla(fichero, ruta_imagen, x_img, y_img):
    entrada = open(fichero, "r", encoding = "utf-8")

    entrada_str = entrada.read()

    pos_tabla = entrada_str.find("<table>")

    salida_str = entrada_str[:pos_tabla]

    salida_str += "<img src=\"{}\" width=\"{}\" height=\"{}\" />".format(ruta_imagen, x_img, y_img)

    salida_str += entrada_str[pos_tabla:]

    entrada.close()

    salida = open(fichero, "w", encoding = "utf-8")

    salida.write(salida_str)
    salida.close()


def leer_td_html(fichero):
    entrada = open(fichero,"r", encoding = "utf-8" )

    entrada_str = entrada.read()

    soup = BeautifulSoup(entrada_str, "html.parser")

    celdas = soup.find_all("td")

    lista = []

    for celda in celdas:
        if celda.get_text() != "":
            lista.append(celda.get_text())

    return lista


def leer_comunidades(fichero):

    num_columnas = 2

    lista = leer_td_html(fichero)

    i = 0
    lista_final = []

    while i < len(lista):

        valor = ""

        for j in range(i, i + num_columnas):
            valor += lista[j]

        lista_final.append(valor)

        i += num_columnas


    return lista_final

def leer_comunidades_y_provincias(fichero, comunidades):

    lista = leer_td_html(fichero)
    #print(lista)

    lista_com_prov = []

    i = 0
    while i < len(lista):
        if lista[i] != "Ciudades    Autónomas:":
            lista_com_prov.append(lista[i] + " " + lista[i+1])
            lista_com_prov.append(lista[i + 2] + " " + lista[i+3])

            i += 4
        else:
            i += 1


    diccionario_prov = {}

    i = 0
    while i < len(lista_com_prov):
        clave = lista_com_prov[i+1]
        val = lista_com_prov[i]

        diccionario_prov[clave] = val

        i += 2

    return diccionario_prov



if __name__ == "__main__":
    print("Fichero con funciones para la p1")

