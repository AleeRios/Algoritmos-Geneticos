#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:40:13 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Individuo
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

from CromosomaReal import CromosomaReal as cr

class Individuo:
    
    def __init__(self, minn, maxx, bits):
        self.min = minn
        self.max = maxx
        self.bits = bits
        self.cromosoma = cr(self.min, self.max, self.bits)
        
    def init(self):
        self.cromosoma.init()
        
    def cruza(self, madre):
        papa = cr(self.min, self.max, self.bits)
        papa.init()
        mama = cr(self.min, self.max, self.bits)
        mama.init()
        hijos = papa.cruzar(mama)
        h1 = Individuo(self.min, self.max, self.bits)
        h1.cromosoma = hijos[0]
        h2 = Individuo(self.min, self.max, self.bits)
        h2.cromosoma = hijos[1]
        return [h1, h2]
    
    def __str__(self):
        return self.cromosoma.__str__()
    
    def mutar(self):
        self.cromosoma.mutar()