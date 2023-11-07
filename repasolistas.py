#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Zumpango

Unidad de Aprendizaje: Algoritmos genéticos

Author: Dr. Asdrúbal López Chau

Descripción:  Repaso (de nuevo) listas por comprensión

Created on Mon Mar  7 11:58:14 2022

@author: asdruballopezchau
"""

# Lista de numeros pares entre 1 y 10
pares = []
for i in range(1, 11):
    if i%2==0:
        pares.append(i)
        
pares2 = [n for n in range(1,11) if n%2==0]

# Lista de frutas

frutas = ["mango", "sandia", "melon", 
          "aguacate", "fresa", "durazno", 
          "melocoton"]
# Sublista de frutas sin "a"

fsa = [fruta for fruta in 
       frutas if "a" not in fruta]
# Sublista con frutas cuyo nombre sea
#menor o igual a cinco letras
fm5 = [fruta for fruta in frutas 
       if len(fruta)<=5]
fm5b =[]

for fruta in frutas:
    if len(fruta)<=5:
        fm5b.append(fruta)

    

