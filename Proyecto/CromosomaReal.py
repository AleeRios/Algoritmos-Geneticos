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

from GenReal import GenReal as gr


class CromosomaReal:
    
    def __init__(self, minis, maxis, bits):
        if len(minis) != len(maxis):
            return
        
        self.bits = bits
        self.minis = minis.copy()
        self.maxis = maxis.copy()
        self.genes = []
        
        for minn, maxx, nb in zip(minis, maxis, bits):
            gen = gr(minn, maxx, nb)
            self.genes.append(gen)
    
    def init(self):
        for gen in self.genes:
            gen.init()
    
    def cruzar(self, madre):
        genHijos1 = []
        genHijos2 = []
        
        for papa, mama in zip(self.genes, madre.genes):
            g = papa.cruzar(mama)
            genHijos1.append(g[0])
            genHijos2.append(g[1])
        
        h1 = CromosomaReal(self.minis, self.maxis, self.bits)
        h2 = CromosomaReal(self.minis, self.maxis, self.bits)
        h1.genes = genHijos1
        h2.genes = genHijos2
        
        return [h1, h2]
    
    def mutar(self):
        self.init()
        
    def getValues(self):
        val = []
        for gen in self.genes:
            val.append(gen.getValue())
        return val
    
    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad += gen.__str__()
        return cad