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
 
Created on Mon Mar  7 11:31:56 2022
 
@author: DELL
"""
from Individuo import Individuo

class Poblacion:
    
    def __init__(self, size,min,max,nb):
        self.size=size
        self.min=min
        self.max=max
        self.nb=nb
        
    def inicializa(self):
        poblacion=[]
        for i in range(self.size):
            ind = Individuo(self.min,self.max,self.nb)
            ind.init()
            poblacion.append(ind)
        self.poblacion=poblacion