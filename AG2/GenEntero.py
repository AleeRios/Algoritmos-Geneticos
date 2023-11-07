#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos Genéticos

Author: 
    Emmanuel Vazquez Bravo
    Bladimir Axley Garduño Sanchez
    Beckham Alejandro Rios Campusano

Descripción:  Representación entera 

Created on Mon Apr  4 11:55:16 2022

@author: asdruballopezchau
"""
import numpy as np
import random

class GenEntero:
    
    def __init__(self, mini, maxi):
        # Calcular el numero de bits necesarios
        max = np.max([np.abs(maxi), np.abs(mini)])        
        self.nbits = 1 + int(np.ceil(np.log(max)/np.log(2)))
        self.maxi = maxi
        self.mini = mini
        
    def initGen(self):
        # Inicializa el gen pseudoaletoriamente con 
        # ceros y unos
            self.gen = random.choices([0, 1], 
                                      k=self.nbits)
            while not self.isValid():
                self.gen = random.choices([0, 1], 
                                          k=self.nbits)
            
    def isValid(self):
        value = self.getValue()
        if value >= self.mini and value <= self.maxi:
            return True
        else:
            return False            
    
    def getValue(self):
        #Regresa el valor entero que representa el gen
        value = int(''.join([str(i) for i 
                     in self.gen[1:]]), 2)
        if self.gen[0] == 1:
            value = -value
        
        return value
    
    def cruzar(self, genMadre):
        # Aplica cruza de este gen con el gen de la madre
        padre = self.gen.copy()
        madre = genMadre.gen.copy()
        cp1 = int(np.ceil((self.nbits - 1)/3.))
        cp2 = 2 * cp1
        son1 = padre[0:cp1]
        son1.extend(madre[cp1:cp2])
        son1.extend(padre[cp2:])
        
        son2 = madre[0:cp1]
        son2.extend(padre[cp1:cp2])
        son2.extend(madre[cp2:])
        
        s1 = GenEntero(self.mini, self.maxi)
        s2 = GenEntero(self.mini, self.maxi)
        s1.gen = son1
        s2.gen = son2
        # TODO: PrevenIMSS hijos inválidos
        # (Método Preventivo o "más vale prevenir que
        # bautizar")
        # a) Por módulo
        # b) Crear nuevo individuo (mutar)
        # c) crosspoint aleatorio
        # d) Otros
        '''if s1.getValue() > self.maxi:
            valor1=s1.getValue()%self.maxi+1
            print("el valor del hijo  es:",valor1)
            s1=valor1
        if s1.getValue() < self.mini:
            valor2=s1.getValue()%self.mini-1
            print("el valor del hijo es:",valor2)
            s1=valor2
        '''
        print("s1:",s1.getValue())
        
        print("s2:",s2.getValue())
        #print("maxi:",self.maxi)
        #print("mini:",self.mini)
        
        if s1.getValue()>self.maxi:
            valor1=int(s1.getValue()%(self.maxi+1))
            print("valor1",valor1)
            numero_decimal=valor1
            modulos1 = []
            while numero_decimal != 0:
                 # se almacena el módulo en el orden correcto
                 modulos1.insert(0, numero_decimal % 2)
                 numero_decimal //= 2
            print(modulos1)
            tam=8-len(modulos1)
            for i in range (tam):
                 modulos1.insert(0, 0)
            print("Este es tu nuevo hijo",modulos1)
            s1.gen = modulos1
            
            
        if s2.getValue()>self.maxi:
            valor2=int(s2.getValue()%(self.maxi+1))
            print("valor2",valor2)
            numero_decimal=valor2
            modulos2 = []
            while numero_decimal != 0:
                 # se almacena el módulo en el orden correcto
                 modulos2.insert(0, numero_decimal % 2)
                 numero_decimal //= 2
            print(modulos2)
            tam2=8-len(modulos2)
            for i in range (tam2):
                 modulos2.insert(0, 0)
            print("Este es tu nuevo hijo",modulos2)
            s2.gen = modulos2

        if s1.getValue()<self.mini:
            valor1=int(s1.getValue()%(self.mini-1))
            print("valor1",valor1)
            #s1=valor1
            numero_decimal=valor1
            modulos3 = []
            while numero_decimal != 0:
                 # se almacena el módulo en el orden correcto
                 modulos3.insert(0, numero_decimal % 2)
                 numero_decimal //= 2
            print(modulos3)
            tam3=8-len(modulos3)
            for i in range (tam3):
                 modulos3.instert(0, 0)
                 
            modulos3.insert(0, 1) 
            print("Este es tu nuevo hijo",modulos3)
            s1.gen = modulos3
        
        if s2.getValue()<self.mini:
            valor2=int(s2.getValue()%(self.mini-1))
            print("valor2",valor2)
            #s2=valor2
            numero_decimal=valor2
            modulos4 = []
            while numero_decimal != 0:
                 # se almacena el módulo en el orden correcto
                 modulos4.insert(0, numero_decimal % 2)
                 numero_decimal //= 2
            print(modulos4)
            tam4=8-len(modulos4)
            for i in range (tam4):
                 modulos4.instert(0, 0)
                 
            modulos4.insert(0, 1) 
            print("Este es tu nuevo hijo",modulos4)
            s2.gen = modulos4
           
        return [s1, s2]
   
        
    def mutar(self):
        self.initGen()
        
    def __str__(self):
        # Regresa el gen como cadena de ceros y unos
        return str(self.gen)
        
        
        
        
        
        
        
        
        
        
        