"""
Écrire un programme Python pour générer six nombres flottants
aléatoires dans une plage numérique spécifique exemple (0-100).
"""


import random

def generer_nombres_flottants():
    return [random.uniform(0, 100) for _ in range(6)]

# Exemple d'utilisation
if __name__ == "__main__":
    nombres_flottants = generer_nombres_flottants()
    print("Nombres flottants générés :", *(f"{n:.2f}" for n in nombres_flottants))