#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: ALGORITMOS GENETICOS
Tema: 
Author: 
    Emmanuel Vazquez Bravo
    Bladimir Axley Garduño Sanchez
    Beckham Alejandro Rios Campusano
Profesor: Dr. Asdrúbal López Chau
Descripción: test para el cromosoma real
 
Created on Sat Apr 30 12:04:42 2022
 
@author: DELL
"""

from CromosomaReal import CromosomaReal as CRea

minis = [-5.9, -1, 100]
maxis = [12, 0, 201.13]
nbits=[8,4,16]
papa= CRea(minis, maxis,nbits)
papa.init()
print("papa",papa.__str__())
print(papa.getValues())

mama= CRea(minis, maxis,nbits)
mama.init()
print("mama",mama.__str__())
print(mama.getValues())
hijos = papa.cruzar(mama)
print("hijo 0",hijos[0].__str__())
print(hijos[0].getValues())
print("hijo 2",hijos[1].__str__())
print(hijos[1].getValues())