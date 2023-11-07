#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:59:58 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Seleccion
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

import numpy as np  #importamos numpy
import random #importamos random

class Seleccion: #definimos la clase Seleccion
    
    def selecciona(self, apti, k=2): #efinimos la funcion selecciona
        apti = np.array(apti) + .01  #apti es igual a np.array(apti) +0.1
        prob = [np.exp(apt) / np.sum(np.exp(apti)) for apt in apti]  
        indices = list(range(len(apti)))  #indices es igual a una lista que este en el rango de apti 
        return random.choices(indices, prob, k=k)