from primality_tests import*
from sage.all import*
from random_search import*
from pollard import*

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

    while not test(pz+2*jz*r*s):
        pz=pz+1
    p=pz+2*jz*r*s
    return p


def gT(n,test=is_pseudoprime):
    s=random_search(n//3)
    t=random_search(n//3)
    iz = randint(0,2**(n//5))
    i=iz
    while not test(2*i*t+1):
        i+=1
    r=2*i*t+1

    pz = 2*power_mod(s,r-2,r)*s -1
    jz = randint(0,2**(n//5))

    while not test(pz+2*jz*r*s):
        pz=pz+1
    p=pz+2*jz*r*s
    return p

def ttt():
    r=RS(300)
    return r

def testComparaisonGordon(RS,G):
    return (pollard(Integer(RS[0]),130000),pollard(Integer(G[0]),130000))
    

def RS_GG(k):
    p,q = (RS(k),RS(k+6))
    pp,qq = (gT(k),gT(k+6))
    
    return (p*q,p,q),(pp*qq,pp,qq)






        
    
