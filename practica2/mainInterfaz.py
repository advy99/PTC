#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import vrep
import tkinter
from tkinter import messagebox
from parametros import Parametros

def conectar_vrep():
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
    vrep.simxFinish(-1)

    boton_conectar["state"] = "normal"
    boton_desconectar["state"] = "disabled"
    boton_capturar["state"] = "disabled"

    etiqueta_estado.configure(text = "Estado: No conectado a VREP")

    tkinter.messagebox.showinfo(title = "Conexión cerrada",message = "Se ha desconectado de VREP")


def cambiar_parametros():
    Parametros.iteraciones = entrada_iteraciones.get()
    Parametros.cerca = entrada_cerca.get()
    Parametros.media = entrada_media.get()
    Parametros.lejos = entrada_lejos.get()
    Parametros.min_puntos = entrada_minpuntos.get()
    Parametros.max_puntos = entrada_maxpuntos.get()
    Parametros.umbral_distancia = entrada_umbral_distancia.get()

    print("Nuevos parámetros:")
    print("\tIteraciones: ", Parametros.iteraciones)
    print("\tCerca: ", Parametros.cerca)
    print("\tMedia: ", Parametros.media)
    print("\tLejos: ", Parametros.lejos)
    print("\tMinPuntos: ", Parametros.min_puntos)
    print("\tMaxPuntos: ", Parametros.max_puntos)
    print("\tUmbralDistancia: ", Parametros.umbral_distancia)



def main():

    global root
    global boton_conectar
    global boton_desconectar
    global boton_capturar
    global etiqueta_estado
    global entrada_iteraciones
    global entrada_cerca
    global entrada_media
    global entrada_lejos
    global entrada_minpuntos
    global entrada_maxpuntos
    global entrada_umbral_distancia

    for i in range(1, 7):
        os.makedirs("positivo" + str(i), exist_ok = True)
        os.makedirs("negativo" + str(i), exist_ok = True)

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

    boton_capturar = tkinter.Button(root, text = "Capturar")
    boton_capturar.grid(row = 4, column = 0)
    boton_capturar["state"] = "disabled"

    boton_agrupar = tkinter.Button(root, text = "Agrupar")
    boton_agrupar.grid(row = 5, column = 0)
    boton_agrupar["state"] = "disabled"

    boton_extraer_caracteristicas = tkinter.Button(root, text = "Extraer características")
    boton_extraer_caracteristicas.grid(row = 6, column = 0)
    boton_extraer_caracteristicas["state"] = "disabled"

    boton_entrenar = tkinter.Button(root, text = "Entrenar clasificador")
    boton_entrenar.grid(row = 7, column = 0)
    boton_entrenar["state"] = "disabled"

    boton_predecir = tkinter.Button(root, text = "Predecir")
    boton_predecir.grid(row = 8, column = 0)
    boton_predecir["state"] = "disabled"

    boton_salir = tkinter.Button(root, text = "Salir")
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

    lista_ficheros = tkinter.Listbox(root, width = 32, height = 12)
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
