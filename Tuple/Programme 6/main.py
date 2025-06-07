"""
Écrire un programme Python pour vérifier si un élément existe dans un tuple sans fonction
"""

# Définition du tuple
mon_tuple = (1, 2, 3, 4, 5)

# Élément à rechercher
element = 3

# Vérification de l'existence de l'élément dans le tuple
existe = False
for i in mon_tuple:
    if i == element:
        existe = True
        break

# Affichage du résultat
if existe:
    print("L'élément existe dans le tuple.")
else:
    print("L'élément n'existe pas dans le tuple.")