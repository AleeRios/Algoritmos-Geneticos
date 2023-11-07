#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:23:46 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Test
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

from Ecuacion import Ecuacion as ec
from AlgoritmoEvolutivo import AE as ae
import numpy as np

def resultado(n, coefi, m):
    s = ""

    for i in range(n):
        if coefi[i] >= 0:
            s += "+" + str(coefi[i]) + "(" + str(m[i]) + ")"
        else:
            s += str(coefi[i]) + "(" + str(m[i]) + ")"

    if(s[0] == "+"):
        s = s.replace("+", "", 1)

    s += "=" + str(np.dot(coefi, m))
    return s

n = int(input("\nIngresa la cantidad de coeficientes (<=10): "))
ec = ec(n)
coefi, res, ecu = ec.generar()
maxx = ec.max
minn = ec.min
bits = ec.bits

print("\n\t\tLa ecuacion es: ", ecu)

alEv = ae(res, coefi, maxx, minn, bits, 100)

for i in range(100):
    alEv.evolucion()
    
print("\n-----------------")
print("\n\t\tUltima Poblacion: ", end="\n\n")
alEv.showPob(True)

m = alEv.mejorSolucion()

print("\n\n\t\tLa mejor solucion es: ", m)


print("\n\n\t\tLa solucion es: ", resultado(n, coefi, m))
