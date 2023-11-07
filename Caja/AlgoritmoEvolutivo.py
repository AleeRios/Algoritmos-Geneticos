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
Descripción: lgoritmo genetico V 1.0
 
Created on Mon Mar  7 12:48:42 2022
 
@author: DELL
"""
import numpy as np
import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from Individuo import Individuo
from Poblacion import Poblacion
from FitnesFunction import FitnesFunction
from Seleccion import Seleccion

class AlgoritmoEvolutivo:
    def __init__(self, size,target,min,max,nb): #definimos nuestra funcion init
        self.size=size#self.size es igual a size
        self.pob= None#self.pob es igual a None
        self.target =target#self.target es igual a target
        self.max=max#self.max es igul a max
        self.min=min#self.min es igual a min
        self.nb=nb#self.nb es igual a nb
        
    def showPob(self, showAptitude= False): #definimos la funcion showPob
        if showAptitude:
            aptitudes= [self.ff.evaluate(ind) for ind in self.pob.poblacion]
        for i in range(self.size):#ciclo que vaya desde i hasta que llege al rango de size
            if showAptitude:
                print(self.pob.poblacion[i].__str__(), "->"+ str(aptitudes[i]))
            else:
                print(self.pob.poblacion[i])
            
        
    def inicializa(self): #definimos la funcion inicializa
        pob = Poblacion(self.size,self.min,self.max,self.nb)#pob es igual a poblacion con los parametros establecidos
        pob.inicializa()#inicializamos una poblacion
        self.pob = pob#self.pob es igual a pob
        self.seleccion = Seleccion() #self.seleccion es igual a seleccion
        self.ff=FitnesFunction(self.target) #self.ff es igual a FitnesFunction
    def evolucion(self):    #definimos la funcion evolucion
        #1) evaluar individuos
        #2) seleccionar padres para cruza
        #3) generar hijos (cruza)
        #4) mutar algunos
        #5) evaluar hijos
        #6) seleccionar mienmbros de la siguiente poblacion
        
        ###implementacion
        if self.pob is None:#si la poblacion es None entonces 
            print("Inicialize la poblacion")    #mandamos el mensaje "Inicialize la pobalcion"
            return
        #1.- Evaluar individuos
        poblacion = self.pob.poblacion #poblacion es igual a self.pob.poblacion
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion]
        #2.- Seleccionar padres para la cruza
        #en este caso cada padre puede tener 2 hijos
        k=int(self.size/2) #dividimos el tamaño entre 2
        if k%2 ==1: #si k modulo 2 es 1 entonces
            k+=1    #sumamos 1 a k para que sean 2
        idx= self.seleccion.selecciona(aptitudes,k)#idx es igual a self.seleccion.selecciona
        #3.-generar hijos (cruza)
        descendencia = []
        
        for i in range(0, k, 2):
            ip = papa=idx[i] #ip es igual a papa.idx[i]
            im = mama=idx[i+1]  #im es igual a mama idx[i+1]
            print(str(papa)+" con " + str(mama)) #imprimimos a nuestro papa y nuestra mama
            papa = poblacion[ip]    #papa es igual a poblacion[ip]
            mama = poblacion[im]    #mama es igual a poblacion[im]
            hijos = papa.cruza(mama)    #hijos es igual a papa.cruza(mama)
            descendencia.append(hijos[0])   #creamos la primer descendencia 
            descendencia.append(hijos[1])   #creamos la segunda descendencia
        #4.- Mutar algunos (5%)
        totalMutar = int(np.ceil(len(descendencia)*0.05)) #mutamos a alguna descendencia
        for i in range(totalMutar): #ciclo de i hasta el rango de totalMutar
            idx= random.choices(range(len(descendencia)))
            descendencia[idx[0]].mutar()    #mutamos a una de las descendencias
        
        #5.- evaluar a los hijos
        #6) seleccionar mienmbros de la siguiente poblacion
        
        #junto padres e hijos
        for hijo in descendencia:   
            poblacion.append(hijo)
        #calculo aptitudes de todos
        aptitudes = [self.ff.evaluate(ind) for ind in poblacion]#calculamos aptitudes
        
        #elitismo!!!
        idxMejor = np.argmax(aptitudes) #obtenemos al mejor de la poblacion
        #el mejor pasa directamente a la siguiente poblacion
        siguientePob = []
        siguientePob.append(poblacion[idxMejor])
        
        #selecciono inices de individuos para la siguiente generacion
        idx= self.seleccion.selecciona(aptitudes,self.size)
        #creo la lista de individuos de la siguiente generacion
        siguientePob = []
        for i in idx:
            siguientePob.append(poblacion[i])
        #guardo para la siguiente evolucion
        self.pob.poblacion=siguientePob
            
    def graficar(self, mostrar=False):
        if mostrar:
            mejores = [self.ff.evaluate(ind) for ind in self.pob.poblacion] #obtenemos a los 5 mejores
            mejores = list(set(mejores))#los guardamos en una lista
            mej = []    
            for i in range(5):
                idx = mejores.index(max(mejores)) #buscmos a los 5 mejores
                mej.append(self.pob.poblacion[idx].cromosoma.getValues()) #obtenemos a los 5 mejores
                self.pob.poblacion.pop(idx) #los eliminamos  de la poblacion
                mejores.pop(idx)
            
            #print(mej)
            print("\n\n")
            for i in range(len(mej)):
                v = mej[i]
                volumen = v[0] * v[1] * v[2] #sacamos el volumen
                print("El volumen " + str(i+1) + " es: ", volumen, end="\n\n")#imprimimos el volumen
                
            for i in range(len(mej)):
                fig = plt.figure()
                ax = plt.axes(projection="3d")
                plt.title("Volumen "+str(i+1))#titulo de la grafica
                plt.xlabel("X") #imprimimos  x
                plt.ylabel("Y") #imprimimos y
                plt.xlim(2)
                plt.ylim(2)
                val = mej[i]
                x = val[0]#valores x
                y = val[1]#valores y
                z = val[2]#valores z
                ax.plot3D(x, y, z)
                plt.show()#mostramos la grafica
        else:
            return