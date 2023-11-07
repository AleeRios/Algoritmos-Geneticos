#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: 

Author: Dr. Asdrúbal López Chau

Descripción:  Población de individuos


Created on Mon Mar  7 11:31:12 2022

@author: asdruballopezchau
"""
from Individuo import Individuo

class Poblacion:
    
    def __init__(self, target, size=100):
        self.size = size
        self.target = target

    def inicializa(self):
        poblacion = []
        for i in range(self.size):
            ind = Individuo()
            ind.sizeInd = len(self.target)
            ind.init(len(self.target))
            poblacion.append(ind)
        self.poblacion = poblacion
        
        
        
        
        
        
        
        
        
        
        
        