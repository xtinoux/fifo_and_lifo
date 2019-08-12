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
N = [3,5,7,15]
# Somme à obtenir :
S = [15,42,87,154]

print("***************************************")
print("          BATTERIE DE TESTS ")
print("-----------------------------------\n")
# on appelle la fonction du competiteur
for n in N:
    for s in S:
        M = carre_magique(n,s)
        # puis on la teste avec notre fonction
        if isinstance(M, list):
            # si M est une liste
            print(F"Carre : {n}x{n} - somme = {s} :")
            print(F"{test_complet(M,n,s)}\n")
#        else:
#            # sinon on affiche ce que renvoie la fonction du competiteur
#            print(M)
print("-------------------------------------")
print("                FIN DES TESTS ")
print("***************************************")