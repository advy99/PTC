#!/usr/bin/env python

import math

def longitud_circunferencia(radio):
    return 2 * math.pi * radio

def area_circunferencia(radio):
    return math.pi * radio**2

radio = input("Introduce el radio de la circunferencia: ")
radio = float(radio)

print("La longitud de la circunferencia es: {} ".format(longitud_circunferencia(radio)) )
print("El area de la circunferencia es: {} ".format(area_circunferencia(radio)) )
