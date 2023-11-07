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
Descripción: Clase fitnessfunction evalua individuos par el problema de 
encontrar contraseña
 
Created on Mon Mar  7 11:13:56 2022
 
@author: DELL
"""

import numpy as np
class FitnesFunction:
    def __init__(self, target):
        self.target = target
        self.lamda = 1
        self.beta = 1
        
    def evaluate(self, ind):
        '''
        Evalua la aptitud de un individuo
        Parameters
        ----------
        ind : Individuo
            DESCRIPTION. Representa una contraseña

        Returns
        -------
        int
            Description. Aptitud del individuo es la cantidad de letras
            en la posicion correcta

        '''
        intento = ind  #cambio
        ladosCaja = intento.cromosoma.getValues()
        vol=1
        
        for lado in ladosCaja:
            vol=vol*lado
        x= np.abs(self.target-vol)

        return self.beta*np.exp(-self.lamda*x)
        
        
        
        
        
        