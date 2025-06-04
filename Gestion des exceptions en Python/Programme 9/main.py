"""
Écrire un programme Python qui exécute une opération de liste
et gère une exception AttributeError si l’attribut n’existe pas.
"""


def afficher_longueur(liste):
    try:
        # Essayer d'obtenir la longueur de la liste avec len()
        longueur = len(liste)
        print("Longueur de la liste :", longueur)
    except AttributeError:
        print("Erreur : Impossible de déterminer la longueur de l'objet fourni.")

# Exemple d'utilisation
if __name__ == "__main__":
    ma_liste = [1, 2, 3, 4, 5]
    afficher_longueur(ma_liste)