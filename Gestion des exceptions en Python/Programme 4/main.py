"""
Ecrivez un programme Python qui invite l’utilisateur à saisir deux nombres et
qui lève une exception TypeError si les entrées ne sont pas numériques.
"""

def saisir_nombres():
    while True:
        try:
            a = float(input("Veuillez saisir le premier nombre : "))
            b = float(input("Veuillez saisir le deuxième nombre : "))
            return a, b
        except ValueError:
            print("Erreur : Veuillez saisir des valeurs numériques.")

if __name__ == "__main__":
    nombre1, nombre2 = saisir_nombres()
    print(f"Vous avez saisi : {nombre1} et {nombre2}")