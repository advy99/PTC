#!/usr/bin/env python

import math

def hipotenusa(cateto1, cateto2):
    suma_catetos_cuadrado = cateto1**2 + cateto2**2
    return math.sqrt(suma_catetos_cuadrado)


cateto1 = input("Introduce las dimensiones del primer cateto: ")
cateto1 = float(cateto1)

cateto2 = input("Introduce las dimensiones del segundo cateto: ")
cateto2 = float(cateto2)

print("La hipotenusa mide : {} ".format(hipotenusa(cateto1, cateto2)))

