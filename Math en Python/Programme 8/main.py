"""
Écrire un programme Python pour générer six nombres entiers
aléatoires dans une plage numérique spécifique exemple (0-100).
"""

import random

def generer_nombres_aleatoires():
    return [random.randrange(0, 100) for _ in range(6)]

# Exemple d'utilisation
if __name__ == "__main__":
    nombres_aleatoires = generer_nombres_aleatoires()
    print("Nombres aléatoires générés :", *nombres_aleatoires)