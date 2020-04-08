import time
import matplotlib
import matplotlib.pyplot as plt
import hashlib

##========================================================================================================================
## PARTIE 1 : Les tests de primalité : 
##========================================================================================================================


#constante B pour le nombre de divisions successives nécessaires pour l'algo random_search
B = 2**20



def H(s):
    s=str(s)
    sha2 = hashlib.sha256
    a=sha2(s.encode('utf-8'))
    return ZZ(a.hexdigest(),16)
    
def List_premiers(n):
    i=0
    l=[]
    while i <= sqrt(n):
        i = next_prime(i)
        l.append(i)
    return l

# Liste des nombres premiers < 2**20.
LP=List_premiers(B)


def LongDivision(n,m):
    i=1
    while i*m <= n:
        i=i+1
    return (i-1,n-(i-1)*m)



def TrialDivision(p):
    "Test les divisions successives de p"
    for i in LP:
        if p%i==0 and p!=i:
            return False
    return True




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


##========================================================================================================================
## PARTIE 2 : Les algorithmes de génération aléatoire de grands nombres premiers.
##========================================================================================================================


def naiveGen(n):
    q=Integer(randint(0,2**n))
    while (q % 2 != 1):
        q=Integer(randint(0,2**n))
    while not q.is_pseudoprime():
        q=q+2
    return q

def random_search(k):
    " Algo random_search récursif "
    a = Integer(randint(0,2**k))
    if not TrialDivision(a) :
        return random_search(k)
    else :
        if not a.is_pseudoprime():
            return random_search(k)
        else:
            return a

def RS(k):
    " Algo random_search avec boucle while =/= récursif "
    b = False
    while not b:
        a=Integer(randint(0,2**k))
        if TrialDivision(a):
            if a.is_pseudoprime():
                b=True
    return a

def RS2(k):
    " Algo random_search avec boucle while =/= récursif sans Divisions successives"
    b = False
    while not b:
        a=Integer(randint(0,2**k))
        if a.is_pseudoprime():
            b=True
    return a

def RS3(k):
    " RS avec notre test de miller-rabin"
    b = False
    while not b:
        a=Integer(randint(0,2**k))
        if TrialDivision(a):
            if MillerRabin(a,3):
                b=True
    return a


def gordon(k=0):
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




    
    
    
    
def nist(l):
    q=Integer(8)
    L=512+64*l
    n,b = LongDivision(L-1,160)
    my_bool = False
    while not my_bool :
        while not q.is_pseudoprime():
            
            s = Integer(randint(0,2**200))
            U = H(s) ^ H((s+1) % 2**200)
            ql = U.digits(2)
            ql[0]=1
            ql[-1]=1
            q=Integer(bin_to_dec(ql))
        i=0
        j=2
        
        while i < 4096 :
            V = []
            
            for k in range (0,n):
                V.append(H((s+j+k) % 2**200))
            W = V[0]
            for ii in range (0,n):
                W += V[ii]*(2**(160*(ii)))
            
            W += (V[-1] % 2**b)*(2**(160*n))
            X = W + 2**(L-1)
            c = X % (2*q)
            p = X - (c-1)
            
            if p>=(2**(L-1)):
                if p.is_pseudoprime():
                    return (q,p)
            i += 1
            j += 1

def maurer(k):
    b1 = True
    b2 = True
    r=0
    if k <= 20 :
        while b1:
            n = Integer(randint(0,2**k))
            if TrialDivision(n):
                b1 = False
    else :
        while b2:
            c=0.1
            m=20
            B=c*(k**2)
            
            if k>(2*m):
                while True:
                    s=random()
                    r=2**(s-1)
                    if (k-r*k)>m:
                        break
            else :
                r=0.5
            rk=floor(r*k)+1

            q = maurer(rk)
            I = floor(2**(k-1) / (2*q))
            succes = 0
            while (succes==0):
                R = randint(I+1, 2*I)
                
                n=2*R*q+1
                if TrialDivision(n):
                    a = randint(2,n-1)
                    b = power_mod(a,n-1,n)
                    if b==1 :
                        b = power_mod(a,2*R,n)
                        d=gcd(b-1,n)
                        if d==1:
                            succes = 1
                            b2=False
                            
    return n



##def RS2(k):
##    b = False
##    while not b:
##        a=Integer(randint(0,2**k))
##        if a.is_pseudoprime():
##            b=True
##    return a


##========================================================================================================================
## PARTIE 3 : Tests expérimentaux.
##========================================================================================================================



def test_if_really_Prime(gen,k):
    b = True
    for i in range (0,10000):
        a=gen(k)
        b = a.is_pseudoprime()
    return b
        


def TestGen(n,k,gen):
    " Test n fois la génération de nombres premiers pouvant être codés sur k-bits, renvoie un couple : temps moyen d'exécution , bugs "
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

    if bug==0:
           return (tps/n)
        



##def TestGen1(n,k,gen):
##    " Test n fois la génération de nombres premiers pouvant être codés sur k-bits "
##    l = []
##    tps=0
##    bug = 0
##    for i in range (0,n):
##        start = time.time()
##        try :
##            prime = gen(k)
##        except :
##            bug +=1
##        end = time.time()
##        tps += (end-start)
##
##    return ("la generation de {} nombre(s) premier(s) a pris en moyenne {} secondes, il y a eu {} bugs").format(n-bug,tps/n,bug)







a=2




def bin_to_dec(L):
    ret = 0
    for i in range (0,len(L)):
        if L[i] == 1 :
            ret+= 2**i
    return ret

def gen_courbes(gen) :
    x= []
    y=[]
    for i in range(18,28):
        global LP
        LP = List_premiers(2**i)
        y.append(TestGen(100,1000,gen))
        x.append(2**i)

    return (x,y)
	
	
