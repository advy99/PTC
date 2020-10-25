#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sesion 2 - Ejercicio 10

Partiendo de una disolución de ácido sulfúrico en agua al 80 % de concentración, quiero obteneruna cantidad x de centímetros cúbicos a una concentración y% (y<80%). Siendo x, e y valores deentrada al programa, calcular cuantos centímetros cúbicos de la disolución al 80% y de agua sonnecesarios para obtener los x centímetros cúbicos deseados al y% de concentración.

"""

def obtener_disolucion(cc_a_obtener, porcentaje_concentracion):

    # calculamos los cc de acido que queremos en nuestra disolucion
    cc_acido = cc_a_obtener * (porcentaje_concentracion / 100)

    # necesitamos cc_acido cc de acido puro, por lo que si de una disolucion al 80 % sabemos que cc_acido = 80 * cc_necesarios, despejamos:
    cc_necesarios_disolucion = cc_acido / 0.8

    # el resto es agua
    agua = cc_a_obtener - cc_necesarios_disolucion

    return cc_necesarios_disolucion, agua


cc_a_obtener = float(input("Introduce los cc de la disolución a obtener: "))
porcentaje_concentracion = float(input("Introduce el porcentaje de concentración a obtener[0-80]: "))

if porcentaje_concentracion > 80:
    print("No puedo obtener una concentración de más del 80% si solo parto de una con un 80%")

else:
    cc_disolucion, agua = obtener_disolucion(cc_a_obtener, porcentaje_concentracion)
    print("Necesitamos {}cc de la disolucion al 80% de acido y {}cc de agua para obtener {}cc de la disolucion al {}%".format(cc_disolucion, agua, cc_a_obtener, porcentaje_concentracion))


