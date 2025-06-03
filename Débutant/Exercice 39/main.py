"""
Écrire un programme en Python qui affiche une demi-pyramide inversée en
utilisant des *, en fonction d’un entier N saisi par l’utilisateur.
"""


n = int(input("Entrez un entier N : "))

for i in range(n, 0, -1):
    print("* " * i)
