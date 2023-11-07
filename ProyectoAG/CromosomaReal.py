#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 25 23:16:58 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Cromosoma Real
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

from GenReal import GenReal as gr  #imprtamos GenReal


class CromosomaReal: #definimos la clase CromosomaReal
    
    def __init__(self, minis, maxis, bits): #definimos la funcion __init__
        if len(minis) != len(maxis):    #si la longitud de min es diferente  la longitud de maxis entonces
            return
        
        self.bits = bits  #self.bits es igual a bits
        self.minis = minis.copy()   #self.minis es igual a minis.copy
        self.maxis = maxis.copy()   #self.maxis es igual a maxis.copy
        self.genes = []     #genes es igual a una lista
        
        for minn, maxx, nb in zip(minis, maxis, bits): 
            gen = gr(minn, maxx, nb) #gen es igual a gr(minn, maxx,nb)
            self.genes.append(gen) #genes ingresa a gen
    
    def init(self): #declaramos la funcion init
        for gen in self.genes:  #ciclo 
            gen.init()  ##inicializamos el gen
    
    def cruzar(self, madre):    #definimos la funcion cruzar
        genHijos1 = []      #genHijos1 es igual a un arreglo
        genHijos2 = []     #genHijos2 es igual a un arreglo
        
        for papa, mama in zip(self.genes, madre.genes): 
            g = papa.cruzar(mama) #g es igual a papa.cruzar(mama)
            genHijos1.append(g[0])  #genHijos1 ingrea g[0]
            genHijos2.append(g[1])  #genHijos2 ingresa g[1]
        
        h1 = CromosomaReal(self.minis, self.maxis, self.bits)  #h1 es igual a CromosomaReal
        h2 = CromosomaReal(self.minis, self.maxis, self.bits)  #h2 es igual a cromosomaReal
        h1.genes = genHijos1  #h1.genes es igual a genHijos1
        h2.genes = genHijos2  #h2.genes es igual a genHijos2
        
        return [h1, h2] #regresamos h1 y h2
    
    def mutar(self): #definimos la funcion mutar
        self.init() #inicialzamos 
        
    def getValues(self):    #definimos la funcion getValues
        val = []    #val es igual a un arreglo
        for gen in self.genes:  
            val.append(gen.getValue()) #ingresamos el valor a val
        return val #regresamos val
    
    def __str__(self):  #definimos la funcion __str__
        cad = ""  #cad es igual a una cadena vacia
        for gen in self.genes: 
            cad += gen.__str__() #imprimimo el valor de nuestros genes
        return cad #regresamos la cadena
    
    
    
    
    
    
    