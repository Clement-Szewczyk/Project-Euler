# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 12:09:44 2022

@author: Clément Szewczyk
"""

def Fib(n): 
    if (n<=1):
        return n 
    else:
        return (Fib(n-1) + Fib(n-2))

def nbdigit(x):
    nbd =0
    while x>1:
        x = x/10
        nbd = nbd+1
    return(nbd)
    
def euleur25(maxi):
    i=0
    while nbdigit(Fib(i))<maxi:
        i=i+1
    return i

print(euleur25(1000))