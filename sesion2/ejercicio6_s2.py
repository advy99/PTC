#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sesion 2 - Ejercicio 6

Programa que pide tres valores y muestra por pantalla su maximo y su minimo

"""


def mayor_y_menor(numero1, numero2, numero3):
    """
    Función que dado tres números devuelve el mayor y el menor
    """

    # suponemos que el mayor y el menor es el primero
    mayor = numero1
    menor = numero1

    # si el segundo es mas grande, actualizamos el mayor
    if numero2 > mayor:
        mayor = numero2

    # si el tercero es mas grande, actualizamos el mayor
    if numero3 > mayor:
        mayor = numero3

    # si el segundo es menor, actualizamos el menor
    if numero2 < menor:
        menor = numero2

    # si el tercero es menor, actualizamos el menor
    if numero3 < menor:
        menor = numero3

    # devolvemos el mayor y el menor
    return mayor, menor

# pedimos los tres numeros
x1 = float(input("Introduce el primer numero: "))
x2 = float(input("Introduce el segundo numero: "))
x3 = float(input("Introduce el tercero numero: "))

# de los tres obtenemos el mayor y el menor
mayor, menor = mayor_y_menor(x1, x2, x3)

# los mostramos por pantalla
print("El mayor es {} y el menor es {}".format(mayor, menor))




