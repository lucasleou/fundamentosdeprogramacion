#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 08:41:32 2021

@author: lucasvillegas
"""

def combinatoria(m,n):
    comb = factorial(m) / (factorial(n) * factorial(m-n))
    return comb
def factorial(n):
    factor = 1
    for x in range(n):
        factor = factor * (n-x)
    return factor
n1 = int(input('Digite m: '))
n2 = int(input('Digite n: '))
print(combinatoria(n1,n2))  