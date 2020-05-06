import math
from tools import *
import time
from gordon import*

def pollard(n,B):
    a=Integer(randint(2,n-1))
    d=gcd(a,n)
    if d>=2:
        return d
    for q in premiers(B):
        l=floor(ln(n)/ln(q))
        a=power_mod(a,q**l,n)
    d=gcd(a-1,n)
    if d==1 or d==n:
        return False
    else:
        return d


def pl(N,B):
    a=2
    for p in premiers(B):
        pp=1
        while pp*p <= B :
            pp*=p
        a=power_mod(a,pp,N)
        g=gcd(a-1,n)
        if 1 < g < N:
            return g
    return False

def P_1(N,B):
    a=2
    j=2
    while j <= B:
        a=power_mod(a,j,N)
        d=gcd(a-1,N)
        if d>1 and d<N:
            return d
        j=j+1
    return False

def factorRunningTime(N,fact):
    start=time.time()
    n=fact(Integer(N))
    end=time.time()
    return n,end-start

def t(N,f):
    return f(N)

def Compare(k):
    a=0
    b=0
    for i in range (0,k):
        A,B = RS_GG(100)
        while (len(str(A[0])) != len(str(B[0]))):
            A,B = RS_GG(100)
        a+= factorRunningTime(A[0])[1]
        b+= factorRunningTime(B[0])[1]
        print(a,b)
    return(a/k,b/k)


    
    
def factor_AverageTime(gen,k,n,fact_Alg):
    res = 0
    for i in range (0,n):
        pq = gen(k)*gen(k)
        res+= factorRunningTime(pq,fact_Alg)[1]
    return res/n


def factor_CompareCourbes(gen1,gen2,k,n,fact_Alg):
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    for i in range (k,k+n):
        x1.append(factor_AverageTime(gen1,i,20,fact_Alg))
        x2.append(factor_AverageTime(gen2,i,20,fact_Alg))
        y1.append(i)
        y2.append(i)
    return (x1,y1),(x2,y2)
        

    
              
 
def fact(N,B):
    e=factorial(B)
    a=Integer(randint(0,N))
    x=gcd(a,N)
    if x != 1 :
        return x
    b = power_mod(a,e,N)
    x = gcd (b-1,N)
    if x == N :
        return ("Borne trop grande")
    elif x ==1 :
        return ("Brne trop petite")
    else:
        return x




