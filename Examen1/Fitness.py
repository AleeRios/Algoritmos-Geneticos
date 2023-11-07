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

Descripcion:  Clase FitnessFunction

Created on Mon Mar 28 19:48:42 2022

@author: alebe
"""

class FitnessFunction:
    
    def __init__(self, target=[1, 5, 3, 4, 6], target2=[2, 7, 8, 9, 10]):
        self.target = target
        self.target2 = target2
        #target2=[2, 7, 8, 9, 10]
        
    def evaluateMult(self, ind):
        intento = ind.grupoA
        ctr = 0
        
        for numT, numI in zip(self.target, intento):
            if numT == numI:
                ctr += 1
        return ctr
    
    def evaluateSuma(self, ind):
        intento2 = ind.grupoB
        ctr = 0
        
        for numT, numI in zip(self.target2, intento2):
            if numT == numI:
                ctr += 1
        return ctr