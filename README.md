# Projet-Tutoré-

L'ensemble du projet est découpé en plusieurs fichiers dans le dossier "Sage".
Dans le dossier Sage se trouvent tous les algorithmes présentés dans le rapport de ce Projet Tutoré.

Afin d'utiliser les algorithmes : 
Depuis un terminal, se placer dans le bon dossier, puis après avoir lancé Sage, importer tout le contenu du projet grâce à la commande : 
           - sage: load("loadALL.py") 

Une fois le fichier loadALL.py chargé : 

           - Exemples d'utilisation des 4 algorithmes : 
           Pour des premiers codés sur 1024 bits :
           
                      1) Random_search : 
                               - sage: RS(1024)
                      2) Gordon :
                               - sage: gordon(1024)
                      3) DSA par Nist :
                               - sage: nist(8)
                      4) Maurer :
                               - maurer(1024)

La fonction GenerationAverageTime(n,k,algo) prend en entrée deux entiers et un des 4 algorithmes cités plus haut.    

           Exemples de tests retournant le temps moyen de génération :
           
                      - Si on veut tester le temps moyen (sur n=1000 essais ici) pour la génération d'un premier de k=2048 bits avec l'algorithme de Gordon : 
                              - sage: GenerationAverageTime(1000,2048,gordon)
                              
                       - Même procédé pour des premiers de 1024 bits avec l'algorithe de Maurer :
                              - sage: GenerationAverageTime(1000,2048,maurer)
                      
                      



           
Fichiers "tools.py" : 
           - Ensemble des fonctions nécessaires pour utiliser les algorithmes, en particulier pour maurer qui a besoin de fonction de                    hachage mais aussi de conversion binaire vers décimale.


           


