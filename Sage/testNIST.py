import time
import matplotlib
import matplotlib.pyplot as plt
import hashlib
from primality_tests import*
from NIST_DSA import*
from sage.all import*



def TestNist(l,k):
    "Test la primalité de q et p et vérifie que q | (p-1) "
    depart = 0
    fin = 0
    depart = time.time()
    for i in range (0,k):
        q,p = nist(l)
        if (q.is_pseudoprime == False) or (p.is_pseudoprime==False) or ( (p-1) % q != 0 ) :
            return False
        
    fin = time.time()
    return (True,(fin-depart)/k)



    


def testAlea():
    depart = time.time()
    for i in range (0,100000):
        r=randint(0,2**1024)
    fin = time.time()
    return ((fin-depart)/100000)
