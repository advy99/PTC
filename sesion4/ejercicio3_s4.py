#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3. Crea una lista con los valores enteros de 1 a N e implementa una función
que reciba dicha lista y nos devuelva el máximo y el mínimo de dichos valores,
así como sus respectivas posiciones. Solicitar N por teclado y mostrar
el resultado por pantalla.
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

def max_min_lista(lista):
    """
    Devuelve el maximo y el minimo de la lista
    """
    maximo = lista[0]
    pos_max = 0
    minimo = lista[0]
    pos_min = 0

    # recorremos todos los elementos de la lista, y los vamos sumando
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            pos_max = i

        if lista[i] < minimo:
            minimo = lista[i]
            pos_min = i

    return ( (maximo, pos_max), (minimo, pos_min)  )


# pedimos los datos y lo probamos
num_elementos = int(input("Introduce el número de elementos: "))

lista = crear_lista(num_elementos)

min_y_max = max_min_lista(lista)

print("El máximo de la lista es {} y su posición es {}".format(min_y_max[0][0], min_y_max[0][1]))

print("El mínimo de la lista es {} y su posición es {}".format(min_y_max[1][0], min_y_max[1][1]))


print("\nUtilizando métodos de listas")



