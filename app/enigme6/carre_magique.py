#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:48:36 2019

@author: eric

ici, une speudo fonction qui devrait etre celle du competiteur
"""

def carre_magique(N,S):
    if N > 10:
        return [0, "Merci de donner un nombre inférieur à 11"]
    if S < N * (N**2 + 1) // 2:
        return [1, N*(N**2+1)//2]
    elif S >= N * (N**2 + 1) // 2 and N > 3:
        return [2, []]
    return [3,[[6,1,8],[7,5,3],[2,9,4]]]