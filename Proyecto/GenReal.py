#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:23:26 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Gen Real
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""
 
import numpy as np
import random as rd

class GenReal:
    
    def __init__(self, minn, maxx, bits=8):
        self.min = minn
        self.max = maxx
        self.bits = bits
        self.delta = abs(minn - maxx) / 2 ** self.bits
        
    
    def init(self):
        self.gen = rd.choices([0,1], k=self.bits)
        while(not self.isValid()):
            self.gen = rd.choices([0,1], k=self.bits)
    
    def isValid(self):
        v = self.getValue()
        if v >= self.min & v <= self.max:
            return True
        else:
            return False
    
    def cruzar(self, mama):
        padre = self.gen.copy()
        madre = mama.gen.copy()
        cp1 = int(np.ceil((self.bits)/3))
        cp2 = 2 * cp1
        son1 = padre[0:cp1]
        son1.extend(madre[cp1:cp2])
        son1.extend(padre[cp2:])
        
        son2 = madre[0:cp1]
        son2.extend(padre[cp1:cp2])
        son2.extend(madre[cp2:])
        
        s1 = GenReal(self.min, self.max, self.bits)
        s2 = GenReal(self.min, self.max, self.bits)
        
        s1.gen = son1
        s2.gen = son2
        
        return [s1, s2]
    
    def mutar(self):
        self.init()
        
    def __str__(self):
        return str(self.gen)
    
    def getValue(self):
        part = int("".join([str(i) for i in self.gen[:]]), 2)
        return round(self.min + self.delta * part)