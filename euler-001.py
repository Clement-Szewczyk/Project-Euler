# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:39:34 2022

@author: Clément Szewczyk
"""

def estmult35(x):
    if x%3 == 0:
        return True
    if x%5 == 0:
        return True
    return False

def euler001(x):
    somme=0
    for i in range(0,x):
        if estmult35(i):
            somme=somme+i
    return somme

print(euler001(1000))