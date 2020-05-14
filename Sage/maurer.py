# coding: utf-8
from primality_tests import*
from tools import*

def maurer(k,test=TrialDivision):
    b1 = True
    b2 = True
    if k <= 20 :
        while b1:
            n = Integer(randint(0,2**k))
            if test(n):
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
                if test(n):
                    a = randint(2,n-1)
                    b = power_mod(a,n-1,n)
                    if b==1 :
                        b = power_mod(a,2*R,n)
                        d=gcd(b-1,n)
                        if d==1:
                            succes = 1
                            b2=False
                            
    return n

#======================================================================================================================

def TestMaurer(n,k,test):
    " Test n fois la génération de nombres premiers pouvant être codés sur k-bits, renvoie un couple : temps moyen d'exécution , bugs "
    l = []
    tps=0
    bug = 0
    for i in range (0,n):
        start = time.time()
        prime=maurer(k,test)
        end = time.time()
        tps += (end-start)

    return (tps/n)

def gen_courbesMaurer() :
    x1=[]
    x2=[] 
    y=[]
    for i in ListeBits:
        x1.append(TestMaurer(600,i,TrialDivision))
        x2.append(TestMaurer(600,i,is_pseudoprime))
        y.append(i)
	print(y)

    return (x1,y),(x2,y)


def traceMaurer(gen1,gen2):
    n=gen1[1]
    plt.plot(n,gen1[0],"r--",label="TrialDivision")
    plt.plot(n,gen2[0],label='is_pseudoprime')
    plt.xlabel("taille en bits")
    plt.ylabel("vitesse de génération en sec")
    plt.legend()
    plt.show()



