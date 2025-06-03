"""
Écrire un programme Python pour ajouter, soustraire, multiplier et diviser deux fractions.
"""

from fractions import Fraction
def addition(fraction1, fraction2):
    return fraction1 + fraction2

def soustraction(fraction1, fraction2):
    return fraction1 - fraction2

def multiplication(fraction1, fraction2):
    return fraction1 * fraction2

def division(fraction1, fraction2):
    return fraction1 / fraction2 if fraction2 != 0 else "Division par zéro"

# Exemple d'utilisation
if __name__ == "__main__":
    fraction1_str = input("Entrez la première fraction (ex: 1/2): ")
    fraction2_str = input("Entrez la deuxième fraction (ex: 1/4): ")

    # Convertir les entrées en objets Fraction
    fraction1 = Fraction(fraction1_str)
    fraction2 = Fraction(fraction2_str)

    print("Addition:", addition(fraction1, fraction2))
    print("Soustraction:", soustraction(fraction1, fraction2))
    print("Multiplication:", multiplication(fraction1, fraction2)) 
    print("Division:", division(fraction1, fraction2))