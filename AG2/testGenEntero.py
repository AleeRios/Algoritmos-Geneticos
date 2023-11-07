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

Descripción:  Prueba del gen entero

Created on Mon Apr  4 12:02:39 2022

@author: asdruballopezchau
"""

from GenEntero import GenEntero

for i in range(5):
    papa = GenEntero(-100, 50)
    papa.initGen()
    print(papa.__str__())
    print(papa.getValue())
    mama = GenEntero(-100, 50)
    mama.initGen()
    print(mama.__str__())
    print(mama.getValue())

hijos = papa.cruzar(mama)

print(hijos[0].__str__())
print(hijos[0].getValue())
print(hijos[1].__str__())
print(hijos[1].getValue())

hijos[0].mutar()
print(hijos[0].__str__(), hijos[0].getValue(), sep=": ")