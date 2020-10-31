#!/usr/bin/env python
# -*- coding: utf-8 -*-

import financiacion


dinero = float(input("Introduce una cantidad de dinero en euros: "))

interes_anual = float(input("Introduce un porcentaje de interes [0-100]: "))

while interes_anual < 0 or interes_anual > 100:
    print("Tienes que introducir un valor entre 0 y 100, ambos incluidos.")
    interes_anual = float(input("Introduce un porcentaje de interes [0-100]: "))

periodo = int(input("Introduce el número de años: "))

dinero = financiacion.redondear(dinero)
interes_anual = financiacion.redondear(interes_anual)


capital_final = dinero

for i in range(periodo):
    capital_final = financiacion.calcular_capital_final(capital_final, interes_anual)



print(capital_final)
