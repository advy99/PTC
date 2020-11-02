#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo financiación. Contiene:
    Función redondear
    Función calcular_capital_final
"""


def redondear ( numero, decimales=2 ):
    """
    Funcion que recibe dos parámetros, un número y la cantidad de decimales
    a redondear, por defecto dos. Como salida da el numero redondeado a tantos
    decimales como se indiquen.
    """

    # lo multiplicamos por 10^decimales, para que la parte entera tenga hasta
    # donde queremos redondear
    redondeado = numero * 10**decimales

    # sumamos 0.5, para acercarlo a donde queremos redondear
    redondeado += 0.5

    # nos quedamos con la parte entera, si al sumar 0.5 se paso del entero, es
    # que redondeamos hacia arriba, si no, se mantiene y redondeamos hacia abajo
    redondeado = int(redondeado)

    # dividimos por 10^decimales, para volver a dejar la parte entera como se
    # nos dio
    redondeado = redondeado / 10**decimales


    return redondeado

def calcular_capital_final ( capital_inicial, interes ):
    """
    Función que dada una cantidad de capital (float con dos decimales), y un
    interes en tanto por ciento (con dos decimales), da la suma de capital
    inicial con el interes obtenido, redondeado a dos decimales
    """

    # calculamos los intereses ganados
    intereses_ganados = capital_inicial * (interes/100)

    # sumamos el capital inicial con los intereses
    capital_final = capital_inicial + intereses_ganados

    # redondeamos el resultado
    capital_final = redondear( capital_final, 2 )

    return capital_final


if __name__ == "main":
    print("Módulo de financiacion llamado como fichero principal")

