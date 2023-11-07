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

Descripción:  Clase Poblacion

Created on Mon Mar 28 19:48:42 2022

@author: alebe
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
            ind.init(int(len(self.target)/2))
            poblacion.append(ind)
        self.poblacion = poblacion