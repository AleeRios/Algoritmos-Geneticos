#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: 

Author: 
    Emmanuel Vazquez Bravo
    Bladimir Axley Garduño Sanchez
    Beckham Alejandro Rios Campusano

Descripción:  

Created on Mon Apr 18 13:17:14 2022

@author: asdruballopezchau
"""
from GenEntero import GenEntero as Entero

class CromosomaEntero:
    
    def __init__(self, minis, maxis):
        if len(minis) != len(maxis):
            return
        self.minis = minis.copy()
        self.maxis = maxis.copy()
        self.genes = []
        for min, max in zip(minis, maxis):
            gen = Entero(min, max)
            self.genes.append(gen)
            
    def init(self):
        for gen in self.genes:
            gen.initGen()

    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + gen.__str__()
        return cad

    def getValues(self):
        values = []
        for gen in self.genes:
            values.append(gen.getValue())
        return values

    def cruzar(self, madre):
        genesHijos1 = []
        genesHijos2 = []
        for papa, mama in zip(self.genes, madre.genes):
            g = papa.cruzar(mama)
            genesHijos1.append(g[0])
            genesHijos2.append(g[1])
        h1 = CromosomaEntero(self.minis, self.maxis)
        h2 = CromosomaEntero(self.minis, self.maxis)
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]
    
    def mutar(self):
        self.init()
        
        