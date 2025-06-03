"""
Écrire un programme en Python qui affiche une Pyramide complète
avec des nombres, en fonction d’un entier N saisi par l’utilisateur.
"""


n = int(input("Entrer le nombre de lignes : "))

for i in range(1, n + 1):

    print("  " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()
