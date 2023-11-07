#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTOMA DEL ESTADO DE MEXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos geneticos

Tema: Algoritmo genetico

Alumnos: Bladimir Axley Garduño Sanchez
         Beckham Alejandro Rios Campusano
         Emmanuel Vazquez Bravo

Descripcion:  Clase Seleccion

Created on Mon Mar 28 19:48:42 2022

@author: alebe
"""

import numpy as np
import random

class Seleccion:
    
    def seleccionaMult(self, aptitudes, k=2):
        aptitudes = np.array(aptitudes) + .01
        
        prob = [np.exp(aptitud)/np.sum(np.exp(aptitudes)) for aptitud in aptitudes]
        indices = list(range(len(aptitudes)))
        
        return random.choices(indices, prob, k=k)
    
    def seleccionaSuma(self, aptitudes, k=2):
        aptitudes = np.array(aptitudes) + .01
        
        prob = [np.exp(aptitud)/np.sum(np.exp(aptitudes)) for aptitud in aptitudes]
        indices = list(range(len(aptitudes)))
        
        return random.choices(indices, prob, k=k)