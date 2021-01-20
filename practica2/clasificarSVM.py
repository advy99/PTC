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
    
    # grid de parametros para la grid search
    parametros = [
        {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['linear']},
        {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
        {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'degree': [1, 2, 3, 4, 5], 'kernel': ['poly']}
    ]

    svc = SVC()
    
    grid_search = GridSearchCV(svc, parametros)

    grid_search.fit(x_train, y_train)

    print("Mejores parametros encontrados por grid_search:")
    print(grid_search.best_params_)
    
    y_pred = grid_search.predict(x_test)

    print("Matriz de confusión Filas: verdad Columnas: predicción")
    print(confusion_matrix(y_test, y_pred))
    
    
    # predicciones con validación cruzada:
    scores = cross_val_score(grid_search, datos_x, datos_y, cv=5)

    # exactitud media con intervalo de confianza del 95%
    print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))

    # guardamos el clasificador
    with open("mejor_clasificador.pkl", "wb") as archivo:
        pickle.dump(grid_search, archivo)
