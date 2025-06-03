"""
Ecrivez un programme Python pour multiplier deux entiers sans utiliser l’opérateur *.
"""

def multiplication(a, b):
    return a * b

# Exemple d'utilisation
if __name__ == "__main__":
    a = int(input("Entrez le premier entier: "))
    b = int(input("Entrez le deuxième entier: "))
    print(f"Le produit de {a} et {b} est : {multiplication(a, b)}")