#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np 
import json
import math


def calcular_perimetro(puntos):
    perimetro = 0.0
    
    i = 0
    
    for i in range(len(puntos) - 1):
        distancia = math.hypot(puntos[i+1,0] - puntos[i,0], puntos[i+1,1] - puntos[i,0] )
        
        perimetro += distancia
    
    return perimetro

def calcular_caracteristicas(fichero_entrada, fichero_salida, es_pierna):
    
    f_lectura = open(fichero_entrada, "r")
    
    clusters = f_lectura.readlines()
    
    f_lectura.close()
    
    i = 0
    
    for cluster in clusters:
        if cluster != "":
            info_cluster = json.load(cluster)
            puntos_x = np.array(info_cluster["puntosX"]).reshape(-1, 1)
            puntos_y = np.array(info_cluster["puntosY"]).reshape(-1, 1)

            puntos = np.concatenate([puntos_x, puntos_y], axis = 1)
            perimetro = calcular_perimetro(puntos)
            profundidad = calcular_profundidad(puntos)
            anchura = calcular_anchura(puntos)
            
            salida = {"numero_cluster":i, "perimetro":perimetro, "profundidad":profundidad, "anchura":anchura, "esPierna":es_pierna}
            i += 1 


def caracteristicas():
    
    calcular_caracteristicas("clustersPiernas.json", "caracteristicasPiernas.dat", 1)
    calcular_caracteristicas("clustersNoPiernas.json", "caracteristicasNoPiernas.dat", 0)


