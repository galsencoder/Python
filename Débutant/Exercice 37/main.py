"""
Écrire un programme en Python qui affiche une demi-pyramide en 
utilisant des nombres, en fonction d’un entier N saisi par l’utilisateur.
"""

n = int(input("Entrez un entier N : "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
