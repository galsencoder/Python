"""
Écrire un programme Python pour créer une différence symétrique (Autre methode).
"""

# Création de deux ensembles avec quelques éléments
ensemble1 = {1, 2, 3, 4, 5}
ensemble2 = {4, 5, 6, 7, 8}

# Création de la différence symétrique entre les deux ensembles en utilisant symetric_difference
difference_symetrique = ensemble1.symmetric_difference(ensemble2)

# Affichage du résultat
print("La différence symétrique entre les deux ensembles est :", difference_symetrique)