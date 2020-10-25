#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sesion 2 - Ejercicio 8

Programa que pide el porcentaje de alcohol de una bebida y muestra por pantalla
cuantos tercios de esta bebida podemos ingerir sin ingerir más de 50cc de alcohol.


"""

def num_bebidas(p_alcohol, limite_ingesta_alcohol=50, tam_bebida=333):
    """
    Función para calcular el numero máximo de bebidas de un tamaño dado sin pasarse del limite de ingesta dado
    """

    # calculamos el alcohol en una bebida
    alcohol_en_una_bebida = tam_bebida * p_alcohol / 100

    # la division entera del limite de ingesta entre el alcohol de una bebida
    # será el máximo posible
    num_posibles_bebidas = limite_ingesta_alcohol // alcohol_en_una_bebida

    return int(num_posibles_bebidas)


# datos del programa
limite = 50
porcentaje_alcohol = float(input("Introduce el porcentaje de alcohol de la bebida [0-100]: "))

# calculamos las bebidas que podemos ingerir
num_bebidas_ingerir = num_bebidas(porcentaje_alcohol)

# mostramos el resultado por pantalla
print("Puedes tomar {} tercios con {} por ciento de alcohol sin pasarte de {}cc de alcohol.".format(num_bebidas_ingerir, porcentaje_alcohol, limite))

