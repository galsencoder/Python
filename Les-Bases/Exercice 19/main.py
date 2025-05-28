"""
Écrire un programme en Python qui prend deux entiers de
l'utilisateur (un nombre de base et un exposant) et calcule la puissance.
"""

# Autre methode

a = int(input("Entrez la base : "))
n = int(input("Entrez l'exposant : "))

expo = 1

for i in range(n):
    expo = expo * a

print(f"{a} exposant {n} est {expo}")