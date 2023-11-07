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

Descripción:  Prueba de cromosoma entero

Created on Mon Apr 18 13:42:22 2022

@author: asdruballopezchau
"""

from CromosomaEntero import CromosomaEntero as CInt

minis = [-1000, 0, -2000, -500]
maxis = [1000, 120, 55, 0]
papa= CInt(minis, maxis)
papa.init()
print(papa.__str__())
print(papa.getValues())

mama= CInt(minis, maxis)
mama.init()
print(mama.__str__())
print(mama.getValues())
hijos = papa.cruzar(mama)

print(hijos[0].__str__())
print(hijos[0].getValues())

print(hijos[1].__str__())
print(hijos[1].getValues())


