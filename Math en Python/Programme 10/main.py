"""
Ecrivez un programme Python pour mélanger les éléments suivants de manière aléatoire.

Exemple:

[1, 2, 3, 4, 5] -> [4, 1, 3, 2, 5]
"""


import random
def melanger_elements(liste):
    random.shuffle(liste)
    return liste

# Exemple d'utilisation
if __name__ == "__main__":
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    elements_melanges = melanger_elements(elements)
    print("Liste mélangée :", elements_melanges)