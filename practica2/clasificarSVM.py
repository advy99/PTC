#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np  
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
    
    datos_piernas = pd.read_csv("piernasDataset.csv", names=colnames)

    datos_x = datos_piernas.drop("clase", axis = 1)
    datos_y = datos_piernas["clase"]
    
    # dividimos train y test, 20% de test
    x_train, x_test, y_train, y_test = train_test_split(datos_x, datos_y, test_size = 0.20, random_state=25)




