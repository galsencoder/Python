"""
Écrire un programme en Python permettant de calculer le plus grand commun
diviseur (PGCD) entre deux nombres entiers entrés par l'utilisateur.
"""

# Autre methode 

a = int(input("Entrez le premier entier : "))
b = int(input("Entrez le deuxieme entier : "))

x, y = a, b

if a > b :
    minimun = b
else :
    minimun = a

for i in range(1, minimun + 1) :
    if (a % i == 0 and b % i == 0) :
        pgcd = i

print(f"PGCD({x},{y}) = {pgcd}")