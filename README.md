# Projet-Tutoré-

fonctions du fichier : 

naiveGen : prend en parametre un entier k et retourne un nombre premier pouvant être codé sur k-bits.
           marche bien pour l'instant.

random_search : prend en parametre un entier k et retourne un nombre premier pouvant être codé sur k-bits.
--> à améliorer : la fonction ne marche pas tout le temps, elle retourne une "RunTimeError" : maximum recursion.
                  --> essayer de "catch" l'erreur ou l'exception 


gordon(): prend un paramêtre qui n'influe pas sur le nombre premier retourné. (Par soucis d'uniformité pour ensuite faire un 
testeur générique pour tous les tests).

TestGen1 : prend en parametre 2 entiers n et k et un générateur:
                      - n le nombre d'itérations du test
                      - k le nombre de bits 
                      - naiveGen, random_search, gordon pour l'instant 
                      
                      
exemple : sage : load("projet2.py")
          sage : TestGen1(5,1024,naiveGen)
           'la generation de 5 nombre(s) premier(s) a pris en moyenne 0.0928555965424 secondes'
           


