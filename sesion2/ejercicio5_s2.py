#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Sesion 2 - Ejercicio 5

Programa que calcula la diferencia en horas, minutos y segundos entre
dos instantes pedidos al usuario en horas, minutos, segundos

"""


def formatear_hora(hora):
    """
        Función para pasar una fecha dada para que tanto minutos como segundos
        sean como mucho 60
    """
    segundos = hora[2] % 60
    suma_minutos = hora[1] + hora[2] // 60
    minutos = suma_minutos % 60
    horas = hora[0] + suma_minutos // 60

    return horas, minutos, segundos



def pedir_instante_tiempo():
    """
        Función que pide hora, minutos y segundos y lo devuelve

    """
    hora = int(input("Introduce la hora: "))
    minuto = int(input("Introduce el minuto: "))
    segundo = int(input("Introduce el segundo: "))

    # devolvemos una tupla con los tres valores
    return hora, minuto, segundo


def diferencia_instantes(instante1, instante2):
    """
        Funcion para calcular la diferencia entre dos horas
    """

    # aseguramos que los instantes estan bien representados
    instante1 = formatear_hora(instante1)
    instante2 = formatear_hora(instante2)

    # calculamos la diferencia en valor absoluto
    diferencia_horas = abs(instante1[0] - instante2[0])
    diferencia_minutos = abs(instante1[1] - instante2[1])
    diferencia_segundos = abs(instante1[2] - instante2[2])

    # devolvemos una tupla con los tres valores
    return diferencia_horas, diferencia_minutos, diferencia_segundos


# pedimos los instantes de tiempo
instante1 = pedir_instante_tiempo()
instante2 = pedir_instante_tiempo()

# calculamos su diferencia
diferencia_instantes = diferencia_instantes(instante1, instante2)

# formateamos la hora por si la diferencia de minutos o segundos es < 60
diferencia_instantes = formatear_hora(diferencia_instantes)

# lo mostramos por pantalla
print("La diferencia es de {} horas, {} minutos y {} segundos".format(diferencia_instantes[0], diferencia_instantes[1], diferencia_instantes[2] ))

