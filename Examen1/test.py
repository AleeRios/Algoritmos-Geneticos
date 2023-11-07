#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTOMA DEL ESTADO DE MEXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos geneticos

Tema: Algoritmo genetico

Alumnos: Bladimir Axley Garduño Sanchez
         Beckham Alejandro Rios Campusano
         Emmanuel Vazquez Bravo

Descripcion:  test

Created on Mon Mar 28 19:48:42 2022

@author: alebe
"""

from AE import AlgoritmoEvolutivo

ae = AlgoritmoEvolutivo(200, [1,2,3,4,5,6,7,8,9,10])
ae.inicializa()
ae.showPob(True)
for i in range(100):
    ae.evolucion()
print("------------")
ae.showPob(True)
