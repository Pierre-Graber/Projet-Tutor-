from primality_tests import*
from sage.all import*
from random_search import*
from factor_tools import*

def gordon(test=is_pseudoprime):
    s=RS(300)
    t=RS(300)
    iz = randint(0,2**200)
    i=iz
    while not test(2*i*t+1):
        i+=1
    r=2*i*t+1

    pz = 2*power_mod(s,r-2,r)*s -1
    jz = randint(0,2**200)
    j = jz
    while not test(pz+2*j*r*s):
        j=j+1
    p=pz+2*j*r*s
    return p


def gT(n,test=is_pseudoprime):
    s=RS(n//3)
    t=RS(n//3)
    iz = randint(0,2**(n//5))
    i=iz
    while not test(2*i*t+1):
        i+=1
    r=2*i*t+1

    pz = 2*power_mod(s,r-2,r)*s -1
    jz = randint(0,2**(n//5))
    j=jz
    while not test(pz+2*j*r*s):
        j=j+1
    p=pz+2*j*r*s
    return p


def testComparaisonGordon(RS,G):
    return (pollard(Integer(RS[0]),130000),pollard(Integer(G[0]),130000))
    







        
    
