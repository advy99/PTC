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

def entrenar_modelo(datos_x, datos_y, x_train, y_train, x_test, y_test, svc):
    svc.fit(x_train, y_train)
    
    y_pred = svc.predict(x_test)

    print("Matriz de confusión Filas: verdad Columnas: predicción")
    print(confusion_matrix(y_test, y_pred))
    
    
    # predicciones con validación cruzada:
    scores = cross_val_score(svc, x_test, y_test, cv=5, n_jobs=-1)

    # exactitud media con intervalo de confianza del 95%
    print("Accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (scores.mean(), scores.std() * 2))
    
    return scores, svc

def entrenar_grid(datos_x, datos_y, x_train, y_train, x_test, y_test, svc, parametros):
        
    grid_search = GridSearchCV(svc, parametros, n_jobs=-1)
    
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
    
    svc_rbf = SVC(kernel='rbf')
    svc_linear = SVC(kernel='linear')
    svc_poly_2 = SVC(kernel='poly', degree=2)
    svc_poly_3 = SVC(kernel='poly', degree=3)
    svc_poly_4 = SVC(kernel='poly', degree=4)
    
    print("Entrenando modelos, esto puede tardar un poco")
    print("Entrenando rbf")
    scores_rbf, grid_rbf = entrenar_grid(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_rbf, parametros)
    scores_linear, svc_linear = entrenar_modelo(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_linear)
    scores_poly_2, svc_poly_2 = entrenar_modelo(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_poly_2)
    scores_poly_3, svc_poly_3 = entrenar_modelo(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_poly_3)
    scores_poly_4, svc_poly_4 = entrenar_modelo(datos_x, datos_y, x_train, y_train, x_test, y_test, svc_poly_4)


    mejor_score = max(scores_rbf.mean(), scores_linear.mean(), scores_poly_2.mean(), scores_poly_3.mean(), scores_poly_4.mean())
    
    if comparar_reales(mejor_score, scores_rbf.mean() ):
        print("El mejor estimador es SVC con el kernel RBF con los siguientes parámetros: ")
        print(grid_rbf.best_params_)
        mejor_score = scores_rbf
        grid_search = grid_rbf
    elif comparar_reales(mejor_score, scores_linear.mean()):
        print("El mejor estimador es SVC con el kernel linear: ")
        mejor_score = scores_linear
        grid_search = svc_linear
    elif comparar_reales(mejor_score, scores_poly_2.mean()):
        print("El mejor estimador es SVC con el kernel polinomico de grado 2 ")
        mejor_score = scores_poly_2
        grid_search = svc_poly_2
    elif comparar_reales(mejor_score, scores_poly_3.mean()):
        print("El mejor estimador es SVC con el kernel polinomico de grado 3 ")
        mejor_score = scores_poly_3
        grid_search = svc_poly_3
    elif comparar_reales(mejor_score, scores_poly_4.mean()):
        print("El mejor estimador es SVC con el kernel polinomico de grado 4 ")
        mejor_score = scores_poly_4
        print(grid_poly_4.best_params_)
        grid_search = svc_poly_4
        
        
    print("Y con un accuracy 5-cross validation: %0.4f (+/- %0.4f)" % (mejor_score.mean(), mejor_score.std() * 2))

    # guardamos el clasificador
    with open("mejor_clasificador.pkl", "wb") as archivo:
        pickle.dump(grid_search, archivo)
        
