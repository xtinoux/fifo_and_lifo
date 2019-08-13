# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce module contient differentes fonctions. Il permet de determiner si un carre est magique
Il est appele par test_carre.py
"""
def test_forme(M,N):
    ''' 
    Teste si le carre propose est bien un carre NxN
    '''
    val = 0
    n = len(M)
    for i in range(n-1):
        for j in range(i+1,n):
            if len(M[i]) == len(M[j]):
                val += 1
    if val == N*(N-1)//2:
        return 1
    else:
        return 0
    
    
def test_nbre(M):
    '''
    Teste si tous les nombres sont differents et non  nuls et entiers positifs
    '''
    N = len(M)
    for i in range(N):
        for j in range(N):
            if M[i][j] == 0:
                return 0
            if not isinstance(M[i][j], int):
                return 3
            if M[i][j] < 0:
                return 4
            for k in range(i,N):
                for l in range((j+1)*(k==i),N):
                    if M[i][j] == M[k][l]:
                        return 2
    return 1


    
def test_diago(M):
    '''
    Si la somme de chaque diagonale est identique, on la retourne, sinon, on renvoie 0
    '''
    N = len(M)
    s = 0
    for i in range(N):
        s = s + M[i][i]
    S = 0
    for i in range(N):
        S = S + M[N-i-1][i]
    if s == S:
        return s
    return 0


def test_lig(M):
    '''
    Si la somme de chaque ligne est identique, on la retourne, sinon, on renvoie 0
    '''
    N = len(M)
    s = []
    lig = 1
    for i in range(N):
        s.append(0)
        for j in range(N):
            s[i] = s[i] + M[i][j]
    for i in range(N):
        for j in range(i+1,N):
            if s[i] != s[j]:
                lig = 0
            if lig == 1:
                return s[0]
    return 0

def test_col(M):
    '''
    Si la somme de chaque colonne est identique, on la retourne, sinon, on renvoie 0
    '''
    N = len(M)
    s = []
    col = 1
    for j in range(N):
        s.append(0)
        for i in range(N):
            s[j] = s[j] + M[i][j]
    for j in range(N):
        for i in range(N):
            if s[j] != s[i+1]:
                col = 0
            if col == 1:
                return s[0]
    return col

def test_carre(M,N,S,pos,neg):
    if test_forme(M,N) == 0:
        return neg + F"Ce n'est pas un carre {N} x {N} !"
    else:
        val = test_nbre(M)
        if val == 2:
            return neg + "Il y a des nombres identiques dans le carre !"
        elif val == 0:
            return neg + "Il y a au moins un nombre nul dans le carre !"
        elif val == 3:
            return neg + "Le carre ne contient pas que des entiers !"
        elif val == 4:
            return neg + "Le carre ne contient pas que des entiers positifs !"
        else:
            s1 = test_diago(M)
            s2 = test_lig(M)
            s3 = test_col(M)
            if s1 == s2 == s3 == S:
                return pos + F"Le carre retourné est magique de somme {S}."
            elif s1 == s2 == s3 != S:
                return neg + F"Ce carre est magique, mais de somme {s1}, et non {S}."
    return neg + F"Ce carre n'est pas magique ! (lignes, colonnes, diagonales : {s1},{s2},{s3})"

def test_complet(M,N,S):
    '''
    On teste si c'est un carre, sans 0 et sans nombre identique, avec des entiers positifs ...
    Puis, on teste sur les diagonales, les lignes et les colonnes si la somme est identique, egale
    à ce qui est prevu.
    '''
    val = 0
    neg = " Erreur(s) detectee(s) --> "
    pos = "***** SUCCES *****"
    if isinstance(M, list) == False:
        return neg + "La fonction ne renvoie pas une liste !"
    else:
        if len(M) != 2:
            return neg + "La fonction ne renvoie pas une liste conforme !"
    if M[0] == 0:
        if N%2 == 0:
            return pos + "La fonction détecte bien que N est pair"
        else:
            return neg + "La fonction ne détecte pas que N est pair"
    if M[0] == 1:
        if S < N*(N**2+1)//2:
            return pos + "La fonction détecte bien que la somme demandée est trop faible"
        else:
            return neg + "La fonction ne détecte pas que la somme demandée est trop faible"
    if M[0] == 2:
        return "Ce cas n'est pas encore traité"
    if M[0] == 3:
        res = test_carre(M[1],N,S,pos,neg)
        return res


if __name__ == '__main__':
    print(test_carre([[2,13,9,14],[16,7,11,4],[15,8,12,3],[5,10,6,17]],4,38,"ok ! ","non ! "))
    


