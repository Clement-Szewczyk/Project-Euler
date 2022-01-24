# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:53:52 2022

@author: Clément Szewczyk
"""

def Fibonacci(n): 
    if (n<=1):
        return n 
    else:
        return (Fibonacci(n-1) + Fibonacci(n-2))


n = int(input("nombre de terme :"))
somme = 0
print("Suite de Fibonacci de", n, " termes :")

for i in range (n):
    if Fibonacci(i)<4000000:
        if Fibonacci(i)%2 == 0:
            somme = somme + Fibonacci(i)


print(somme -1)
print(somme)
        