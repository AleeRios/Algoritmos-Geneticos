#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTOMA DEL ESTADO DE MEXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Tema: Algoritmo genético

Alumnos: Bladimir Axley Garduño Sanchez
         Beckham Alejandro Rios Campusano
         Emmanuel Vazquez Bravo

Descripción:  Clase Individuo

Created on Mon Mar 28 19:48:42 2022

@author: alebe
"""

import random
import numpy as np

class Individuo:
    
    def __init__(self):
        self.alfabeto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.alfabeto2 = self.alfabeto
        self.grupoA = []
        self.grupoB = []
    
    def init(self, sizeInd=5):
        while len(self.grupoA) < 5:
            self.grupoA = list(set(random.choices(self.alfabeto, k=sizeInd)))
        
        for i in range (len(self.grupoA)):
            self.alfabeto.remove(self.grupoA[i])
        
        self.grupoB = self.alfabeto
        self.sizeInd = sizeInd
        
    def cruza(self, madre):
        mitad = int(self.sizeInd / 2)
        
        padreA = self.grupoA
        madreA = madre.grupoA
        padreB = self.grupoB
        madreB = madre.grupoB
        
        hijoA1 = padreA[:mitad] + madreA[mitad:]
        hijoA2 = madreA[:mitad] + padreA[mitad:]
        hijoB1 = padreB[:mitad] + madreB[mitad:]
        hijoB2 = madreB[:mitad] + padreB[mitad:]
        
        ind1 = Individuo()
        ind1.sizeInd = self.sizeInd
        ind1.grupoA = hijoA1
        ind1.grupoB = hijoB1
        
        ind2 = Individuo()
        ind2.sizeInd = self.sizeInd
        ind2.grupoA = hijoA2
        ind2.grupoB = hijoB2
        
        return [ind1, ind2]
    
    def __strA__(self):
        return self.grupoA
    
    def __strB__(self):
        return self.grupoB
    
    def mutarA(self):
        idx = np.random.randint(self.sizeInd)
        cambiar = random.choices(self.alfabeto2, k=1)
        self.grupoA[idx] = cambiar[0]
    
    def mutarB(self):
        idx = np.random.randint(self.sizeInd)
        cambiar = random.choices(self.alfabeto2, k=1)
        self.grupoB[idx] = cambiar[0]