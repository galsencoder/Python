"""
Écrire un programme en Python qui prend deux entiers de
l'utilisateur (un nombre de base et un exposant) et calcule la puissance.
"""

a = int(input("Entrez la base : "))
n = int(input("Entrez l'exposant : "))

expo = pow(a,n)

print(f"{a} exposant {n} est {expo}")
