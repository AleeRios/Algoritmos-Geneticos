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

import numpy as np   #importamos numpy
import random as rd  #importamos random
from Poblacion import Poblacion as pob #importamos Poblcion
from Seleccion import Seleccion as sel  #importamos Seleccion
from FitnessFunction import FitnessFunction as ff  #importamos FitnessFunction

class AE:  #declaramos la clase AE
    
    def __init__(self, target, coefi, maxx, minn, bits, tam):  #definimos la funcion __init__
        self.target = target  #self.target es igual a target 
        self.coefi = coefi    #self.coefi es igual a coefi
        self.max = maxx      #self.max es igual a maxx
        self.min = minn      #self.min es igual a minn
        self.bits = bits    #self.bits es igual a bits
        self.tam = tam      #self.tam es igual a tam
        self.pob = pob(self.tam, self.min, self.max, self.bits)   #self.pob es igual a pob
        self.pob.inicializa()
        self.sel = sel()   #self.sel es igual a sel
        self.ff = ff(self.target, self.coefi)  #self.ff es igual a ff
        
    def showPob(self, sA=False):  #declaramos la funcion showPob 
        if sA:  
            apti = [self.ff.evaluar(i) for i in self.pob.pob]
            
        for i in range(self.tam):  #ciclo que valla desde 0 hasta lo que valga tam
            if sA:  
                print(self.pob.pob[i].cromosoma.getValues(), " ---> ", apti[i])  #imprimimos el valor de nuestra poblaacion y de la aptitud
            else: #de otro caso
                print(self.pob.pob[i])  #imprimimos la poblacion 
    """
    def inicializa(self):
        poblacion = pob(self.tam, self.min, self.max, self.bits)
        poblacion.inicializa()
        self.pob = poblacion
        
        self.sel = sel()
        self.ff = ff(self.target, self.coefi)
        """
    
    def evolucion(self):#definimos la funcion evolucion
        pobla = self.pob.pob  #pobla es igual a poblacion
        apti = [self.ff.evaluar(i) for i in pobla]  
        
        k = int(self.tam/2)  #k es igual a tamaño entre 2
        if k % 2 == 1: #si k modulo 2 es igual a 1 entonces 
            k += 1      #k sumara 1
        
        idx = self.sel.selecciona(apti, k) #idx es igual a sel.selecciona(apti , k)
        
        des = []  #des es igual a una lista
        for i in list(range(0, k-1, 2)):
            iP = idx[i]     #iP es igual a idx[i]
            iM = idx[i+1]   #iM es igual a idx[i+1]
            papa = pobla[iP] #papa es igual a pobla[iP]
            mama = pobla[iM]    #mama es igual a pobla[iM]
            hijos = papa.cruza(mama)  #hijos es igual a una cruza entre el papa y la mama
            des.append(hijos[0])  #des ingresara hijos[0]
            des.append(hijos[1])    #des ingresara hijos[1]
        
        totalMutar = int(np.ceil(len(des) * .1))  #
        
        for i in range(totalMutar): #ciclo que va desde 0 hasta que sea el valor de totalMutar
            idx = rd.choice(range(len(des)))  #idx es igual a rd.choice(range(len(des)))
            des[idx].mutar()  #mutamos des[idx]
        
        for h in des:  
            pobla.append(h)  #pobla ingresa h
            
        apti = [self.ff.evaluar(i) for i in pobla]  
        
        idxM = np.argmax(apti)  #idxM es igual a el argumento maximo de apti
        sigPob = [] #sigPob es igual a una lista
        sigPob.append(pobla[idxM])  #siguiente poblcion ingresara a pobla[idxM]
        
        idx = self.sel.selecciona(apti, self.tam) #idx es igual a la seleccion de selecciona
        
        for i in idx:  
            sigPob.append(pobla[i])  #sigPob ingresara a pobla[i]
        
        self.pob.pob = sigPob #self.pob.pob es igual a sigPob
        
    def mejorSolucion(self):   #definimos la funcion mejorSolucion
        apti = [self.ff.evaluar(i) for i in self.pob.pob]  
        idxM = np.argmax(apti) #idxM es igual a el argumento maximo de apti
        return self.pob.pob[idxM].cromosoma.getValues()  #regreamos el valor que tengamos en pob.pob[idxM]
    
    
    
    
    
    
    