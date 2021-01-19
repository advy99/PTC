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

def calcular_anchura(puntos):
    
    anchura = math.hypot(puntos[-1,0] - puntos[0,0], puntos[-1,1] - puntos[0,0] )
    
    return anchura


def calcular_profundidad(puntos):
    distancia_maxima = 0.0
    
    punto1_recta = puntos[0]
    punto2_recta = puntos[-1]
    
    for p in puntos:
        # distancia de un punto a una recta formada por dos puntos usando el producto y la norma
        distancia_recta = np.linalg.norm(np.cross(punto2_recta-punto1_recta, punto1_recta-p))/np.linalg.norm(punto2_recta-punto1_recta)
        
        distancia_maxima = max(distancia_maxima, distancia_recta)

    return distancia_maxima

def calcular_caracteristicas(fichero_entrada, fichero_salida, es_pierna):
    
    f_lectura = open(fichero_entrada, "r")
    
    clusters = f_lectura.readlines()
    
    f_lectura.close()
    
    i = 0
    
    f_salida = open(fichero_salida, "w")
    
    for cluster in clusters:
        if cluster != "":
            info_cluster = json.loads(cluster)
            puntos_x = np.array(info_cluster["puntosX"]).reshape(-1, 1)
            puntos_y = np.array(info_cluster["puntosY"]).reshape(-1, 1)

            puntos = np.concatenate([puntos_x, puntos_y], axis = 1)
            perimetro = calcular_perimetro(puntos)
            profundidad = calcular_profundidad(puntos)
            anchura = calcular_anchura(puntos)
            
            salida = {"numero_cluster":i, "perimetro":perimetro, "profundidad":profundidad, "anchura":anchura, "esPierna":es_pierna}
            
            f_salida.write(json.dumps(salida) + '\n')
            
            i += 1
            

    f_salida.close()



def crear_csv_caracteristicas(ficheros, fichero_salida):
    
    f_salida = open(fichero_salida, "w")
    
    for fichero in ficheros:
        
        f_lectura = open(fichero, "r")
        
        lineas = f_lectura.readlines()
        
        f_lectura.close()
        
        for linea in lineas:
            caracteristicas = json.loads(linea)
            salida = "{}, {}, {}, {} \n".format(caracteristicas["perimetro"], caracteristicas["profundidad"], caracteristicas["anchura"], caracteristicas["esPierna"])
            
            f_salida.write(salida)
    
    f_salida.close()
    

def caracteristicas():
    
    calcular_caracteristicas("clustersPiernas.json", "caracteristicasPiernas.dat", 1)
    calcular_caracteristicas("clustersNoPiernas.json", "caracteristicasNoPiernas.dat", 0)
    
    crear_csv_caracteristicas(["caracteristicasPiernas.dat", "caracteristicasNoPiernas.dat"], "piernasDataset.csv")

