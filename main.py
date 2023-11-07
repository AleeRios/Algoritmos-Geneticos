# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:54:57 2022

@author: Redes
"""

from Laboratorio01 import Sistema as MySystem
from Laboratorio01 import MyHack

a=MySystem()
#print(a.login("Emanuel", "acaaa"))
hack = MyHack(a)
hack.fuerzaBruta()