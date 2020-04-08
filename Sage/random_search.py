import time
import matplotlib
import matplotlib.pyplot as plt
import hashlib
from testNIST import*
from primality_tests import*




def naiveGen(n=1000,test=is_pseudoprime):
    q=Integer(randint(0,2**n))
    while (q % 2 != 1):
        q=Integer(randint(0,2**n))
    while not test(q):
        q=q+2
    return q




def random_search(k=1000,test=is_pseudoprime):
    " Algo random_search récursif "
    a = Integer(randint(0,2**k))
    if not TrialDivision(a) :
        return random_search(k)
    else :
        if not test(a):
            return random_search(k)
        else:
            return a

def RS(k=1000,test=is_pseudoprime):
    " Algo random_search avec boucle while =/= récursif "
    b = False
    while not b:
        a=Integer(randint(0,2**k))
        if TrialDivision(a):
            if test(a):
                b=True
    return a






    
