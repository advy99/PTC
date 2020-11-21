#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
1. Crea una lista con los valores enteros de 1 a N e implementa una función
que reciba dicha lista y nos devuelva la suma de dichos valores. Solicitar N
por teclado y mostrar el resultado por pantalla.
"""

def crear_lista(limite_superior):
    """
    Función para dado un número entero, crear una lista con los valores desde
    0 hasta el número dado
    """

    lista = []

    # recorremos todos los valores, y los añadimos a la lista
    # introducimos i + 1 porque el cero no está incluido pero el ultimo si
    for i in range(limite_superior):
        lista.append(i + 1)

    return lista

def suma_elementos_lista(lista):
    """
    Sumar los elementos de una lista
    """
    suma = 0

    # recorremos todos los elementos de la lista, y los vamos sumando
    for elemento in lista:
        suma += elemento

    return suma


# pedimos los datos y lo probamos
num_elementos = int(input("Introduce el número de elementos: "))

lista = crear_lista(num_elementos)

suma = suma_elementos_lista(lista)

print("El resultado de la suma de todos los elementos de 0 a {} es {}".format(num_elementos, suma))


print("\nUtilizando métodos de listas")

suma = sum(lista)

print("El resultado de la suma de todos los elementos de 0 a {} es {}".format(num_elementos, suma))

