"""
Écrire un programme en Python permettant de calculer le plus grand commun
diviseur (PGCD) entre deux nombres entiers entrés par l'utilisateur.
"""

a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxieme entier : "))

x, y = a, b

while b != 0:
    reste = a % b
    a = b
    b = reste

print(f"PGCD({x},{y}) : {a}")