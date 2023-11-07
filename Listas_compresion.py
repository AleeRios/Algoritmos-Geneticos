"""
Created on Mon Mar  7 11:58:28 2022

UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: ALGORITMOS GENÉTICOS
Tema: Listas por comprenseion
Alumno: Rios Campusano Beckham Alejandro
Profesor: Dr. Asdrubal López Chau
Descripción: Repaso (de nuevo) listas por comprensión
    
@author: alebe
"""

pares = []
for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)
        
pares2 = [n for n in range(1, 11) if n % 2 == 0]

frutas = ["mango", "sandia", "melon", "aguacate", "fresa", "durazno", "melocoton"]

fsa = [fruta for fruta in frutas if "a" not in fruta]

f = [i for i in frutas if len(i) <= 5]