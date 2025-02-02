#!/usr/bin/env python
# -*- coding: utf-8 -*-


from parametros import Parametros
import vrep
import json
import time
import glob
import re

def leer_datos_laser(id_cliente, segundos):
    #listas para recibir las coordenadas x, y z de los puntos detectados por el laser
    puntosx = []
    puntosy = []
    puntosz = []
    
    returnCode, signalValue = vrep.simxGetStringSignal(id_cliente,'LaserData',vrep.simx_opmode_buffer)
    
    #esperamos un tiempo para que el ciclo de lectura de datos no sea muy rápido
    time.sleep(segundos) 
    
    datosLaser = vrep.simxUnpackFloats(signalValue)
    
    for indice in range(0,len(datosLaser),3):
        puntosx.append(datosLaser[indice+1])
        puntosy.append(datosLaser[indice+2])
        puntosz.append(datosLaser[indice])
        
    return puntosx, puntosy, puntosz


def capturar_positivos(fichero, id_cliente):
    
    # sensor de la camara
    _, camhandle = vrep.simxGetObjectHandle(id_cliente, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
    
    # referencia a la persona, para moverla
    _, personhandle = vrep.simxGetObjectHandle(id_cliente, 'Bill', vrep.simx_opmode_oneshot_wait)
    
    # abrimos la conexion con el LaserData
    _, datosLaserComp = vrep.simxGetStringSignal(id_cliente,'LaserData',vrep.simx_opmode_streaming)


    # esperamos 0.5 para el ciclo de lectura, como nos pide el guión
    segundos = 0.5
    
    #Iniciar la camara y esperar un segundo para llenar el buffer
    _, resolution, image = vrep.simxGetVisionSensorImage(id_cliente, camhandle, 0, vrep.simx_opmode_streaming)
    time.sleep(segundos)
        
    cabecera = {"TiempoSleep":segundos,
                "MaxIteraciones":Parametros.iteraciones}
    
    fichero_laser = open(fichero, "w")

    fichero_laser.write(json.dumps(cabecera)+'\n')


    distancia = 0.0
    a_recorrer = 0.0
    
    if re.findall("Cerca", fichero):
        a_recorrer = Parametros.media - Parametros.cerca
        distancia = Parametros.cerca + a_recorrer 
    elif re.findall("Media", fichero):
        a_recorrer = Parametros.lejos - Parametros.media
        distancia = Parametros.media + a_recorrer
    elif re.findall("Lejos", fichero):
        a_recorrer = 1
        distancia = Parametros.lejos + 1
    
    # colocamos a BIll en la posicion inical
    returnCode = vrep.simxSetObjectPosition(id_cliente, personhandle, -1, [distancia , 0.0, 0.0], vrep.simx_opmode_oneshot)

    
    for i in range(1, Parametros.iteraciones):
        puntosx, puntosy, _ = leer_datos_laser(id_cliente, segundos)
    
        # escribimos los datos
        lectura = {"Iteracion":i, "PuntosX":puntosx, "PuntosY":puntosy}
        fichero_laser.write(json.dumps(lectura) + '\n')
        
        # movemos a la persona
        returnCode = vrep.simxSetObjectPosition(id_cliente, personhandle, -1, [distancia - a_recorrer * i / Parametros.iteraciones, 0.0, 0.0], vrep.simx_opmode_oneshot)
                                                                               
              
    # cerramos el fichero
    fichero_laser.close()
                                                                               
                                                                               
   
def capturar_negativos(fichero, id_cliente):
    
    # sensor de la camara
    _, camhandle = vrep.simxGetObjectHandle(id_cliente, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
    
    # referencia a la persona, para moverla
    _, cylinderhandler = vrep.simxGetObjectHandle(id_cliente, 'Cylinder', vrep.simx_opmode_oneshot_wait)
    _, cylinder1handler = vrep.simxGetObjectHandle(id_cliente, 'Cylinder1', vrep.simx_opmode_oneshot_wait)

    # abrimos la conexion con el LaserData
    _, datosLaserComp = vrep.simxGetStringSignal(id_cliente,'LaserData',vrep.simx_opmode_streaming)


    # esperamos 0.5 para el ciclo de lectura, como nos pide el guión
    segundos = 0.5
    
    #Iniciar la camara y esperar un segundo para llenar el buffer
    _, resolution, image = vrep.simxGetVisionSensorImage(id_cliente, camhandle, 0, vrep.simx_opmode_streaming)
    time.sleep(segundos)
        
    cabecera = {"TiempoSleep":segundos,
                "MaxIteraciones":Parametros.iteraciones}
    
    fichero_laser = open(fichero, "w")

    fichero_laser.write(json.dumps(cabecera)+'\n')


    distancia = 0.0
    a_recorrer = 0.0
    
    if re.findall("Cerca", fichero):
        a_recorrer = Parametros.media - Parametros.cerca
        distancia = Parametros.cerca + a_recorrer 
    elif re.findall("Media", fichero):
        a_recorrer = Parametros.lejos - Parametros.media
        distancia = Parametros.media + a_recorrer
    elif re.findall("Lejos", fichero):
        a_recorrer = 1
        distancia = Parametros.lejos + 1
    
    # colocamos a BIll en la posicion inical
    returnCode = vrep.simxSetObjectPosition(id_cliente, cylinderhandler, -1, [distancia , 0.15, 0.0], vrep.simx_opmode_oneshot)
    returnCode = vrep.simxSetObjectPosition(id_cliente, cylinder1handler, -1, [distancia , -0.15, 0.0], vrep.simx_opmode_oneshot)

    
    for i in range(1, Parametros.iteraciones):
        puntosx, puntosy, _ = leer_datos_laser(id_cliente, segundos)
    
        # escribimos los datos
        lectura = {"Iteracion":i, "PuntosX":puntosx, "PuntosY":puntosy}
        fichero_laser.write(json.dumps(lectura) + '\n')
        
        # movemos a al cilindro
        returnCode = vrep.simxSetObjectPosition(id_cliente, cylinderhandler, -1, [distancia - a_recorrer * i / Parametros.iteraciones, 0.15, 0.0], vrep.simx_opmode_oneshot)
        returnCode = vrep.simxSetObjectPosition(id_cliente, cylinder1handler, -1, [distancia - a_recorrer * i / Parametros.iteraciones, -0.15, 0.0], vrep.simx_opmode_oneshot)

                                                                               
              
    # cerramos el fichero
    fichero_laser.close()
