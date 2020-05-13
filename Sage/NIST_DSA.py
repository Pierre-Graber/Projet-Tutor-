from primality_tests import*
from tools import*
    
def dsa_nist(l):
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
