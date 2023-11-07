#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:19:42 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Algoritmo Evolutivo
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

import numpy as np
import random as rd
from Poblacion import Poblacion as pob
from Seleccion import Seleccion as sel
from FitnessFunction import FitnessFunction as ff

class AE:
    
    def __init__(self, target, coefi, maxx, minn, bits, tam):
        self.target = target
        self.coefi = coefi
        self.max = maxx
        self.min = minn
        self.bits = bits
        self.tam = tam
        self.pob = pob(self.tam, self.min, self.max, self.bits)
        self.pob.inicializa()
        self.sel = sel()
        self.ff = ff(self.target, self.coefi)
        
    def showPob(self, sA=False):
        if sA:
            apti = [self.ff.evaluar(i) for i in self.pob.pob]
            
        for i in range(self.tam):
            if sA:
                print(self.pob.pob[i].cromosoma.getValues(), " ---> ", apti[i])
            else:
                print(self.pob.pob[i])
    """
    def inicializa(self):
        poblacion = pob(self.tam, self.min, self.max, self.bits)
        poblacion.inicializa()
        self.pob = poblacion
        
        self.sel = sel()
        self.ff = ff(self.target, self.coefi)
        """
    
    def evolucion(self):
        pobla = self.pob.pob
        apti = [self.ff.evaluar(i) for i in pobla]
        
        k = int(self.tam/2)
        if k % 2 == 1:
            k += 1
        
        idx = self.sel.selecciona(apti, k)
        
        des = []
        for i in list(range(0, k-1, 2)):
            iP = idx[i]
            iM = idx[i+1]
            papa = pobla[iP]
            mama = pobla[iM]
            hijos = papa.cruza(mama)
            des.append(hijos[0])
            des.append(hijos[1])
        
        totalMutar = int(np.ceil(len(des) * .1))
        
        for i in range(totalMutar):
            idx = rd.choice(range(len(des)))
            des[idx].mutar()
        
        for h in des:
            pobla.append(h)
            
        apti = [self.ff.evaluar(i) for i in pobla]
        
        idxM = np.argmax(apti)
        sigPob = []
        sigPob.append(pobla[idxM])
        
        idx = self.sel.selecciona(apti, self.tam)
        
        for i in idx:
            sigPob.append(pobla[i])
        
        self.pob.pob = sigPob
        
    def mejorSolucion(self):
        apti = [self.ff.evaluar(i) for i in self.pob.pob]
        idxM = np.argmax(apti)
        return self.pob.pob[idxM].cromosoma.getValues()