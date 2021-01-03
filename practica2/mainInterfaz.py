#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter


def main():
    root = tkinter.Tk()
    root.geometry("700x300")

    etiquetaInfo = tkinter.Label(root, text = "Es necesario ejecutar el simulador VREP")
    etiquetaInfo.grid(row = 0, column = 0)

    botonConectar = tkinter.Button(root, text = "Conectar con VREP")
    botonConectar.grid(row = 1, column = 0)

    botonDesconectar = tkinter.Button(root, text = "Detener y desconectar VREP")
    botonDesconectar.grid(row = 2, column = 0)


    etiquetaEstado = tkinter.Label(root, text = "Estado: No conectado con VREP")
    etiquetaEstado.grid(row = 3, column = 0)

    botonCapturar = tkinter.Button(root, text = "Capturar")
    botonCapturar.grid(row = 4, column = 0)

    botonAgrupar = tkinter.Button(root, text = "Agrupar")
    botonAgrupar.grid(row = 5, column = 0)

    botonExtraerCaracteristicas = tkinter.Button(root, text = "Extraer características")
    botonExtraerCaracteristicas.grid(row = 6, column = 0)

    botonEntrenar = tkinter.Button(root, text = "Entrenar clasificador")
    botonEntrenar.grid(row = 7, column = 0)

    botonPredecir = tkinter.Button(root, text = "Predecir")
    botonPredecir.grid(row = 8, column = 0)

    botonSalir = tkinter.Button(root, text = "Salir")
    botonSalir.grid(row = 9, column = 0)



    etiquetaParametros = tkinter.Label(root, text = "Parámetros")
    etiquetaParametros.grid(row = 1, column = 1)


    etiquetaIteraciones = tkinter.Label(root, text = "Iteraciones:")
    etiquetaIteraciones.grid( row = 2, column = 1)

    entradaIteraciones = tkinter.Entry(root)
    entradaIteraciones.grid(sticky = "E", row = 2, column = 2)


    etiquetaCerca = tkinter.Label(root, text = "Cerca:")
    etiquetaCerca.grid( row = 3, column = 1)

    entradaCerca = tkinter.Entry(root)
    entradaCerca.grid(sticky = "E", row = 3, column = 2)

    etiquetaMedia = tkinter.Label(root, text = "Media:")
    etiquetaMedia.grid( row = 4, column = 1)

    entradaMedia = tkinter.Entry(root)
    entradaMedia.grid(sticky = "E", row = 4, column = 2)

    etiquetaLejos = tkinter.Label(root, text = "Lejos:")
    etiquetaLejos.grid( row = 5, column = 1)

    entradaLejos = tkinter.Entry(root)
    entradaLejos.grid(sticky = "E", row = 5, column = 2)


    etiquetaMinPuntos = tkinter.Label(root, text = "MinPuntos:")
    etiquetaMinPuntos.grid( row = 6, column = 1)

    entradaMinPuntos = tkinter.Entry(root)
    entradaMinPuntos.grid(sticky = "E", row = 6, column = 2)

    etiquetaMaxPuntos = tkinter.Label(root, text = "MaxPuntos:")
    etiquetaMaxPuntos.grid( row = 7, column = 1)

    entradaMaxPuntos = tkinter.Entry(root)
    entradaMaxPuntos.grid(sticky = "E", row = 7, column = 2)

    etiquetaUmbralDistancia = tkinter.Label(root, text = "UmbralDistancia:")
    etiquetaUmbralDistancia.grid( row = 8, column = 1)

    entradaUmbralPuntos = tkinter.Entry(root)
    entradaUmbralPuntos.grid(sticky = "E", row = 8, column = 2)

    botonCambiar = tkinter.Button(root, text = "Cambiar")
    botonCambiar.grid(row = 9, column = 1)






    etiquetaFicheros = tkinter.Label(root, text = "Fichero para la captura")
    etiquetaFicheros.grid(row = 1, column = 3)


    root.mainloop()


main()
