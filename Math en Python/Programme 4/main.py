"""
Écrire un programme Python pour afficher un nombre complexe et ses parties réelle et imaginaire.
"""

def afficher_nombre_complexe(nombre_complexe):
    partie_reelle = nombre_complexe.real
    partie_imaginaire = nombre_complexe.imag
    return f"Nombre complexe: {nombre_complexe}, Partie réelle: {partie_reelle}, Partie imaginaire: {partie_imaginaire}"


# Exemple d'utilisation
if __name__ == "__main__":
    nombre_complexe = complex(input("Entrez un nombre complexe (par exemple, 3+4j): "))
    resultat = afficher_nombre_complexe(nombre_complexe)
    print(resultat)