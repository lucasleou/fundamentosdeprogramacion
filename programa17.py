#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:33:44 2021

@author: lucasvillegas
"""

import numpy as np
def ingresar_sueldos():
    sueldos = []
    for x in range(5):
        sueldo = int(input('Ingrese el sueldo: '))
        sueldos.append(sueldo)
    return sueldos
def sueldos_prom(sueldos):
    cont = 0
    for x in range(len(sueldos)):
        print(sueldos[x])
        if sueldos[x] >= 4000:
            cont += 1
    print(f'Hay {cont} sueldos sobre 4000')
def bajo_prom(sueldos):
    prom = np.mean(sueldos)
    cont = 0
    for x in range(len(sueldos)):
        if sueldos[x] <= prom:
            cont += 1
    print(f'Hay {cont} saldos bajo el promedio')    
sueldos = ingresar_sueldos()
sueldos_prom(sueldos)
bajo_prom(sueldos)