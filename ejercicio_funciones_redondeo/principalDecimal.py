#!/usr/bin/env python
#-*- coding: utf-8 -*-

# importamos los modulos necesarios
import math
import decimal
from decimal import Decimal, getcontext


def pedir_valor( tipo, tope_inferior=-math.inf, tope_superior=math.inf, mensaje="" ):
    """
    Funcion para pedir un valor, de un tipo dado, en un intervalo dado.
    Opcionalmente recibe un mensaje que mostrará al pedir el valor
    """

    # pedimos el valor con input, y lo pasamos al tipo pedido
    valor = tipo(input(mensaje))

    # mientas este fuera del rango, lo seguimos pidiendo
    while valor < tope_inferior or valor > tope_superior:
        print("Debes introducir un valor entre {} y {}, ambos incluidos".format(tope_inferior, tope_superior))
        valor = tipo(input(mensaje))

    # devolvemos el valor
    return valor


# especificamos la forma de redondeo
getcontext().rounding = decimal.ROUND_HALF_UP

# pedimos los datos
dinero = pedir_valor(Decimal, 0, math.inf, "Introduce una cantidad de dinero en euros: ")

interes_anual = pedir_valor(Decimal, 0, 100, "Introduce un porcentaje de interes [0-100]: ")

periodo = pedir_valor(int, 0, math.inf, "Introduce el número de años: ")


# redondeamos los datos de entrada
dinero = dinero.quantize(Decimal("1.00"))
interes_anual = interes_anual.quantize(Decimal("1.00"))

# calculamos el capital final
capital_final = dinero

for i in range(periodo):
    capital_final = capital_final + capital_final * interes_anual/100

# redondeamos el resultado
capital_final = capital_final.quantize(Decimal("1.00"))

# lo mostramos por pantalla
print("Tras {} años, el capital obtenido a partir de {} con un interes del {} por ciento es {}".format(periodo, dinero, interes_anual, capital_final))

