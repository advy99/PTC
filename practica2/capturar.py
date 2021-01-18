#!/usr/bin/env python
# -*- coding: utf-8 -*-


from parametros import Parametros
import vrep
import json



def main(fichero, id_cliente):
    
    # sensor de la camara
    _, camhandle = vrep.simxGetObjectHandle(clientID, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
    
    # referencia a la persona, para moverla
    _, personhandle = vrep.simxGetObjectHandle(clientID, 'Bill', vrep.simx_opmode_oneshot_wait)


    
    #Iniciar la camara y esperar un segundo para llenar el buffer
    _, resolution, image = vrep.simxGetVisionSensorImage(id_cliente, camhandle, 0, vrep.simx_opmode_streaming)
    time.sleep(1)
    
    segundos = 0.5
    
    cabecera={"TiempoSleep":segundos,
                "MaxIteraciones": Parametros.iteraciones}
    
    fichero_laser=open(fichero, "w")

    fichero_laser.write(json.dumps(cabecera)+'\n')

    
    
    for i in range(1, Parametros.iteraciones):
        puntosx=[] #listas para recibir las coordenadas x, y z de los puntos detectados por el laser
        puntosy=[]
        puntosz=[]
        
        returnCode, signalValue = vrep.simxGetStringSignal(id_cliente,'LaserData',vrep.simx_opmode_buffer) 
        
        # esperamos 0.5 para el ciclo de lectura, como nos pide el guión
        time.sleep(segundos) #esperamos un tiempo para que el ciclo de lectura de datos no sea muy rápido
        
        datosLaser=vrep.simxUnpackFloats(signalValue)
        
        for indice in range(0,len(datosLaser),3):
            puntosx.append(datosLaser[indice+1])
            puntosy.append(datosLaser[indice+2])
            puntosz.append(datosLaser[indice])
    
        lectura={"Iteracion":i, "PuntosX":puntosx, "PuntosY":puntosy}
        fichero_laser.write(json.dumps(lectura)+'\n')

   
