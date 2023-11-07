#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: 

Author: Dr. Asdrúbal López Chau

Descripción:  Primer Algoritmo Genético. Clase Individuo.

Created on Mon Feb 28 12:26:50 2022

@author: asdruballopezchau
"""
import random
import numpy as np
class Individuo:
    
    def __init__(self):
        self.alfabeto = "abcdefghijklmnopqrtsuvwxyz"
        self.cromosoma = ""
    
    def init(self, sizeInd=5):
        self.cromosoma = ''.join(random.choices(self.alfabeto, k=sizeInd))
        self.sizeInd = sizeInd 
    
        
        
        
    def cruza(self, mother):
        padre = str(self.cromosoma)
        madre = str(mother.cromosoma)
        mitad = int(self.sizeInd/2)
        son1 = padre[0:mitad] + madre[mitad:]
        son2 = madre[0:mitad] + padre[mitad:]
        ind1 = Individuo()
        ind1.sizeInd = self.sizeInd 
        ind1.cromosoma = son1
        ind2 = Individuo()
        ind2.sizeInd = self.sizeInd 
        ind2.cromosoma = son2
        return [ind1, ind2]
    
    def __str__(self):
        return self.cromosoma
    
    def mutar(self):
        idx = np.random.randint(self.sizeInd)
        cambiar = ''.join(random.choices(self.alfabeto, k=1))
        self.cromosoma =  list(self.cromosoma)
        self.cromosoma[idx] = cambiar
        self.cromosoma = ''.join(self.cromosoma)

        
        
    


'''
# 1) Representación de la solución: La cromosoma será
una cadena de 5 caracteres. Cada gen es un caracter.
# 2) Función de evaluación o aptitud: Es el número de letras
en posición correcta.
# 3) Selección de progenitores: Mayor aptitud, más probabilidad
de ser elegido.
# 4) Operadores genéticos: 
#    a) Cruza: Cruza por un punto.
#    b) Mutación: Cambiar un gen (letra) mediante un proceso
                estocástico
'''