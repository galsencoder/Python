"""
Écrire un programme Python pour convertir un flottant en rationnel.
"""

from fractions import Fraction
def nombre_rationnel(flottant):
    return Fraction(flottant).limit_denominator()

# Exemple d'utilisation
if __name__ == "__main__":
    nombre_flottant = float(input("Entrez un nombre flottant: "))
    resultat = nombre_rationnel(nombre_flottant)
    print(f"Le nombre rationnel de {nombre_flottant} est {resultat}.")