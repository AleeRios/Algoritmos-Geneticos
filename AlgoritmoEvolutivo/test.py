#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: 

Author: Dr. Asdrúbal López Chau

Descripción:  Script de pruebas

Created on Mon Feb 28 13:33:22 2022

@author: asdruballopezchau
"""

from AlgoritmoEvolutuvo import AlgoritmoEvolutivo

ae = AlgoritmoEvolutivo(300, "ingenieriaencomputacioncuuaemzumpango")
ae.inicializa()
ae.showPob(False)
for i in range(400):
    ae.evolucion()
print("------------")
ae.showPob(True)
