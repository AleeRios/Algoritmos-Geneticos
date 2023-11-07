#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: ALGORITMOS GENETICOS
Tema: Reprecentacion real
Author: 
    Emmanuel Vazquez Bravo
    Bladimir Axley Garduño Sanchez
    Beckham Alejandro Rios Campusano
Profesor: Dr. Asdrúbal López Chau
Descripción: cromosoma real para algoritmos geneticos
 
Created on Mon Apr 25 13:27:29 2022
 
@author: DELL
"""
from GenReal import GenReal as Real
class CromosomaReal:
    def __init__(self,minis,maxis,nbits):
        '''

        Parameters
        ----------
        minis : list
        DESCRIPTION valores minimos
        maxis : list
            DESCRIPTION. valores maximos
        nbits : list
            DESCRIPTION. Longitud de cada gen

        Returns
        -------
        None.

        '''
        if len(minis) != len(maxis):
            return
        self.nbits= nbits.copy()
        self.minis = minis.copy()
        self.maxis = maxis.copy()
        self.genes = []
        for min, max,nb in zip(minis, maxis,nbits):
            gen = Real(min, max,nb)
            self.genes.append(gen)
        
    
    def init(self):
        '''
        
        Returns
        -------
        None.

        '''
        for gen in self.genes:
            gen.init()
    
    def cruzar(self,madre):
        genesHijos1 = []
        genesHijos2 = []
        for papa, mama in zip(self.genes, madre.genes):
            g = papa.cruzar(mama)
            genesHijos1.append(g[0])
            genesHijos2.append(g[1])
        h1 = CromosomaReal(self.minis, self.maxis,self.nbits)
        h2 = CromosomaReal(self.minis, self.maxis,self.nbits)
        h1.genes = genesHijos1
        h2.genes = genesHijos2
        return [h1, h2]
    
    def mutar(self):
        self.init()
    
    def getValues(self):
        values = []
        for gen in self.genes:
            values.append(gen.getValue())
        return values
    def __str__(self):
        cad = ""
        for gen in self.genes:
            cad = cad + gen.__str__()
        return cad
    