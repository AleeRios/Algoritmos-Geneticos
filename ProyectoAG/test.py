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

from Ecuacion import Ecuacion as ec   #importamos Ecuacion
from AlgoritmoEvolutivo import AE as ae  #importamos AlgoritmoEvolutivo
import numpy as np  #importamos numpy

def resultado(n, coefi, m):  #definimos la funcion resultado
    s = ""   #s es igual a una cadena vacia

    for i in range(n):  #ciclo que va desde i hasta el valor que tenga n
        if coefi[i] >= 0:  #si coefi[i] es mayor a 0 entonces
            s += "+" + str(coefi[i]) + "(" + str(m[i]) + ")"  #s sumara coefi mas m[i]
        else:  #en otro caso 
            s += str(coefi[i]) + "(" + str(m[i]) + ")"  #s sumara coefi[i] masa m[i]

    if(s[0] == "+"):  #si s[0] es igual a +
        s = s.replace("+", "", 1)  

    s += "=" + str(np.dot(coefi, m))  #s sumara el producto punto de coefi y m
    return s   #regresaremos s
    

#n = int(input("\nIngresa la cantidad de coeficientes (<=10): "))
ec = ec()   #ec es igual a ec
ec.pedirDatos()  #ec pedira datos 
coefi, res, ecu = ec.generar()  #coefi, res, ecu generaran datos
maxx = ec.max   #maxx es igual aa ec.max
minn = ec.min   #minn es igual a ec.min
bits = ec.bits  #bits es igual a ec.bits

print("\n\t\tLa ecuacion es: ", ecu)  #imporimiremos cual es nuestra ecuacion 

alEv = ae(res, coefi, maxx, minn, bits, 100)  

for i in range(100):   #ciclo que valla desde 0 hasta 100
    alEv.evolucion()  #hacemos una evolucion 
    
print("\n-----------------")  #imprimimos una linea 
print("\n\t\tUltima Poblacion: ", end="\n\n")  #imprimimos nuestra ultima poblacion 
alEv.showPob(True) #mostramos nuestra ultima poblacion

m = alEv.mejorSolucion()  #m es igual a la mejor solucion encontrada

print("\n\n\t\tLa mejor solucion es: ", m)  #imprimimos nuestra mejor solucion encontrada


print("\n\n\t\tLa solucion es: ", resultado(ec.numCo, coefi, m))    #imprimimos cual es nuestra solucion 








