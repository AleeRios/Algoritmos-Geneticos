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

from CromosomaReal import CromosomaReal as cr  #importamos CromosomaReal

class Individuo:  #definimos la clase Individuo 
    
    def __init__(self, minn, maxx, bits):  #definimos la funcion __init__
        self.min = minn #self.min es igual a minn
        self.max = maxx #self.max es igual a maxx
        self.bits = bits #self.bits es igual a bits
        self.cromosoma = cr(self.min, self.max, self.bits)#self.cromosoma es igual a cr
        
    def init(self): #definimos la funcion init
        self.cromosoma.init() #inicializamos el cromosoma
        
    def cruza(self, madre): #definimos la funcion cruza
        papa = cr(self.min, self.max, self.bits) #papa e s igual a un cromosoma
        papa.init() #inicializamos al papa
        mama = cr(self.min, self.max, self.bits) #mama es igual a un cromosoma real
        mama.init() #inicializamos a la mama
        hijos = papa.cruzar(mama) #hijo es igual a una cruza entre el papa y la mama
        h1 = Individuo(self.min, self.max, self.bits) #h1 es un individuo
        h1.cromosoma = hijos[0] #h1.cromosoma es igual a hijo[0]
        h2 = Individuo(self.min, self.max, self.bits) #h2 es un individuo
        h2.cromosoma = hijos[1] #h2.cromosoma es igual a hijos[1]
        return [h1, h2]  #regresamos h1 y h2
    
    def __str__(self): #definimos la funcion __str__
        return self.cromosoma.__str__() 
    
    def mutar(self): #definimos la funcion mutar
        self.cromosoma.mutar() #realizamos la mutacion
        
        
        
        
        