#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: ALGORITMOS GENETICOS
Tema: Reprecentacion real
Author: 
    Emmanuel Vazquez Bravo
    Bladimir Axley Garduño Sanchez
    Beckham Alejandro Rios Campusano
Profesor: Dr. Asdrúbal López Chau
Descripción: Reprecentacion real para algoritmos geneticos
 
Created on Mon Apr 25 12:10:35 2022
 
@author: DELL
"""
import numpy as np
import random
class GenReal:
    
    
    def __init__(self, min=-1.,max=1.,nbits=16):
        self.min=min
        self.max=max
        self.delta=np.abs(min-max)/2**nbits
        self.nbits=nbits
        #gencer=min+(delx*numpar)    

    def init(self):
        self.gen=random.choices([0,1], k=self.nbits)
        while not self.isValid():
                self.gen = random.choices([0, 1], 
                                          k=self.nbits)
                
    def isValid(self):
        value = self.getValue()
        if value >= self.min and value <= self.max:
            return True
        else:
            return False 
    
    def cruzar(self, mama):
        padre=self.gen.copy()
        madre=mama.gen.copy()
        cp1 = int(np.ceil((self.nbits)/3.))
        cp2 = 2 * cp1
        son1 = padre[0:cp1]
        son1.extend(madre[cp1:cp2])
        son1.extend(padre[cp2:])
        #print(padre)
        #print(madre)
        
        son2 = madre[0:cp1]
        son2.extend(padre[cp1:cp2])
        son2.extend(madre[cp2:])
        
        s1 = GenReal(self.min, self.max,self.nbits)
        s2 = GenReal(self.min, self.max,self.nbits)
        s1.gen = son1
        s2.gen = son2
        #print(s1)
        #print(s2)
        return[s1,s2]
    def mutar(self):
        self.init()
    
    def __str__(self):
        return str(self.gen)
    
    def getValue(self):
        particion=int(''.join([str(i) for i in self.gen]), 2)
        #print("particion",particion)
        #print("delta",self.delta)
        #print("min", self.min)
        #print("max",self.max)
        #print("nbits",self.nbits)
        return self.min + self.delta*particion
        
    
    
    
    
    
    