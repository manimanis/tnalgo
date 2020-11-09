from random import randint


def arrondi(x):
    if type(x) == float:
        return int(round(x, 0))
    elif type(x) == int:
        return x
    else:
        raise TypeError(type(x), " n'est pas supporté")
        

def racine_carre(x):
    return x ** 0.5


def alea(vi, vf):
    return randint(vi, vf)


def ent(x):
    if type(x) == float:
        return int(x)
    elif type(x) == int:
        return x
    else:
        raise TypeError(type(x), " n'est pas supporté")
        
    
def long(ch):
    return len(ch)


def pos(ch1, ch2):
    return ch2.find(ch1)


def convch(x):
    if type(x) == float or type(x) == int:
        return str(x)
    else:
        raise TypeError(type(x), " n'est pas supporté")
        
        
def valeur(ch):
    try:
        x = int(ch)
        return x
    except Exception:
        pass
    try:
        x = float(ch)
        return x
    except Exception:
        pass
    raise ValueError("Ne peut pas être convertie")
    

def sous_chaine(ch, d, f):
    return ch[d:f]


def effacer(ch, d, f):
    if f >= d:
        return ch[:d] + ch[f:]
    raise ValueError(f"{d} < {f} impossible d'effacer")
    

def majus(ch):
    return ch.upper() 
    
# -*- coding: utf-8 -*-

