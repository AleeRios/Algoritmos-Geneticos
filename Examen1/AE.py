#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTOMA DEL ESTADO DE MEXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos geneticos

Tema: Algoritmo genetico

Alumnos: Bladimir Axley Garduño Sanchez
         Beckham Alejandro Rios Campusano
         Emmanuel Vazquez Bravo

Descripcion:  Clase Algoritmo Evolitivo

Created on Mon Mar 28 19:48:42 2022

@author: alebe
"""

import numpy as np
import random
from Poblacion import Poblacion
from Fitness import FitnessFunction
from Seleccion import Seleccion

class AlgoritmoEvolutivo:
    
    def __init__(self, size=100, target=[1,2,3,4,5,6,7,8,9,10]):
        self.sizeInd = len(target)
        self.size = size
        self.pob = None
        self.target = target
        
    def inicializa(self):
        pob = Poblacion(self.target, self.size)
        pob.inicializa()
        self.pob = pob
        self.seleccion = Seleccion()
        self.ff = FitnessFunction()
    
    def showPob(self, show=False):
        if show:
            aptitudesMult = [self.ff.evaluateMult(ind) for ind in self.pob.poblacion]
            aptitudesSuma = [self.ff.evaluateSuma(ind) for ind in self.pob.poblacion]
        
        print("\t-----Aptitudes Multiplicacion-----")
        for i in range(self.size):
            if show:
                print(self.pob.poblacion[i].__strA__(), "--> " + str(aptitudesMult[i]), 
                      "Mul: ", np.prod(self.pob.poblacion[i].__strA__()))
            else:
                print(self.pob.poblacion[i].__strA__())
        
        print("\t-----Aptitudes Suma-----")
        for i in range(self.size):
            if show:
                print(self.pob.poblacion[i].__strB__(), "--> " + str(aptitudesSuma[i]), 
                      "Sum: ", np.sum(self.pob.poblacion[i].__strB__()))
            else:
                print(self.pob.poblacion[i].__strB__())
        
    def evolucion(self):
        if self.pob is None:
            print("Inicialice la poblacion")
            return
        
        poblacion = self.pob.poblacion
        aptitudesMult = [self.ff.evaluateMult(ind) for ind in self.pob.poblacion]
        aptitudesSuma = [self.ff.evaluateSuma(ind) for ind in self.pob.poblacion]
        
        k = int(self.size/2)
        if k % 2 == 1:
            k += 1
        idx = self.seleccion.seleccionaMult(aptitudesMult, k)
        idx2 = self.seleccion.seleccionaSuma(aptitudesSuma, k)
        
        descendenciaA = []
        for i in list(range(0,k-1,2)):
            ipA = idx[i]
            imA = idx[i+1]
            papa = poblacion[ipA]
            mama = poblacion[imA]
            hijos = papa.cruza(mama)
            descendenciaA.append(hijos[0])
            descendenciaA.append(hijos[1])
        
        descendenciaB = []
        for i in list(range(0,k-1,2)):
            ipA = idx2[i]
            imA = idx2[i+1]
            papa = poblacion[ipA]
            mama = poblacion[imA]
            hijos = papa.cruza(mama)
            descendenciaB.append(hijos[0])
            descendenciaB.append(hijos[1])
            
        totalMutarA = int(np.ceil(len(descendenciaA) * 0.1))
        for i in range(totalMutarA):
            idx = random.choice(range(len(descendenciaA)))
            descendenciaA[idx].mutarA()

        totalMutarB = int(np.ceil(len(descendenciaB) * 0.1))
        for i in range(totalMutarB):
            idx = random.choice(range(len(descendenciaB)))
            descendenciaB[idx].mutarB()
        
        for hijoA in descendenciaA:
            poblacion.append(hijoA)
        
        for hijoB in descendenciaB:
            poblacion.append(hijoB)
        
        aptitudesMult = [self.ff.evaluateMult(ind) for ind in self.pob.poblacion]
        aptitudesSuma = [self.ff.evaluateSuma(ind) for ind in self.pob.poblacion]
        
        idxMejor1 = np.argmax(aptitudesMult)
        idxMejor2 = np.argmax(aptitudesSuma)
        
        sigPobA = []
        sigPobA.append(poblacion[idxMejor1])
        
        sigPobB = []
        sigPobB.append(poblacion[idxMejor2])
        
        idx = self.seleccion.seleccionaMult(aptitudesMult, self.size)
        idx2 = self.seleccion.seleccionaSuma(aptitudesSuma, self.size)
        
        for i in idx:
            sigPobA.append(poblacion[i])
        
        for i in idx2:
            sigPobB.append(poblacion[i])
        
        self.pob.poblacion = sigPobA + sigPobB