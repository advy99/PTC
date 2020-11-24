#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fichero con funciones auxiliares sobre HTML, tanto de lectura como de escritura
a disco
"""


from bs4 import BeautifulSoup
import locale


def diccionario_a_tabla_html(ruta, diccionario, titulo, nombre_tabla, cabecera, css = ""):
    """
    Dada una ruta, un diccionario, el titulo, el nombre de la tabla, la cabecera
    a utilizar en la tabla y el fichero de estilo, pasar un diccionario a una
    tabla en HTML
    """

    # utilizamos la localización del sistema para escribir
    locale.setlocale(locale.LC_ALL,'')

    # abrimos el fichero
    fichero = open(ruta, "w", encoding = "utf-8")


    # insertamos la cabecera, con el titulo y el css, así como el cuerpo
    # con el nombre de la tabla
    pagina = """<!DOCTYPE html><html>
    <head><title>"""+ titulo + """</title>
    <link rel="stylesheet" href="  """ + css + """ ">
    <meta charset="utf8"></head>
    <body><h1>""" + nombre_tabla + """</h1>"""

    # añadimos el comienzo de la tabla
    pagina += """<p><table>
    <tr>"""

    # añadimos cada palabra de la cabecera como th
    for columna in cabecera:
        pagina += "<th>" + columna + "</th>"

    # finalizamos la primera fila de cabecera
    pagina += "</tr>"

    # para cada clave del diccionario, una linea nueva
    for clave in diccionario:
        # la primera columna será la clave
        pagina += "<tr><td>" + clave + "</td>"

        # las siguientes el valor asociado en el diccionario
        # en nuestro caso cada valor de un array de NumPy
        for val in diccionario[clave]:
            # lo formateamos para que de la salida como nos pedia el enunciado
            pagina += "<td>" + locale.format_string("%.2f", val, grouping = True) +  "</td>"

        # cerramos esa fila, y pasamos a la siguiente
        pagina += "</tr>"

    # cerramos el html
    pagina += "</table></p></body></html>"

    # escribimos el resultado y cerramos el fichero
    fichero.write(pagina)
    fichero.close()


def insertar_imagen(fichero, ruta_imagen, x_img, y_img, tag = "<table>"):
    """
    Función para dado un fichero, una ruta con una imagen, el tamaño de la imagen
    y una etiqueta, insertar la imagen dada justo antes de la etiqueta

    La etiqueta por defecto es <table>, ya que en mi caso siempre utilizaré esa
    etiqueta
    """

    # abrimos el fichero
    entrada = open(fichero, "r", encoding = "utf-8")

    # lo leemos
    entrada_str = entrada.read()

    # buscamos la etiqueta dada
    pos_tabla = entrada_str.find(tag)

    # añadimos a la salida lo anterior a la etiqueta
    salida_str = entrada_str[:pos_tabla]

    # añadimos la imagen
    salida_str += "<img src=\"{}\" width=\"{}\" height=\"{}\" />".format(ruta_imagen, x_img, y_img)

    # añadimos el resto de la web, etiqueta incluida
    salida_str += entrada_str[pos_tabla:]

    # cerramos el archivo de lectura
    entrada.close()

    """
    En este punto podriamos haber decidido utilizar el mismo open con 'rw' para
    hacer tanto lectura como escritura, pero prefiero separar las operaciones
    y no tener un buffer bidireccional abierto, de cara a evitar errores no
    intencionados
    """

    # lo abrimos para escritura
    salida = open(fichero, "w", encoding = "utf-8")

    # guardamos la nueva pagina, y cerramos
    salida.write(salida_str)
    salida.close()


def leer_tag_html(fichero, tag):
    """
    Dado un fichero en HTML y una etiqueta, leer el texto que aparece en dicha
    etiqueta todas las aparaciones en el fichero
    """

    # abrimos el fichero
    entrada = open(fichero,"r", encoding = "utf-8" )

    # lo leemos
    entrada_str = entrada.read()

    # utilizamos BautifulSoup para encontrar todas las etiquetas
    soup = BeautifulSoup(entrada_str, "html.parser")

    celdas = soup.find_all(tag)

    lista = []

    # para todas las apariciones, leemos el texto, a no ser que sea
    # la cadena vacia, que no nos interesa
    for celda in celdas:
        if celda.get_text() != "":
            lista.append(celda.get_text())

    return lista


def leer_comunidades(fichero):
    """
    Dado un fichero, leer las comunidades autonomas que aparecen

    Aunque sea un caso concreto, por problemas de forma concreta del archivo,
    me es más facil leer todos los de comunidades de la misma forma.
    """

    # los ficheros de comunidades tienen dos columnas, codigo y nombre
    num_columnas = 2

    # buscamos las etiquetas td en el fichero
    lista = leer_tag_html(fichero, "td")

    i = 0
    lista_final = []

    # mientras queden etiquetas
    while i < len(lista):

        valor = ""

        # juntamos el codigo con el nombre de comunidad
        for j in range(i, i + num_columnas):
            valor += lista[j]

        # aparece distinto en dos ficheros, asi que lo cambiamos para que
        # sean iguales
        if valor == "08 Castilla - La Mancha":
            valor = "08 Castilla-La Mancha"
        lista_final.append(valor)

        i += num_columnas


    return lista_final

def leer_provincias(fichero):
    """
    Dado un fichero leer las provincias de dicho fichero
    """

    lista = leer_tag_html(fichero, "td")

    lista_com_prov = []

    i = 0
    while i < len(lista):
        # de cada td leido tenemos cuatro valores
        # el cod. comunidad, la comunidad, el cod provincia y la provincia
        if lista[i] != "Ciudades    Autónomas:":
            # en la lista juntamos los codigos y los nombres
            lista_com_prov.append(lista[i] + " " + lista[i+1])
            lista_com_prov.append(lista[i + 2] + " " + lista[i+3])

            i += 4
        else:
            # parte de la tabla no es información, así que lo saltamos
            i += 1


    # introduciremos los resultados en un diccionario
    diccionario_prov = {}

    i = 0
    while i < len(lista_com_prov):
        # la clave será el segundo elemento, la provincia
        clave = lista_com_prov[i+1]
        # el calor será a que comunidad pertenece dicha provincia
        val = lista_com_prov[i]

        diccionario_prov[clave] = val

        i += 2

    return diccionario_prov



if __name__ == "__main__":
    print("Fichero con funciones para la p1")

