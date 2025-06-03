"""
Écrire un programme Python pour afficher les nombres séparés par des virgules sous forme de milliers.
1000000 -> 1,000,000
"""

def nombre_avec_milliers(n):
    return f"{n:,}"

# Exemple d'utilisation
if __name__ == "__main__":
    n = int(input("Entrez un nombre entier: "))
    print(f"Le nombre avec des séparateurs de milliers est : {nombre_avec_milliers(n)}")