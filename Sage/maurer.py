from primality_tests import*

def maurer(k):
    b1 = True
    b2 = True
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
