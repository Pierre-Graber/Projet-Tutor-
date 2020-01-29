	
# -*- coding: utf8 -*-
import time

def MillerRabin(n,t):
    """ entrées : un entier impair n et un paramêtre de sécurité t supérieur ou égal à 1 """
    p=n-1
    s=0
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

def naiveGen(n):
    q=Integer(randint(0,2**n))
    while (xgcd(q,2)[0]!=1):
        q=Integer(randint(0,2**n))
    while not q.is_pseudoprime():
        q=q+2
    return q

def random_search(k):
    a = Integer(randint(0,2**k))
    if a.trial_division(2**(sqrt(k/10)))!= a:
        return random_search(k)
    else :
        if not a.is_pseudoprime():
            return random_search(k)
        else:
            return a


def TestGen1(n,k,gen):
    " Test n fois la génération de nombres premiers pouvant être codés sur k-bits "
    l = []
    tps=0
    bug = 0
    for i in range (0,n):
        start = time.time()
        try :
            prime = gen(k)
        except :
            bug +=1
        end = time.time()
        tps += (end-start)

    return ("la generation de {} nombre(s) premier(s) a pris en moyenne {} secondes, il y a eu {} bugs").format(n-bug,tps/n,bug)



def List_premiers(n):
    i=0
    l=[]
    while i <= sqrt(n):
        i = next_prime(i)
        l.append(i)
    return l

LP=List_premiers(2**(32))

def TrialDivision(p,B):
    for i in LP:
        if p%i==0:
            return False

def gordon(k):
    s=random_search(300)
    t=random_search(300)
    iz = randint(0,2**200)
    i=iz
    while not (2*i*t+1).is_pseudoprime():
        i+=1
    r=2*i*t+1

    pz = 2*power_mod(s,r-2,r)*s -1
    jz = randint(0,2**200)

    while not (pz+2*jz*r*s).is_pseudoprime():
        pz=pz+1
    p=pz+2*jz*r*s
    return p
