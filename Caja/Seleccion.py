#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: 
Alumno: Emmanuel Vazquez Bravo
        Bladimir Axley Garduño Sanchez
        Beckham Alejandro Rios Campusano
Profesor: Dr. Asdrúbal López Chau
Descripción: 
 
Created on Mon Mar  7 11:38:59 2022
 
@author: DELL
"""
import numpy as np
import random

class Seleccion:
    
    def selecciona(self, aptitudes, k=2):
        #darle chanse a los feos
        aptitudes= np.array(aptitudes) + .01
        '''  
        denom= np.sum(np.exp(aptitudes))
        probabilidades = []
        for aptitud in aptitudes:
        probabilidades.append(np.exp(aptitud)/denom)
        '''
        probabilidades = [np.exp(aptitud)/np.sum(np.exp(aptitudes)) for aptitud in aptitudes] 
        indices = list(range(len(aptitudes)))
        return random.choices(indices, probabilidades, k=k)