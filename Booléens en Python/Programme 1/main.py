"""
Écrire un programme Python pour vérifier si un nombre donné
est pair ou impair en utilisant des variables booléennes.
"""

def est_pair(nombre):
    return nombre % 2 == 0

def est_impair(nombre):
    return nombre % 2 != 0


# Exemple d'utilisation
if __name__ == "__main__":
    nombre = int(input("Entrez un nombre entier: "))
    
    if est_pair(nombre):
        print(f"{nombre} est un nombre pair.")
    elif est_impair(nombre):
        print(f"{nombre} est un nombre impair.")
    else:
        print("Ce n'est ni un nombre pair ni impair.")