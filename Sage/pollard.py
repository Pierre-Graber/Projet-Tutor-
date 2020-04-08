import math
 
def SquareAndMultiply(base,exponent,modulus):
    binaryExponent = []
    while exponent != 0:
        binaryExponent.append(exponent%2)
        exponent = exponent/2
    result = 1
    binaryExponent.reverse()
    for i in binaryExponent:
        if i == 0:
            result = (result*result) % modulus
        else:
            result = (result*result*base) % modulus
    return result
 
def egcd(a, b) :
    if a == 0 :
        return (b, 0, 1)
    else :
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
 
def PollardAttack(N) :
    B = 2
    a = 2
    while True:
        a = SquareAndMultiply(a, B, N)
        p = egcd(a-1, N)
        if p[0] != 1 :
            print ("p = "+str(p[0]))
            print ("q = "+str(N/p[0]))
            break
        B += 1
 
if __name__ == "__main__":
    N =77048380391019655282606089223
    PollardAttack(N)
