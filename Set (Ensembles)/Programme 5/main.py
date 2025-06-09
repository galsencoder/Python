"""
Écrire un programme Python pour supprimer un élément d’un ensemble s’il est présent dans l’ensemble.
"""

# Création d'un ensemble avec quelques éléments
ensemble = {1, 2, 3, 4, 5}

# Élément à supprimer
element_a_supprimer = 3

# Suppression de l'élément s'il est présent dans l'ensemble
ensemble.discard(element_a_supprimer)

# Affichage de l'ensemble modifié
print("Ensemble après suppression de l'élément :", ensemble)