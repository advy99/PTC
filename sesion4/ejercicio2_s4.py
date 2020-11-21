#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2. Crea una lista con los valores enteros de 1 a N e implementa una función
que reciba dicha lista y nos devuelva una lista con los valores impares y el
número de dichos valores. Solicitar N por teclado y mostrar el resultado
por pantalla.
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

def valores_impares(lista):
    """
    Devuelve una lista con los valores impares de la lista dada
    """
    lista_sol = []

    # recorremos todos los elementos de la lista, y vamos metiendo los imapres
    for elemento in lista:
        if elemento % 2 == 1:
            lista_sol.append(elemento)

    return (lista_sol, len(lista_sol))


# pedimos los datos y lo probamos
num_elementos = int(input("Introduce el número de elementos: "))

lista = crear_lista(num_elementos)

impares = valores_impares(lista)

print("La lista dada con los valores impares es: ")
print(impares)



