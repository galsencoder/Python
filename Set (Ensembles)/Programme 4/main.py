"""
Écrire un programme Python pour supprimer un ou plusieurs éléments d’un ensemble donné.
"""

# Création d'un ensemble avec quelques éléments
ensemble = {1, 2, 3, 4, 5, 6}

# Suppression d'un élément de l'ensemble
ensemble.remove(4)

# Suppression de plusieurs éléments de l'ensemble
ensemble.difference_update({2, 3})

# Affichage de l'ensemble modifié
print("Ensemble après suppression d'éléments :", ensemble)