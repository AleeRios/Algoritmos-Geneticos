#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:56:29 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Fitness Function
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

import numpy as np

class FitnessFunction:
    
    def __init__(self, target, coefi):
        self.target = target
        self.coefi = coefi
        self.lamda = 1
        self.beta = 1
        
    def evaluar(self, ind):
        var = ind.cromosoma.getValues()
        acti = np.dot(var, self.coefi)
        res = abs(self.target - acti)
        return self.beta * np.exp(-self.lamda * res)