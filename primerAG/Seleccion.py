#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Author: Dr. Asdrúbal López Chau

Descripción:  Mecanismo de selección

Created on Mon Mar  7 11:38:30 2022

@author: asdruballopezchau
"""
import numpy as np
import random
class Seleccion:
    
    def selecciona(self, aptitudes, k=2):
        # Darle chance a los feos
        aptitudes = np.array(aptitudes) + .01
        '''        
        denom = np.sum(np.exp(aptitudes))
        probabilidades = []
        for aptitud in aptitudes:
            probabilidades.append(np.exp(aptitud)/denom)
        '''
        probabilidades = [np.exp(aptitud)/np.sum(np.exp(aptitudes))
                  for aptitud 
                  in aptitudes]
        indices = list(range(len(aptitudes)))
        return random.choices(indices, probabilidades, k=k)
        
        











