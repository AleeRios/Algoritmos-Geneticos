#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:48:53 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Poblacion
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

from Individuo import Individuo

class Poblacion:
    
    def __init__(self, size, minn, maxx, bits):
        self.size = size
        self.min = minn
        self.max = maxx
        self.bits = bits
        
    def inicializa(self):
        pob = []
        for i in range(self.size):
            ind = Individuo(self.min, self.max, self.bits)
            ind.init()
            pob.append(ind)
        self.pob = pob