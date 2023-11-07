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
Descripción: clase individuo
 
Created on Mon Feb 28 18:30:00 2022
 
@author: DELL
"""
import random
import numpy as np
#from GenReal import GenReal
from CromosomaReal import CromosomaReal 
class Individuo:
    
    def __init__(self,min,max,nb):
        self.min= min
        self.max=max
        self.nb=nb
        self.cromosoma=CromosomaReal(self.min, self.max, self.nb)
    
    def init(self):
        self.cromosoma.init()
        
    def cruza(self, madre):
        papa=CromosomaReal(self.min, self.max,self.nb)
        papa.init()
        mama=CromosomaReal(self.min, self.max,self.nb)
        mama.init()
        hijos = papa.cruzar(mama)
        h1=Individuo(self.min, self.max, self.nb)
        h1.cromosoma=hijos[0]
        h2=Individuo(self.min, self.max, self.nb)
        h2.cromosoma=hijos[1]
        return [h1, h2]
    
    def __str__(self):
        return self.cromosoma
    
    
    def mutar(self):
        self.cromosoma.mutar()
        
#1) reprecentacion de la solucion: la cromosoma sera una cadena de 5 caracteres.
#cada gen es un caracter
#2) funcion de la evaluacion o aptitud: Es el numero de letras en posicion correcta
#3) seleccion de progenitores: Mayor aptitud mas probabilidad de ser elegido
#4) Operadores geneticos
#   a)cruza:cruza por un punto
#   b)mutuacion: cambiar un gen (letra) mediante un proceso estocastico







