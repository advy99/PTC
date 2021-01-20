#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np  
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
import pickle


# ignoramos warnings, como en el ejemplo
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
simplefilter(action='ignore', category=DeprecationWarning)




def clasificar_piernas():
    
    columnas = ["perimetro", "profundidad", "anchura", "clase"]
    
    datos_piernas = pd.read_csv("piernasDataset.csv", names=columnas)

    datos_x = datos_piernas.drop("clase", axis = 1)
    datos_y = datos_piernas["clase"]
    
    # dividimos train y test, 20% de test
    x_train, x_test, y_train, y_test = train_test_split(datos_x, datos_y, test_size = 0.20, random_state=25)


    # kernel lineal
    
    svc_lineal = SVC(kernel='linear')  
    svc_lineal.fit(x_train, y_train)
    
    y_pred = svc_lineal.predict(x_test)

    acc_test=accuracy_score(y_test, y_pred)

    print("Acc_test Lineal: (TP+TN)/(T+P)  %0.4f" % acc_test)

    print("Matriz de confusión Filas: verdad Columnas: predicción")

    print(confusion_matrix(y_test, y_pred))
    
    print("Precision= TP / (TP + FP), Recall= TP / (TP + FN)")
    print("f1-score es la media entre precisión y recall")
    print(classification_report(y_test, y_pred))

    
    # ahora con cross-val
    svc_lineal2 = SVC(kernel='linear')

    scores = cross_val_score(svc_lineal2, datos_x, datos_y, cv=5)

    # exactitud media con intervalo de confianza del 95%
    print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
    
clasificar_piernas()
