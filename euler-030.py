# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:20:18 2022

@author: Clément Szewczyk
"""
s=0
vmax = 10
for a in range(vmax):
    for b in range(vmax):
        for c in range(vmax):
            for d in range(vmax):
                for e in range(vmax):
                    for f in range(vmax):
                        for g in range(vmax):
                            if (g**5+f**5+e**5+a**5+b**5+c**5+d**5 == g*1000000+f*100000+e*10000+a*1000+b*100+c*10+d):
                                s=s + g*1000000+f*100000+e*10000+a*1000+b*100+c*10+d
                                print ("%i%i%i%i%i%i%i" % (g,f,e,a,b,c,d))
                                
print(s)
        