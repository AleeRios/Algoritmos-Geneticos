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

import numpy as np  #importamos numpy

class FitnessFunction:  #declaramos la clase FitnessFunction
    
    def __init__(self, target, coefi):  #definimos la funcion __init__
        self.target = target #self.target es igual a target
        self.coefi = coefi #self.coefi es igual a coefi
        self.lamda = 1  #self.lamda es igual a 1
        self.beta = 1 #beta es igual a 1
        
    def evaluar(self, ind): #definimos la funcion evaluar
        var = ind.cromosoma.getValues()   #var es igual a ind.cromosoma.getValues
        acti = np.dot(var, self.coefi)  #acti es igual a el producto punto de var y coefi
        res = abs(self.target - acti) #res es igual al valor absoluto de target - acti
        return self.beta * np.exp(-self.lamda * res)  #devolvemos beta*np.exp(-self.lamda * res)
    
    
    
    
    
    
    
    
    