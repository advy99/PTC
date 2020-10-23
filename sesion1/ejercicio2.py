#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sesion 1 - Ejercicio 2

    Programa que pide el radio de una circunferencia y muestra por pantalla
la longitud y el area de dicha circunferencia

"""

# usaremos el modulo math
import math


# pedimos al usuario el radio y lo pasamos a float
radio = input("Introduce el radio de la circunferencia: ")
radio = float(radio)

# calculamos la longitud y el area
longitud = 2 * math.pi * radio
area = math.pi * radio**2

# mostramos por pantalla el resultado
print("La longitud de la circunferencia es: {} ".format(longitud) )
print("El area de la circunferencia es: {} ".format(area) )
