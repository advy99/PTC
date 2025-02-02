#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import vrep
import tkinter
from tkinter import messagebox
from parametros import Parametros
import capturar
import glob
import sys
import agrupar
import caracteristicas
import clasificarSVM
import predecir

def salir():
    global id_cliente
    
    if id_cliente != -1:
        tkinter.messagebox.showwarning(title = "No puede salir", message = "Antes de salir debe cerrar la conexión con VREP")
    else:
        respuesta = tkinter.messagebox.askyesno(title = "Confirmación salir", message = "¿Está seguro de que quiere salir?")
        if respuesta:
            sys.exit()
            
def conectar_vrep():
    global id_cliente
    global boton_conectar
    global boton_desconectar
    global boton_capturar
    global etiqueta_estado
    
    vrep.simxFinish(-1)
    id_cliente = vrep.simxStart("127.0.0.1", 19999, True, True, 5000, 5)

    if id_cliente != -1:
        tkinter.messagebox.showinfo(title = "Conexión establecida",message = "Conexión con VREP establecida")
        boton_conectar["state"] = "disabled"
        boton_desconectar["state"] = "normal"
        boton_capturar["state"] = "normal"
        etiqueta_estado.configure(text = "Estado: Conectado a VREP")
    else:
        tkinter.messagebox.showerror(title = "Error iniciar simulador" ,message = "Debe iniciar el simulador")



def desconectar_vrep():
    global boton_conectar
    global boton_desconectar
    global boton_capturar
    global etiqueta_estado
    global id_cliente
    
    vrep.simxFinish(-1)

    id_cliente = -1
    boton_conectar["state"] = "normal"
    boton_desconectar["state"] = "disabled"
    boton_capturar["state"] = "disabled"

    etiqueta_estado.configure(text = "Estado: No conectado a VREP")

    tkinter.messagebox.showinfo(title = "Conexión cerrada",message = "Se ha desconectado de VREP")


def cambiar_parametros():
    global entrada_cerca
    global entrada_media
    global entrada_lejos
    global entrada_iteraciones
    global entrada_minpuntos
    global entrada_maxpuntos
    global entrada_umbral_distancia
    
    Parametros.iteraciones = int(entrada_iteraciones.get())
    Parametros.cerca = float(entrada_cerca.get())
    Parametros.media = float(entrada_media.get())
    Parametros.lejos = float(entrada_lejos.get())
    Parametros.min_puntos = float(entrada_minpuntos.get())
    Parametros.max_puntos = float(entrada_maxpuntos.get())
    Parametros.umbral_distancia = float(entrada_umbral_distancia.get())

    mensaje = """
    Nuevos parámetros:
    \tIteraciones: {}
    \tCerca: {}
    \tMedia: {}
    \tLejos: {}
    \tMinPuntos: {}
    \tMaxPuntos: {}
    \tUmbralDistancia: {}
    """.format(Parametros.iteraciones, Parametros.cerca, Parametros.media, Parametros.lejos, Parametros.min_puntos, Parametros.max_puntos, Parametros.umbral_distancia)

    print(mensaje)

    tkinter.messagebox.showinfo(title = "Actualizados parametros",message = mensaje)


def funcion_capturar():
    global lista_ficheros
    global id_cliente
    global ficheros_capturados
    global boton_agrupar


    seleccionados = lista_ficheros.curselection()

    if len(seleccionados) == 0:
        tkinter.messagebox.showwarning(title = "Seleccion erronea",message = "Debe elegir un fichero de la lista")
    else:
        archivo = lista_ficheros.get(seleccionados[0])

        respuesta = ""

        if os.path.isfile(archivo):
            respuesta = tkinter.messagebox.askyesno(title = "Confirmación sobreescribir fichero", message = "Se va a sobreescribir el fichero :\n {} ¿Estás seguro?".format(archivo))
        else:
            respuesta = tkinter.messagebox.askyesno(title = "Confirmación creación fichero", message = "Se va a crear el fichero :\n {} ¿Estás seguro?".format(archivo))

        if respuesta:
            es_positivos = archivo[0:3] == "pos"
            if es_positivos:
                capturar.capturar_positivos(archivo, id_cliente)
            else:
                capturar.capturar_negativos(archivo, id_cliente)

            ficheros_capturados.append(archivo)
            
            apariciones_unicas = [i for i in ficheros_capturados if ficheros_capturados.count(i) == 1]
            if len(apariciones_unicas) == 12:
                boton_agrupar["state"] = "normal"

                

def funcion_agrupar():
    global boton_agrupar
    global boton_extraer_caracteristicas
    
    agrupar.agrupar()
    
    boton_extraer_caracteristicas["state"] = "normal"
    
def funcion_entrenar_clasificador():
    global boton_entrenar
    global boton_predecir
    
    clasificarSVM.clasificar_piernas()
    
    boton_predecir["state"] = "normal"
    
    
def funcion_caracteristicas():
    global boton_entrenar
    
    caracteristicas.caracteristicas()
    
    boton_entrenar["state"] = "normal"

    
def funcion_predecir():
    global id_cliente
    
    predecir.predecir_escena(id_cliente)

def main():

    global root
    global boton_conectar
    global boton_desconectar
    global boton_capturar
    global boton_agrupar
    global boton_extraer_caracteristicas
    global boton_predecir
    global boton_entrenar
    global etiqueta_estado
    global entrada_iteraciones
    global entrada_cerca
    global entrada_media
    global entrada_lejos
    global entrada_minpuntos
    global entrada_maxpuntos
    global entrada_umbral_distancia
    global lista_ficheros
    global id_cliente
    global ficheros_capturados
    
    ficheros_capturados = []
    
    id_cliente = -1

    # creamos las carpetas, no pasa nada si existen
    for i in range(1, 7):
        os.makedirs("positivo" + str(i), exist_ok = True)
        os.makedirs("negativo" + str(i), exist_ok = True)
        
    os.makedirs("prediccion", exist_ok = True)

    root = tkinter.Tk()
    root.geometry("700x300")

    etiqueta_info = tkinter.Label(root, text = "Es necesario ejecutar el simulador VREP")
    etiqueta_info.grid(row = 0, column = 0)

    boton_conectar = tkinter.Button(root, text = "Conectar con VREP", command = conectar_vrep)
    boton_conectar.grid(row = 1, column = 0)

    boton_desconectar = tkinter.Button(root, text = "Detener y desconectar VREP", command = desconectar_vrep)
    boton_desconectar.grid(row = 2, column = 0)
    boton_desconectar["state"] = "disabled"


    etiqueta_estado = tkinter.Label(root, text = "Estado: No conectado con VREP")
    etiqueta_estado.grid(row = 3, column = 0)

    boton_capturar = tkinter.Button(root, text = "Capturar", command = funcion_capturar)
    boton_capturar.grid(row = 4, column = 0)
    boton_capturar["state"] = "disabled"

    boton_agrupar = tkinter.Button(root, text = "Agrupar", command = funcion_agrupar)
    boton_agrupar.grid(row = 5, column = 0)
    boton_agrupar["state"] = "disabled"

    boton_extraer_caracteristicas = tkinter.Button(root, text = "Extraer características", command = funcion_caracteristicas)
    boton_extraer_caracteristicas.grid(row = 6, column = 0)
    boton_extraer_caracteristicas["state"] = "disabled"

    boton_entrenar = tkinter.Button(root, text = "Entrenar clasificador", command = funcion_entrenar_clasificador)
    boton_entrenar.grid(row = 7, column = 0)
    boton_entrenar["state"] = "disabled"

    boton_predecir = tkinter.Button(root, text = "Predecir", command = funcion_predecir)
    boton_predecir.grid(row = 8, column = 0)
    boton_predecir["state"] = "disabled"

    boton_salir = tkinter.Button(root, text = "Salir", command = salir)
    boton_salir.grid(row = 9, column = 0)



    etiqueta_parametros = tkinter.Label(root, text = "Parámetros")
    etiqueta_parametros.grid(row = 1, column = 1)


    etiqueta_iteraciones = tkinter.Label(root, text = "Iteraciones:")
    etiqueta_iteraciones.grid( row = 2, column = 1)

    entrada_iteraciones = tkinter.Entry(root)
    entrada_iteraciones.grid(sticky = "E", row = 2, column = 2)
    entrada_iteraciones.insert(0, Parametros.iteraciones)


    etiqueta_cerca = tkinter.Label(root, text = "Cerca:")
    etiqueta_cerca.grid( row = 3, column = 1)

    entrada_cerca = tkinter.Entry(root)
    entrada_cerca.grid(sticky = "E", row = 3, column = 2)
    entrada_cerca.insert(0, Parametros.cerca)

    etiqueta_media = tkinter.Label(root, text = "Media:")
    etiqueta_media.grid( row = 4, column = 1)

    entrada_media = tkinter.Entry(root)
    entrada_media.grid(sticky = "E", row = 4, column = 2)
    entrada_media.insert(0, Parametros.media)

    etiqueta_lejos = tkinter.Label(root, text = "Lejos:")
    etiqueta_lejos.grid( row = 5, column = 1)

    entrada_lejos = tkinter.Entry(root)
    entrada_lejos.grid(sticky = "E", row = 5, column = 2)
    entrada_lejos.insert(0, Parametros.lejos)


    etiqueta_minpuntos = tkinter.Label(root, text = "MinPuntos:")
    etiqueta_minpuntos.grid( row = 6, column = 1)

    entrada_minpuntos = tkinter.Entry(root)
    entrada_minpuntos.grid(sticky = "E", row = 6, column = 2)
    entrada_minpuntos.insert(0, Parametros.min_puntos)

    etiqueta_maxpuntos = tkinter.Label(root, text = "MaxPuntos:")
    etiqueta_maxpuntos.grid( row = 7, column = 1)

    entrada_maxpuntos = tkinter.Entry(root)
    entrada_maxpuntos.grid(sticky = "E", row = 7, column = 2)
    entrada_maxpuntos.insert(0, Parametros.max_puntos)

    etiqueta_umbral_distancia = tkinter.Label(root, text = "UmbralDistancia:")
    etiqueta_umbral_distancia.grid( row = 8, column = 1)

    entrada_umbral_distancia = tkinter.Entry(root)
    entrada_umbral_distancia.grid(sticky = "E", row = 8, column = 2)
    entrada_umbral_distancia.insert(0, Parametros.umbral_distancia)

    boton_cambiar = tkinter.Button(root, text = "Cambiar", command = cambiar_parametros)
    boton_cambiar.grid(row = 9, column = 1)




    etiqueta_ficheros = tkinter.Label(root, text = "Fichero para la captura")
    etiqueta_ficheros.grid(row = 1, column = 3)

    lista_ficheros = tkinter.Listbox(root, width = 32, height = 12, selectmode = tkinter.SINGLE)
    lista_ficheros.insert(1, "positivo1/enPieCerca.json")
    lista_ficheros.insert(2, "positivo2/enPieMedia.json")
    lista_ficheros.insert(3, "positivo3/enPieLejos.json")
    lista_ficheros.insert(4, "positivo4/sentadoCerca.json")
    lista_ficheros.insert(5, "positivo5/sentadoMedia.json")
    lista_ficheros.insert(6, "positivo6/sentadoLejos.json")
    lista_ficheros.insert(7, "negativo1/cilindroMenorCerca.json")
    lista_ficheros.insert(8, "negativo2/cilindroMenorMedia.json")
    lista_ficheros.insert(9, "negativo3/cilindroMenorLejos.json")
    lista_ficheros.insert(10, "negativo4/cilindroMayorCerca.json")
    lista_ficheros.insert(11, "negativo5/cilindroMayorMedia.json")
    lista_ficheros.insert(12, "negativo6/cilindroMayorLejos.json")
    lista_ficheros.grid(row = 2, column = 3, rowspan = 12)



    root.mainloop()


if __name__ == "__main__":
    main()
