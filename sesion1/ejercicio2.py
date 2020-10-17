#!/usr/bin/env python

import math


radio = input("Introduce el radio de la circunferencia: ")
radio = float(radio)

longitud = 2 * math.pi * radio
area = math.pi * radio**2

print("La longitud de la circunferencia es: {} ".format(longitud) )
print("El area de la circunferencia es: {} ".format(area) )
