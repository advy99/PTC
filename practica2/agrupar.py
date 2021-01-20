#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import glob
import numpy as np
from parametros import Parametros
import math

def clusters_muestra(muestra):
    
    
    puntos_x = np.array(muestra["PuntosX"]).reshape(-1, 1)
    puntos_y = np.array(muestra["PuntosY"]).reshape(-1, 1)

    puntos = np.concatenate([puntos_x, puntos_y], axis = 1)
    
    todos_clusters = []
    
    i = 0

    # para todos los puntos
    while i < len(puntos):
        j = i
        # metemos en el inicial el cluster actual
        cluster = []
        cluster += [puntos[j]]

        he_pasado_umbral = False
        
        # mientras no me pase del umbral, no haya llegado al máximo de puntos, y me queden puntos
        while not he_pasado_umbral and len(cluster) < Parametros.max_puntos and j < len(puntos) - 1:
            distancia = math.hypot(puntos[j+1,0] - puntos[j,0], puntos[j+1,1] - puntos[j,1] )
            # si la distancia con el siguiente es menor o igual, lo meto en el cluster
            if distancia <= Parametros.umbral_distancia:
                cluster += [puntos[j + 1]]
            else:
                he_pasado_umbral = True
            j += 1
        
        # si tengo min_puntos, acepto el cluster
        if len(cluster) >= Parametros.min_puntos:
            todos_clusters.append(cluster)
            
            
        i = j + 2
    
    return todos_clusters
    

def agrupar_clusters(directorios):
    clusters = []
    
    for archivo in directorios:
                
        fichero = open(archivo, "r")
        
        lineas = fichero.readlines()
        
        # leemos todas las lineas, menos la primera que es la cabecera
        for linea in lineas[1:]:
            if linea != "":
                muestra = json.loads(linea)
                
                clusters_muestra_actual = clusters_muestra(muestra)
                clusters.append( clusters_muestra_actual[:] )

        fichero.close()

    return clusters


def volcar_clusters(salida_json, clusters):
    fichero_salida = open(salida_json, "w")
    i = 0
    for muestra in clusters:
        for cluster in muestra:
            cluster_np = np.array(cluster)
            salida = {"numero_cluster":i, "numero_puntos":len(cluster_np), "puntosX":list(cluster_np[:, 0]), "puntosY":list(cluster_np[:, 1])}
            fichero_salida.write(json.dumps(salida) + '\n')
            i += 1

    fichero_salida.close

def agrupar():
    directoriosPositivos = sorted(glob.glob("positivo?/*.json"))
    clusters_positivos = agrupar_clusters(directoriosPositivos)
    volcar_clusters("clustersPiernas.json", clusters_positivos)
    
    directoriosNegativos = sorted(glob.glob("negativo?/*.json"))
    clusters_negativos = agrupar_clusters(directoriosNegativos)
    volcar_clusters("clustersNoPiernas.json", clusters_negativos)
