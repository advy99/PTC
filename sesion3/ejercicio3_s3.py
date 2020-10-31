#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 3:

Escribe una función mayusculas_minusculas(palabra) que devuelva una
cadena en la que las mayúsculas y las minúsculas estén al contrario.

"""

def mayusculas_minusculas(palabra):
    """
    Funcion para intercambiar las mayusculas por minusculas y viceversa de una
    cadena
    """

    solucion = ""

    # para cada letra de la palabra
    for letra in palabra:
        # cambiamos de mayuscula a minuscula
        # la diferencia entre mayusculas y minusculas es de 32, como es el
        # quito bit (2^5), aplicando la operacion XOR de la letra con 32,
        # intercambiamos entre 0 y 1 ese bit.
        # primero tenemos que pasarlo el caracter a su representacion en entero
        # aplicamos la operacion, y pasamos el entero a su representacion como
        # caracter
        if letra != ' ' or letra != '\n' or letra != '\t':
            solucion += chr(ord(letra) ^ 32)

    return solucion


# introducimos los datos
palabra = input("Introduce una palabra: ")

# probamos la funcion
solucion = mayusculas_minusculas(palabra)

print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))

solucion = palabra.swapcase()

print("\nUtilizando el metodo de str:")
print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))



