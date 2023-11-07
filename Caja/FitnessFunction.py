#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos Geneticos

Author: Beckham Alejandro Rios Campusano
        Bladimir Axley Garduño Sanchez
        Emmanuel Vazquez Bravo

Descripción:  Clase fitnessfunction
evalua individuos para el problema de 
encontrar contraseña

Created on Mon Mar  7 11:13:53 2022

@author: alebe
"""

#En esta clase crearemos y evaluaremos los valores del cromosoma para la descomposicion y la cantidad de letras 
import numpy as np

class FitnessFunction:
    
    def __init__(self, target):
        self.target = target
        self.lamda  = 1
        self.beta = 1
    
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
        intento = ind
        ladosCaja = intento.cromosoma.getValues()
        vol = 1
        for lado in ladosCaja:
            vol = vol * lado
        x = np.abs(self.target - vol)
        return self.beta*np.exp(-self.lamda*x)
    
        