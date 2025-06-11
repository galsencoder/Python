"""
Écrire un programme Python pour vérifier si deux ensembles donnés n’ont pas d’éléments en commun.
"""

# Definition des ensembles
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {6, 7, 8, 9, 10}

# Vérification des éléments communs
if ensemble1.isdisjoint(ensemble2):
    print("Les deux ensembles n'ont pas d'éléments en commun.")
else:
    print("Les deux ensembles ont des éléments en commun.")