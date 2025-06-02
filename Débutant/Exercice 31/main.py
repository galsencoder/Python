"""
Écrire un programme Python qui calcule le volume d'une sphère.
"""


import math

rayon = float(input("Entrez le rayon de la sphère : "))
volume = 4.0 / 3.0 * math.pi * math.pow(rayon, 3)

print(f"Le volume de la sphère est : {volume:.2f}")