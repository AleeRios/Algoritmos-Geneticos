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

from Individuo import Individuo  #importamos a Individuo

class Poblacion:    #definimos la clase Poblacion 
    
    def __init__(self, size, minn, maxx, bits): #definimos la funcion __init__
        self.size = size #self.size es igual a size
        self.min = minn #self.min es igual a minn
        self.max = maxx #self.max es igual a maxx
        self.bits = bits #self.bits es igual a bits
        
    def inicializa(self): #definimos la funcion inicializa
        pob = [] #pob es igual a un arreglo
        for i in range(self.size): #hacemos un ciclo que valla esde 0 hasta lo que valg size
            ind = Individuo(self.min, self.max, self.bits)  #ind es igual a un individuo 
            ind.init()  #ind inicializa
            pob.append(ind) #ingresamos el individuo a pob
        self.pob = pob #self.pob es igual a pob
        
        
        
        
        