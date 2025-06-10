"""
Écrire un programme Python pour vérifier si un ensemble est un sous-ensemble d’un autre ensemble.
"""

# Création de deux ensembles avec quelques éléments
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {1, 2, 3}

# Vérification si ensemble2 est un sous-ensemble de ensemble1
est_sous_ensemble = ensemble2.issubset(ensemble1)

# Affichage du résultat
print("L'ensemble2 est un sous-ensemble de l'ensemble1 :", est_sous_ensemble)