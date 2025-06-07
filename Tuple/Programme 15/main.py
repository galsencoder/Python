"""
Écrire un programme Python pour décompresser une liste de tuples en listes individuelles.
"""

# Définition de la liste de tuples
tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# Décompression des tuples en listes individuelles
list1, list2, list3 = zip(*tuples_list)

# Affichage des listes
print("Liste 1:", list1)
print("Liste 2:", list2)
print("Liste 3:", list3)