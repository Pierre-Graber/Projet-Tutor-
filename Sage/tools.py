from sage.all import*
import hashlib

#=================================================================================================================
# La Liste de premiers utilisées pour les "TrialDivisions"
#===============================================================================




#constante B pour le nombre de divisions successives nécessaires pour l'algo random_search
B = 2**20

def List_premiers(n):
    i=0
    l=[]
    while i <= sqrt(n):
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


#=================================================================================================================
# Attaque de Pollard
#===============================================================================
def PollardAttack(N) :
    B = 2
    a = 2
    while True:
        a = power_mod(a, B, N)
        p = xgcd(a-1, N)
        if p[0] != 1 :
            print ("p = "+str(p[0]))
            print ("q = "+str(N/p[0]))
            break
        B += 1
