"""
Écrivez un programme Python qui invite l’utilisateur à saisir un nombre et
qui gère une exception KeyboardInterrupt si l’utilisateur annule la saisie.
"""

def saisie_nombre():
    try:
        nombre = input("Veuillez saisir un nombre : ")
        print(f"Vous avez saisi le nombre : {nombre}")
    except KeyboardInterrupt:
        print("\nSaisie annulée par l'utilisateur.")


# Exemple d'utilisation
if __name__ == "__main__":
    saisie_nombre()