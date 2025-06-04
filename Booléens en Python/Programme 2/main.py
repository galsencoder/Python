"""
Écrivez une fonction Python qui prend deux valeurs booléennes
en entrée et renvoie le AND et le OR logiques de ces valeurs.
"""

def logique_and(valeur1, valeur2):
    return valeur1 and valeur2

def logique_or(valeur1, valeur2):
    return valeur1 or valeur2

# Exemple d'utilisation
if __name__ == "__main__":
    valeur1 = bool(int(input("Entrez la première valeur booléenne (0 ou 1): ")))
    valeur2 = bool(int(input("Entrez la deuxième valeur booléenne (0 ou 1): ")))

    print(f"AND logique: {logique_and(valeur1, valeur2)}")
    print(f"OR logique: {logique_or(valeur1, valeur2)}")