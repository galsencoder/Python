"""
Écrivez un programme Python qui invite l’utilisateur à saisir
un nombre entier et qui lève une exception ValueError si le
nombre saisi n’est pas un nombre entier valide.
"""

def saisir_nombre_entier():
    while True:
        try:
            return int(input("Veuillez saisir un nombre entier : "))
        except ValueError:
            print("Erreur : Ce n'est pas un nombre entier valide.")

if __name__ == "__main__":
    nombre = saisir_nombre_entier()
    print(f"Vous avez saisi le nombre entier : {nombre}")