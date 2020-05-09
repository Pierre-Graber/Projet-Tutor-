import matplotlib.pyplot as plt

def trace(gen1,gen2):
    n=gen1[1]
    plt.plot(n,gen1[0],"r-",label="RS")
    plt.plot(n,gen2[0],"g-",label='G')
    plt.xlabel("taille en bits de p et q")
    plt.ylabel("vitesse de factorisation en sec")
    plt.legend()
    plt.show()
    
    
def traceMaurer(gen1,gen2):
    n=gen1[1]
    plt.plot(n,gen1[0],"r--",label="TrialDivision")
    plt.plot(n,gen2[0],label='is_pseudoprime')
    plt.xlabel("taille en bits")
    plt.ylabel("vitesse de génération en sec")
    plt.legend()
    plt.show()
