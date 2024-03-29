#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:48:36 2019

@author: eric

Ce script permet de tester la fonction utilisateur afin de la valider
Il utilise test_enigme6.py

"carre_magique" est la fonction du competiteur pour les tests
"""

from test_enigme6 import test_complet
from carre_magique import carre_magique

# ordre du carre :
N = [3,11,4,7,3,4]
# Somme à obtenir :
S = [15,55,34,168,16,35]

print("***************************************")
print("          BATTERIE DE TESTS ")
print("***************************************")
# on appelle la fonction du competiteur
T = list(zip(N,S))
for x in T:
    print("\n")
    print(F"TEST : Carre {x[0]}x{x[0]} - somme = {x[1]}")
    print("-----------------------------")
    M = carre_magique(x[0],x[1])
    print(test_complet(M,x[0],x[1]))

print("\n")
print("***************************************")
print("                FIN DES TESTS ")
print("***************************************")