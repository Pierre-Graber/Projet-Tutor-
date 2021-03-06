# coding: utf-8
from sage.all import*
import time
import matplotlib
import matplotlib.pyplot as plt
import hashlib
from random_search import RS

def GenerationAverageTime(n,k,gen,test=is_pseudoprime):
    " Test n fois la génération de nombres premiers pouvant être codés sur k-bits, renvoie un couple : temps moyen d'exécution , bugs "
    l = []
    tps=0
    bug = 0
    for i in range (0,n):
        start = time.time()
        try :
            prime = gen(k,test)
        except :
            bug +=1
        end = time.time()
        tps += (end-start)

    return (tps/n,bug)



def TestRS(n,k,B):
    l = []
    tps=0
    bug = 0
    for i in range (0,n):
        start = time.time()
        try :
            prime = RS(k,is_pseudoprime,B)
            
        except :
            bug +=1

        end = time.time()
        tps += (end-start)

    return (tps/n,bug)
    


def gen_courbesRS() :
    x= []
    y=[]
    for i in range(6,20):
        y.append(TestRS(2000,1000,2**i)[0])
        x.append(i)

    return x,y



def distribution(n,k,gen):
     intervalle = [0, 100000]
     mD = {}
     for i in range (0,n):
         p = gen(k)
         if intervalle[0] < p < intervalle[1]:
             if p in mD :
                 mD[p]+=1
             else :
                 mD[p]=1
     return mD












         
