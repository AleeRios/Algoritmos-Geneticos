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
 
import numpy as np   #importamos la libreri numpy
import random as rd  #importamos la libreria random

class GenReal:    #creo la clase GenReal
    
    def __init__(self, minn, maxx, bits=8): #definimos la funcion __init__
        self.min = minn   #self.min es igual a minn
        self.max = maxx   #self.max es igual a maxx
        self.bits = bits  #self.bits es igual a bits
        self.delta = abs(minn - maxx) / 2 ** self.bits  #self.delta es igual a el valor absoluto de minn-maxx
        
    
    def init(self): #definimos la funcion init
        self.gen = rd.choices([0,1], k=self.bits)  #self.gen es igual a valores aleatoreos entre 0 y 1
        while(not self.isValid()):   #si no es valido entonces
            self.gen = rd.choices([0,1], k=self.bits) #generamos el gen 
    
    def isValid(self):      #definimos la funcion isValid
        v = self.getValue()     #v es igual a self.getValue
        if v >= self.min & v <= self.max: #si v es mayor o igual a self.min y menor a self.max entonces
            return True   #es verdadero
        else:   #en otro caso 
            return False  #esfalso
    
    def cruzar(self, mama):  #definimos la funcion cruzar
        padre = self.gen.copy()     #padre es igual a gen.copy
        madre = mama.gen.copy()     #madre es igual a gen.copy
        cp1 = int(np.ceil((self.bits)/3))   #cp1 es igual a el numero de bits entre 3
        cp2 = 2 * cp1  #cp2 es igual a cp1 por 2
        son1 = padre[0:cp1] #son uno toma los bits del padre del bit 0 a cp1
        son1.extend(madre[cp1:cp2]) #son 1 toma los bits de la madre de cp1 a cp2
        son1.extend(padre[cp2:])    #son1 toma los bits del padre de cp2 hasta que termine
        
        son2 = madre[0:cp1]     #son2 es igual a los bits de la madre del bit 0 al bit cp1
        son2.extend(padre[cp1:cp2]) #son 2 toma los bits del padre de cp1 hasta cp2
        son2.extend(madre[cp2:])    #son2 toma los bits del cp2 hasta que termine
        
        s1 = GenReal(self.min, self.max, self.bits) #s1 es igual a un gen real
        s2 = GenReal(self.min, self.max, self.bits) #s2 es igual a un gen real
        
        s1.gen = son1 #s1.gen es igual a son1
        s2.gen = son2 #s2.gen es igual a son2
        
        return [s1, s2] #regresamos s1 y s2
    
    def mutar(self):    #definimos la funcion mutar
        self.init()     
        
    def __str__(self): #definimos la funcion __str__
        return str(self.gen)    #regresamos str(self.gen)
    
    def getValue(self): #definimos la funcion get value
        part = int("".join([str(i) for i in self.gen[:]]), 2) 
        return round(self.min + self.delta * part)
    
    
    
    
    