# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTONOMA DEL ESTADO DE MEXICO
CU UAEM ZUMPANGO

UNIDAD DE APRENDIZAJE:
    
DR ASDRUBAL LOPEZ CHAU
DESCRIPCION: SOLUCION AL LABORATYORIO DE DESCUBERE CONTRASENIA

Spyder Editor

This is a temporary script file.
"""

class Sistema:
    
    def __init__(self):
        self.password = "icoic"
    
    def hack(self, contrasenia):
        ctr = 0
        for letraP, letraC in zip(self.password, contrasenia):
            if letraP == letraC:
                ctr +=1
        
        #i = 0
        #for letra in contrasenia:
         #   if letra == self.passwor[i]:
          #      ctr +=1
           # i +=1
        return ctr
        pass
    def login(self, usuario, contrasenia):
        return self.hack(contrasenia)      

class MyHack:
    def __init__(self, sistema):
        self.target = sistema
        self.alfabeto="abcdefghijklmnopqrstuvwxyz"
        self.N = 5
        
    def fuerzaBruta(self):
        #n=self.N
        alfabeto = self.alfabeto
        target = self.target
        for i1 in alfabeto:
            for i2 in alfabeto:
                for i3 in alfabeto:
                    for i4 in alfabeto:
                        for i5 in alfabeto:
                            intento = i1 + i2 + i3 + i4 + i5
                            if target.login("",intento) == 5:
                                print("Hacked: ")
                                print("Password: "+ intento)
                                return
