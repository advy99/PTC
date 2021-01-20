#!/usr/bin/env python
# -*- coding: utf-8 -*-

import caracteristicas
import capturar
import agrupar
import vrep
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
import pickle
import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

from parametros import Parametros
Parametros.min_puntos = 3
Parametros.max_puntos = 25
Parametros.umbral_distancia = 5

def predecir_escena(id_cliente):
    
    # sensor de la camara
    _, camhandle = vrep.simxGetObjectHandle(id_cliente, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
        
    # abrimos la conexion con el LaserData
    _, datosLaserComp = vrep.simxGetStringSignal(id_cliente,'LaserData',vrep.simx_opmode_streaming)
    
    #Iniciar la camara y esperar un segundo para llenar el buffer
    _, resolution, image = vrep.simxGetVisionSensorImage(id_cliente, camhandle, 0, vrep.simx_opmode_streaming)
    time.sleep(1)
        
    # leemos los datos
    puntosx, puntosy, _ = capturar.leer_datos_laser(id_cliente, 0.5)
    
    # creamos la muestra
    muestra = {"Iteracion":0, "PuntosX":puntosx, "PuntosY":puntosy}
    
    clusters = []
    # la procesamos para agruparla
    clusters_m = agrupar.clusters_muestra(muestra)
    clusters.append( clusters_m[:] )
    
    agrupar.volcar_clusters("prediccion/clustersPrediccion.json", clusters)
    
    # leemos el predictor
    with open("mejor_clasificador.pkl", "rb") as archivo:
        clasificador = pickle.load(archivo)
    
    clusters = np.array(clusters)
    
    # para cada cluster, calculamos las caracteristicas
    for cluster in clusters:
        cluster_np = np.array(cluster)
        if len(cluster_np) != 0:
            dic_cluster = {"numero_puntos":len(cluster), "puntosX":list(cluster_np[:, 0]), "puntosY":list(cluster_np[:, 1])}
        
            puntos_x = np.array(dic_cluster["puntosX"]).reshape(-1, 1)
            puntos_y = np.array(dic_cluster["puntosY"]).reshape(-1, 1)

            puntos = np.concatenate([puntos_x, puntos_y], axis = 1)
            perimetro = caracteristicas.calcular_perimetro(puntos)
            profundidad = caracteristicas.calcular_profundidad(puntos)
            anchura = caracteristicas.calcular_anchura(puntos)
            
            caracteristicas_cluster = [perimetro, profundidad, anchura]
            caracteristicas_cluster = np.array(caracteristicas_cluster)
            
            prediccion = clasificador.predict([caracteristicas_cluster])
            
            plt.clf()    
            plt.plot(puntosx, puntosy, 'r.')
            plt.show()
    
                 
vrep.simxFinish(-1)
id_cliente = vrep.simxStart("127.0.0.1", 19999, True, True, 5000, 5)
predecir_escena(id_cliente)
