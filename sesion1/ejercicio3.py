#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sesion 1 - Ejercicio 3

    Programa que pide los dos catetos de un triangulo rectángulo,
y con estos calcula la hipotenusa.

"""


# usaremos el modulo math
import math


# pedimos las dimensiones del primer cateto y lo pasamos a float
cateto1 = input("Introduce las dimensiones del primer cateto: ")
cateto1 = float(cateto1)

# pedimos las dimensiones del segundo cateto y lo pasamos a float
cateto2 = input("Introduce las dimensiones del segundo cateto: ")
cateto2 = float(cateto2)

# calculamos la suma de cuadrados
suma_catetos_cuadrado = cateto1**2 + cateto2**2

# y con la suma de cuadrados la hipotenusa
hipotenusa = math.sqrt(suma_catetos_cuadrado)

# mostramos el resultado por pantalla
print("La hipotenusa mide : {} ".format(hipotenusa))

