"""
Écrire un programme Python pour supprimer un ou plusieurs tuple(s) vide(s) d’une liste de tuple(s).
"""

# Définition de la liste de tuples
tuples_list = [(1, 2, 3), (), (4, 5), (), (6, 7, 8)]

# Suppression des tuples vides
tuples_list = [t for t in tuples_list if t]

# Affichage de la liste modifiée
print(tuples_list)