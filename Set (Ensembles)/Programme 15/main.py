"""
Écrire un programme Python pour vérifier si une valeur donnée est présente ou non dans un ensemble.
"""

# Création d'un ensemble avec quelques éléments
ensemble = {1, 2, 3, 4, 5}

# Vérification de la présence d'une valeur dans l'ensemble
valeur_a_verifier = 3
est_present = valeur_a_verifier in ensemble

# Affichage du résultat
print("La valeur", valeur_a_verifier, "est présente dans l'ensemble :", est_present)