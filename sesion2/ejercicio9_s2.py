#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sesion 2 - Ejercicio 9

Realizar un programa que tomando como entrada la radiación solar media por día en Kwh/m2 calcule el número mínimo de paneles solares que se necesitan para producir, al menos, 1000 Kwh en un mes (30 días) teniendo en cuenta que los paneles solares tienen un 17% de rendimiento y queson de un tamaño de 1.6 m2.

"""

def minimo_paneles(radiacion, objetivo=1000, num_dias=30, p_rendimiento=17, tam_panel=1.6):
    """
    Función para calcular el minimo de paneles necesarios para obtener cierto objetivo dado, en un numero de dias dado, con paneles de cierto rendimiento y tamaño.
    """

    # calculamos los kw por dia medios
    kwdias_un_panel = radiacion * (p_rendimiento / 100) * tam_panel

    # calculamos la produccion de un panel en los dias dados
    produccion_panel_en_num_dias = kwdias_un_panel * num_dias

    # calculamos el minimo de paneles
    minimo = objetivo // produccion_panel_en_num_dias

    # si hay un resto, necesitamos un panel mas
    if objetivo % produccion_panel_en_num_dias > 0:
        minimo += 1

    return int(minimo)


# pedimos la radiacion
radiacion = float(input("Introduce la radiación solar media por día: "))

# calculamos el minimo de paneles
num_paneles = minimo_paneles(radiacion)

# mostramos el resultado por pantalla
print("Son necesarios al menos {} paneles para conseguir el objetivo de 1000 Kwh en un mes con una productividad del 17% y una radiación de  {} si los paneles son de 1.6 m2 ".format(num_paneles, radiacion))


