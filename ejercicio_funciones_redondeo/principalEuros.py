#!/usr/bin/env python
# -*- coding: utf-8 -*-

import financiacion
import math

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


# pedimos los datos
dinero = pedir_valor(float, 0, math.inf, "Introduce una cantidad de dinero en euros: ")

interes_anual = pedir_valor(float, 0, 100, "Introduce un porcentaje de interes [0-100]: ")

periodo = pedir_valor(int, 0, math.inf, "Introduce el número de años: ")

# redondeamos la entrada
dinero = financiacion.redondear(dinero)
interes_anual = financiacion.redondear(interes_anual)


# calculamos el capital final
capital_final = dinero

# lo aplicamos año a año
for i in range(periodo):
    capital_final = financiacion.calcular_capital_final(capital_final, interes_anual)

# mostramos la solucion por pantalla
print("Tras {} años, el capital obtenido a partir de {} con un interes del {} por ciento es {}".format(periodo, dinero, interes_anual, capital_final))

