#!/usr/bin/env python


def area_triangulo(base, altura):
    return base * altura / 2



base = input("Introduce la base del triangulo: ")
base = float(base)

altura = input("Introduce la altura del triangulo: ")
altura = float(altura)

print("El area del triangulo es: {} ".format(area_triangulo(base, altura)))

