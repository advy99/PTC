#!/usr/bin/env python
# -*- coding: utf-8 -*-

import financiacion
import math

def pedir_valor( tipo, tope_inferior=-math.inf, tope_superior=math.inf, mensaje="" ):
    valor = tipo(input(mensaje))

    while valor < tope_inferior or valor > tope_superior:
        print("Debes introducir un valor entre {} y {}, ambos incluidos".format(tope_inferior, tope_superior))
        valor = tipo(input(mensaje))

    return valor


dinero = pedir_valor(float, 0, math.inf, "Introduce una cantidad de dinero en euros: ")

interes_anual = pedir_valor(float, 0, 100, "Introduce un porcentaje de interes [0-100]: ")

periodo = pedir_valor(int, 0, math.inf, "Introduce el número de años: ")

dinero = financiacion.redondear(dinero)
interes_anual = financiacion.redondear(interes_anual)


capital_final = dinero

for i in range(periodo):
    capital_final = financiacion.calcular_capital_final(capital_final, interes_anual)

print("Tras {} años, el capital obtenido a partir de {} con un interes del {} por ciento es {}".format(periodo, dinero, interes_anual, capital_final))

