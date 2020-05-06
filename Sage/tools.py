# coding: utf-8
from sage.all import*
import hashlib

#=================================================================================================================
# La Liste de premiers utilisées pour les "TrialDivisions"
#===============================================================================




#constante B pour le nombre de divisions successives nécessaires pour l'algo random_search
B = 2**10

def List_premiers(n):
    i=0
    l=[]
    while i <= (n):
        i = next_prime(i)
        l.append(i)
    return l

# Liste des nombres premiers < 2**20.
LP=List_premiers(B)




#=================================================================================================================
# Trois fonctions nécessaires pour l'algo NIST
#===============================================================================

#-----------------------------------------------------------------------

def bin_to_dec(L):
    ret = 0
    for i in range (0,len(L)):
        if L[i] == 1 :
            ret+= 2**i
    return ret

#-----------------------------------------------------------------------   


def LongDivision(n,m):
    i=1
    while i*m <= n:
        i=i+1
    return (i-1,n-(i-1)*m)

#-----------------------------------------------------------------------


def H(s):
    s=str(s)
    sha2 = hashlib.sha256
    a=sha2(s.encode('utf-8'))
    return ZZ(a.hexdigest(),16)


#======================================================================================
def ecmExpectedTime(gen,k):
	module = gen(k) * gen(k)
	return ecm.time(module,30)

def ecmTime(gen,k):
	module = gen(k) * gen(k)
	return tps(ecm.factor,module)

#======================================================================================

def tps(f,k):
	start = time.time()
	f(k)
	end = time.time()
	return end-start



#=================================================================================================================
# liste utile :

ListeBits = [8,12,16,32,56,64,128,160,256,512,1024]







