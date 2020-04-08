import time
import matplotlib
import matplotlib.pyplot as plt
import hashlib


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

    return (tps/n,bug)


def gen_courbes(gen) :
    x= []
    y=[]
    for i in range(5,35):
        global LP
        LP = List_premiers(2**i)
        y.append(TestGen(800,1000,gen))
        x.append(i)

    plt.plot(x,y)
    plt.xlabel("Nombre de divisions successives avant de passer à Miller-Rabin")
    plt.ylabel("Temps de génération")
    plt.show()
