#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM Texcoco

Unidad de Aprendizaje: 

Author: Dr. Asdrúbal López Chau

Descripción:  

Created on Mon Mar  7 12:21:15 2022

@author: asdruballopezchau
"""

import random

import numpy as np

artistas = ["shakira", "Harry Styles", "Cristiano Ronaldo", 
            "Cristina Aguilera", "Dua Lipa", "Don Ramon"]

aptitudes = [9.5, 10., 10., 9, 9.8, 6]
aptitudes = np.array(aptitudes) + 0.2
probabilidades = [np.exp(aptitud)/np.sum(np.exp(aptitudes))
                  for aptitud 
                  in aptitudes]

elegidos = random.choices(artistas, probabilidades, k= 2)
print(elegidos)







