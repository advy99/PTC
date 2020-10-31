#!/usr/bin/env python


def redondear ( numero, decimales=2 ):
    """
    Funcion que recibe dos parámetros, un número y la cantidad de decimales
    a redondear, por defecto dos. Como salida da el numero redondeado a tantos
    decimales como se indiquen.
    """

    redondeado = numero * 10**decimales
    redondeado += 0.5
    redondeado = int(redondeado)
    redondeado = redondeado / 10**decimales


    return redondeado

def calcular_capital_final ( capital_inicial, interes ):
    """
    Función que dada una cantidad de capital (float con dos decimales), y un
    interes en tanto por ciento (con dos decimales), da la suma de capital
    inicial con el interes obtenido, redondeado a dos decimales
    """

    intereses_ganados = capital_inicial * (intereses/100)

    capital_final = capital_inicial + intereses_ganados

    capital_final = redondear( capital_final, 2 )

    return capital_final


if __name__ == "main":
    print("Módulo de financiacion llamado como fichero principal")

