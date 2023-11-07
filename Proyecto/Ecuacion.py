#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:05:05 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Ecuacion
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

import random as rd

class Ecuacion:
    
    def __init__(self, numCo=1):
        self.numCo = numCo
        self.var = "xyzabcdefg"
        self.ecu = None
        self.coefi = None
        self.res = None
        
    def generar(self):
        coefi = []
        ecu = ""
        for i in range(self.numCo):
            c = rd.randint(-10, 10)
            coefi.append(c)
        self.coefi = coefi
        
        for i in range(len(self.coefi)):
            if coefi[i] >= 0:
                ecu += "+" + str(coefi[i])
                ecu += self.var[i]
            else:
                ecu += str(coefi[i]) + self.var[i]
        
        if(ecu[0] == "+"):
            ecu = ecu.replace("+", "", 1)
        
        self.res = rd.randint(-100, 100)
        ecu += "=" + str(self.res)
        self.ecu = ecu
        
        self.max = []
        self.min = []
        self.bits = []
        
        for i in range(self.numCo):
            if self.res > 0:
                self.max.append(self.res)
                self.min.append(-1 * self.res)
            else:
                self.min.append(self.res)
                self.max.append(-1 * self.res)
            self.bits.append(8)
        
        return self.coefi, self.res, self.ecu
