# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:20:25 2022

@author: Clément Szewczyk
"""



def nbpremier(x):
    for i in range(2, (x-1)) :
       if x%i==0: 
           return False
    return True
       
def compteurnb():
    cptnp =0
    z=0
    while cptnp <= 10001:
         z= z+1 
         if nbpremier(z)== True:
             cptnp = cptnp + 1
             
         
    print(z)
            

compteurnb()
             
                 




        

