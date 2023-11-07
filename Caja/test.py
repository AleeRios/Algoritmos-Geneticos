#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU: UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: 
Alumno: Emmanuel Vazquez Bravo
        Bladimir Axley Garduño Sanchez
        Beckham Alejandro Rios Campusano
Profesor: Dr. Asdrúbal López Chau
Descripción: 
 
Created on Mon May  2 13:08:54 2022
 
@author: DELL
"""
import numpy as np
from CromosomaReal import CromosomaReal as Real
from FitnesFunction import FitnesFunction as FF
from AlgoritmoEvolutivo import AlgoritmoEvolutivo as alge
from Individuo import Individuo
from Poblacion import Poblacion
#h, w, l

volumen=int(input("Ingrese el valor de su volumen: "))
k=np.power(volumen, 1/3)
minimos = [k/3, k/3, 3*k]
maximos = [k/2, k/2, 4*k]
nbits= [16,16,16]
'''
r = Real(minimos, maximos, nbits)
r.init()
print(r.__str__())
print(r.getValues())
f=FF(11)
print("fitness = "+str(f.evaluate(r)))
r2 = Real(minimos, maximos, nbits)
r2.init()
print(r2.__str__())
print(r2.getValues())
print("fitness = "+str(f.evaluate(r2)))
'''
muestras=alge(100,volumen,minimos,maximos,nbits)
muestras.inicializa()
print("poblacion ")
muestras.showPob(True)
for i in range(10):
    muestras.evolucion()
muestras.showPob(True)
muestras.graficar(True)
