"""
Écrire un programme en Python qui affiche une demi-pyramide en utilisant *,
en fonction d’un entier N saisi par l’utilisateur.
"""


nombre_ligne = int(input("Entrez le nombre de lignes : "))

for i in range(1, nombre_ligne + 1):
    print("* " * i)
