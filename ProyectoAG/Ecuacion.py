#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 20:05:05 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Ecuacion
Alumno: Rios Campusano Beckham Alejandro
        Garduño Sanchez Bladimir Axley
        Vazquez Bravo Emmanuel
Profesor: Dr. Asdrubal López Chau
Descripción: Proyecto
    
@author: alebe
"""

import random as rd  #importamos ramdom 

class Ecuacion:  #definimos la clase Ecuacion
    
    def __init__(self):  #definimos la funcion __init__
        self.numCo = None  #self.numCo es igual a None
        self.var = "xyzabcdefg"  #self.var es igual a una cadena
        self.ecu = None  #self.ecu es igual a None
        self.coefi = None  #self.coefi es igual a None
        self.res = None #self.res es igual a None
        
    def pedirDatos(self): #definimos la funcion pedirDatos
    	n = int(input("\nIngresa la cantidad de coeficientes (<=10): ")) #pedimos la cantidad de coeficientes
    	coefi = [] #coefi es igual a un arreglo
    	self.numCo = n #self.numCo es igual a n
    	for i in range(self.numCo): #ciclo que va desde 0 hasta lo que valga numCo
    		d = int(input("Ingresa el coeficiente " + str(i+1) + ": ")) #d es igual al coeficiente que ingrese el usuario
    		coefi.append(d)  #ingresamos el d a coefi
    	self.coefi = coefi     #self.coefi es igual a coefi
    	self.res = int(input("Resultado: "))  #self.res es igual a el resultado que nos ingrese el usurio 
    
    def generar(self):  #declaramos la funcion generar 
        #coefi = [] 
        ecu = ""  #ecu es igual a una cadena vacia
        #for i in range(self.numCo):
           # c = rd.randint(-10, 10)
           # coefi.append(c)
        #self.coefi = coefi
        
        for i in range(len(self.coefi)):  #ciclo que valla desde 0 hasta que sea la longitud de coefi 
            if self.coefi[i] >= 0:  #si coefi es mayor a 0 entonces
                ecu += "+" + str(self.coefi[i])  #ecu suma lo que haya en coefi[i]
                ecu += self.var[i]  #ecu suma lo que haya en var[i]
            else:  #ene otro caso 
                ecu += str(self.coefi[i]) + self.var[i]  #ecu suma lo que valga coefi[i] mas var[i]
        
        if(ecu[0] == "+"): # si ecu[0] es igual a + entonces
            ecu = ecu.replace("+", "", 1)  #ecu remplazara por 1
        
        #self.res = rd.randint(-100, 100)
        ecu += "=" + str(self.res)  #ecu sumara lo que valga res
        self.ecu = ecu #self.ecu es igual a ecu
        
        self.max = []  #self.max es igual a una lista
        self.min = []  #self.min es igual a una lista
        self.bits = [] #self.bits es igual a una lista
        
        for i in range(self.numCo):  #ciclo que valla desde 0 hasta lo que valga numCo
            if self.res > 0:    #si res es mayor a 0 entonces
                self.max.append(self.res)  #self.max ingresara res
                self.min.append(-1* self.res) #self.min ingresara -1*res
            else:    #en otro caso 
                self.min.append(self.res)  #self.min ingresaara res
                self.max.append(-1* self.res) #self.max ingresara -1*res
            self.bits.append(8)  #self.bits ingresara 8
        
        return self.coefi, self.res, self.ecu  #regresaremos coefi,res y ecu
    
    
    
    
    
        