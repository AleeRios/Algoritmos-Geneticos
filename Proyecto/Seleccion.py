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

import numpy as np
import random

class Seleccion:
    
    def selecciona(self, apti, k=2):
        apti = np.array(apti) + .01
        prob = [np.exp(apt) / np.sum(np.exp(apti)) for apt in apti]
        indices = list(range(len(apti)))
        return random.choices(indices, prob, k=k)