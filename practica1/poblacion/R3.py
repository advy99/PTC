#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import R2


def main():
    diccionario_pob_comunidades = R2.main()

    diccionario_pob_media_comunidades = {}

    for clave in diccionario_pob_comunidades:
        media = 0

        for i in range(8):
            media += diccionario_pob_comunidades[clave][i]

        media /= 8

        diccionario_pob_media_comunidades[clave] = media

    com_pob_ordenadas = sorted(diccionario_pob_media_comunidades.items(), key=lambda x: x[1], reverse=True)

    mas_pobladas_media = []

    for i in range(10):
        mas_pobladas_media.append(com_pob_ordenadas[i][0])





if __name__ == "__main__":
    main()
