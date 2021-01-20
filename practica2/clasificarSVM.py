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


def comparar_reales(a, b, epsilon = 0.0005):
    return abs(a - b) < epsilon

def probarSVM(datos_x, datos_y, x_train, y_train, x_test, y_test, svc, parametros):
        
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
    
    return scores, grid_search

def clasificar_piernas():
    
    columnas = ["perimetro", "profundidad", "anchura", "clase"]
    
    datos_piernas = pd.read_csv("piernasDataset.csv", names=columnas)

    datos_x = datos_piernas.drop("clase", axis = 1)
    datos_y = datos_piernas["clase"]
    
    # dividimos train y test, 20% de test
    x_train, x_test, y_train, y_test = train_test_split(datos_x, datos_y, test_size = 0.20, random_state=25)
    
    # grid de parametros para la grid search
    parametros = {'C':[1,10,100,1000],
                 'gamma': [0.001, 0.005, 0.01, 0.1]}
    
    parametros_linear = {'C':[1,10]}

    svc_rbf = SVC(kernel='rbf')
    svc_linear = SVC(kernel='linear')
    svc_poly_2 = SVC(kernel='poly', degree=2)
    svc_poly_3 = SVC(kernel='poly', degree=3)
    svc_poly_4 = SVC(kernel='poly', degree=4)
    
    print("Entrenando modelos, esto puede tardar un poco")
    scores_rbf, grid_rbf = probarSVM(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_rbf, parametros)
    scores_linear, grid_linear = probarSVM(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_linear, parametros_linear)
    scores_poly_2, grid_poly_2 = probarSVM(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_poly_2, parametros)
    scores_poly_3, grid_poly_3 = probarSVM(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_poly_3, parametros)
    scores_poly_4, grid_poly_4 = probarSVM(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_poly_4, parametros)

    mejor_score = max(scores_rbf.mean(), scores_linear.mean(), scores_poly_2.mean(), scores_poly_3.mean(), scores_poly_4.mean())
    
    if comparar_reales(mejor_score, scores_rbf.mean() ):
        print("El mejor estimador es SVC con el kernel RBF con los siguientes parámetros: ")
        print(grid_rbf.best_params_)
        grid_search = grid_rbf
    elif comparar_reales(mejor_score, scores_linear.mean()):
        print("El mejor estimador es SVC con el kernel linear con los siguientes parámetros: ")
        print(grid_linear.best_params_)
        grid_search = grid_linear
    elif comparar_reales(mejor_score, scores_poly_2.mean()):
        print("El mejor estimador es SVC con el kernel polinomico de grado 2 con los siguientes parámetros: ")
        print(grid_poly_2.best_params_)
        grid_search = grid_poly_2
    elif comparar_reales(mejor_score, scores_poly_3.mean()):
        print("El mejor estimador es SVC con el kernel polinomico de grado 3 con los siguientes parámetros: ")
        print(grid_poly_3.best_params_)
        grid_search = grid_poly_3
    elif comparar_reales(mejor_score, scores_poly_4.mean()):
        print("El mejor estimador es SVC con el kernel polinomico de grado 4 con los siguientes parámetros: ")
        print(grid_poly_4.best_params_)
        grid_search = grid_poly_4
        
        
        
    # guardamos el clasificador
    with open("mejor_clasificador.pkl", "wb") as archivo:
        pickle.dump(grid_search, archivo)
