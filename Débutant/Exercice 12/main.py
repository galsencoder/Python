"""
Écrire un programme Python pour calculer la somme de deux entiers
et retourner TRUE si la somme est égale au troisième entier.
"""

a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxieme entier : "))
c = int(input("Entrez le troisieme : "))

somme = a + b

if somme == c :
    print("True")
else :
    print("False")