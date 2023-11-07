#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: Algoritmos Geneticos
Tema: 
Author: 
    Emmanuel Vazquez Bravo
    Bladimir Axley Garduño Sanchez
    Beckham Alejandro Rios Campusano
Profesor: Dr. Asdrúbal López Chau
Descripción: Test del gen real
 
Created on Sat Apr 30 10:56:00 2022
 
@author: DELL
"""

from GenReal import GenReal

for i in range(5):
    papa = GenReal(-100, 50,8)
    papa.init()
    print("papa",papa.__str__())
    print(papa.getValue())
    mama = GenReal(-100, 50,8)
    mama.init()
    print("mama",mama.__str__())
    print(mama.getValue())
    print("\n-------------------\n")

hijos = papa.cruzar(mama)
print("hijo 0",hijos[0].__str__())
print(hijos[0].getValue())
print("hijo 1",hijos[1].__str__())
print(hijos[1].getValue())
hijos[0].mutar()
print("hijo mutado",hijos[0].__str__())
print(hijos[0].getValue())