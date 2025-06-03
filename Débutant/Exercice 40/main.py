"""
Écrire un programme en Python qui affiche une demi-pyramide inversée
en utilisant des nombres, en fonction d’un entier N saisi par l’utilisateur.
"""


n = int(input("Entrer le nombre de lignes : "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
