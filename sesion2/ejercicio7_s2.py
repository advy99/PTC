#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sesion 2 - Ejercicio 7

Programa que pide el nombre, primer apellido y segundo apellido, muestra por
pantalla el nombre completo en una sola linea, el nombre al reves y finalmente
volver a descomponer el nombre y mostrarlo por pantalla

"""


# pedimos los datos
nombre = input("Introduce tu nombre: ")
primer_apellido = input("Introduce tu primer apellido: ")
segundo_apellido = input("Introduce tu segundo apellido: ")

# los concatenamos en un unico string
nombre_completo = nombre + " " + primer_apellido + " " + segundo_apellido

# lo mostramos por pantall
print("El nombre completo es {}".format(nombre_completo))

# le damos la vuelta recorriendo el vector entero, pero con paso de -1 para
# que vaya hacia atras
nombre_al_reves = nombre_completo[::-1]

# mostramos el nombre al reves
print("El nombre completo al reves es {}".format(nombre_al_reves))

# volvemos a separar el nombre completo con slit
nombre_separado = nombre_completo.split()

# mostramos el nombre separado
print("El nombre troceado es {}".format(nombre_separado))



