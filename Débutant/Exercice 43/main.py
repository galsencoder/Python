"""
Écrire un programme en Python qui affiche une Pyramide complète inversée
avec des *, en fonction d'un entier N saisi par l'utilisateur.
"""

n = int(input("Entrer le nombre de lignes: "))

for i in range(n, 0, -1):

    for espace in range(n - i):
        print("  ", end="")

    for j in range(2 * i - 1):
        print("* ", end="")

    print()
