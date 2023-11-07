#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: 

Author: Dr. Asdrúbal López Chau

Descripción:  Clase fitnessfunction
evalua individuos para el problema de 
encontrar contraseña

Created on Mon Mar  7 11:13:53 2022

@author: asdruballopezchau
"""

class FitnessFunction:
    
    def __init__(self, target="holam"):
        self.target = target
    
    def evaluate(self, ind):
        '''
        Evalua la aptitud de un individuo
        Parameters
        ----------
        ind : Individuo
            DESCRIPTION. Representa una
            contraseña

        Returns
        -------
        int
            DESCRIPTION. Aptitud del 
            individuo es la cantidad de
            letras en la posicion correcta

        '''
        intento = ind.cromosoma
        ctr = 0
        for letraP, letraC in zip(self.target, intento):
            if letraP == letraC:
                ctr += 1        
        return ctr
    
        