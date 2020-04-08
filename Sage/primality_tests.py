import time
import matplotlib
import matplotlib.pyplot as plt
import hashlib
from math import sqrt
from tools import*
from sage.all import*

##========================================================================================================================
## PARTIE 1 : Les tests de primalité : 
##========================================================================================================================




def TrialDivision(p):
    "Test les divisions successives de p"
    for i in LP:
        if p%i==0 and p!=i:
            return False
    return True




def MillerRabin(n):
    """ entrées : un entier impair n et un paramêtre de sécurité t supérieur ou égal à 1 """
    p=n-1
    s=0
    t=3
    while(p%2==0):
        s=s+1
        p=p//2
    r=(n-1)//2**s
    for i in range (0,t):
        a = randint(2,n-2)
        y = power_mod(a,r,n)
        if y!=1 and y!=n-1 :
            j=1
            while j<=s-1 and y!=n-1:
                y=power_mod(y,2,n)
                if y==1 :
                    return False
                j=j+1
            if y!=n-1:
                return False
    return True










