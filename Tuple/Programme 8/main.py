"""
Écrire un programme Python pour supprimer le caractère ‘n’ du tuple.
"""

# Définition du tuple
mon_tuple = ('g', 'a', 'l', 's', 'e', 'n')

# Suppression du caractère 'n'
mon_tuple = tuple(i for i in mon_tuple if i != 'n')

# Affichage du résultat
print("Le tuple après suppression :", mon_tuple)