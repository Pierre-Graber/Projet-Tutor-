from primality_tests import*
from sage.all import*
from random_search import*

def gordon(test=is_pseudoprime):
    s=random_search(300)
    t=random_search(300)
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
