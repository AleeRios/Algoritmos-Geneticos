#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Author: Dr. Asdrúbal López Chau

Descripción:  Algoritmo genético V1.0

Created on Mon Mar  7 12:48:33 2022

@author: asdruballopezchau
"""
import numpy as np
import random
from Individuo import Individuo
from Poblacion import Poblacion
from FitnessFunction import FitnessFunction
from Seleccion import Seleccion

class AlgoritmoEvolutivo:
    
    def __init__(self, size=100, target="icoic"):
        self.sizeInd = len(target)
        self.size = size
        self.pob = None
        self.target = target
        
    def showPob(self, showAptitude=False):
        if showAptitude:
            aptitudes = [self.ff.evaluate(ind) 
                     for ind in self.pob.poblacion]
            
        for i in range(self.size):
            if showAptitude:
                print(self.pob.poblacion[i].__str__() +
                      " -> " + str(aptitudes[i]))
            else:
                print(self.pob.poblacion[i])
        
    def inicializa(self):
        pob = Poblacion(self.target, self.size)
        pob.inicializa()
        self.pob = pob
        self.seleccion = Seleccion()
        self.ff = FitnessFunction(self.target)
        

    def evolucion(self):
        # 1) Evaluar individuos
        # 2) Seleccionar padres para cruza
        # 3) Generar hijos (cruza)
        # 4) Mutar a algunos
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente población
        ####### Implementación #############
        if self.pob is None:
            print("Inicialice la población")
            return
        #1) Evaluar individuos
        poblacion = self.pob.poblacion        
        aptitudes = [self.ff.evaluate(ind) 
                     for ind in poblacion]
        # # 2) Seleccionar padres para cruza
        k = int(self.size/2)
        if k%2 == 1:
            k += 1
        idx = self.seleccion.selecciona(aptitudes,
                                  k)
        #3) Generar hijos (cruza)
        descendencia = []
        for i in list(range(0,k-1,2)):
            ip = idx[i]
            im = idx[i+1]
            papa = poblacion[ip]
            mama = poblacion[im]
            hijos = papa.cruza(mama)
            descendencia.append(hijos[0])
            descendencia.append(hijos[1])
        
        # 4) Mutar a algunos (5%)
        totalMutar = int(np.ceil(len(descendencia)*0.1))
        
        for i in range(totalMutar):
            idx = random.choice(range(len(descendencia)))
            descendencia[idx].mutar()
        # 5) Evaluar hijos
        # 6) Seleccionar miembros de la siguiente 
        #     población
        
        # Junto padres e hijos
        for hijo in descendencia:
            poblacion.append(hijo)
        # calculo aptitudes de todos
        aptitudes = [self.ff.evaluate(ind) 
                     for ind in poblacion]
        # ELITISMO!!!!!
        idxMejor = np.argmax(aptitudes)
        # El mejor pasa directamente a la siguiente población
        siguientePob = []
        siguientePob.append(poblacion[idxMejor])
        # Selecciono indices de 
        # individuos para la siguiente generacion
        idx = self.seleccion.selecciona(aptitudes,
                                  self.size)
        # Creo la lista de individuos de la siguiente
        # generación

        for i in idx:
            siguientePob.append(poblacion[i])
        # Guardo para la siguiente evolución
        self.pob.poblacion = siguientePob

        







