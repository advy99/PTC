#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ejercicio 7:

Escribe una función mayusculas(palabra) que devuelva la palabra
pasada a mayúsculas.

"""

def mayusculas(palabra):
    """
    Funcion que devuelve la palabra en mayusculas
    """

    val_a = ord('a')
    val_z = ord('z')

    # para cada letra de la palabra
    for i in range( len(palabra) ):
        # cambiamos a mayuscula
        # la diferencia entre mayusculas y minusculas es de 32, como es el
        # quito bit (2^5), aplicando la operacion AND de la letra con ~32,
        # (todo 1, menos el quinto bit a cero), nos aseguramos que ese bit es 0
        # y por lo tanto pasamos la letra a mayuscula, o la dejamos si ya lo esta
        # primero tenemos que pasarlo el caracter a su representacion en entero
        # aplicamos la operacion, y pasamos el entero a su representacion como
        # caracter
        if ord(palabra[i]) >= val_a and ord(palabra[i]) <= val_z:
            palabra = palabra[:i] + chr(ord(palabra[i]) & ~32) + palabra[i+1:]

    return palabra


# introducimos los datos
palabra = input("Introduce una palabra: ")

# probamos la funcion
solucion = mayusculas(palabra)

print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))

solucion = palabra.upper()

print("\nUtilizando el metodo de str:")
print("La cadena original era: {}, tras aplicar la operacion es: {}".format(palabra, solucion))



