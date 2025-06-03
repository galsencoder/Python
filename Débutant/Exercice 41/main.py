"""
Écrire un programme en Python qui affiche une Pyramide complète avec des *,
en fonction d’un entier N saisi par l’utilisateur.
"""


n = int(input("Entrez le nombre de lignes : "))

for i in range(1, n + 1):
    espaces = n - i
    etoiles = 2 * i - 1
    print(" " * espaces + "*" * etoiles)
