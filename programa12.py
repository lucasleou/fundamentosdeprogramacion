#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:02:15 2021

@author: lucasvillegas
"""

def mascaracteres(i):
    maxcaracteres = ''
    for x in range(len(i)):
        if len(i[x]) > len(maxcaracteres):
            maxcaracteres = i[x]
    return maxcaracteres
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))