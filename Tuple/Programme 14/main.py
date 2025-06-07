"""
Écrire un programme Python pour convertir une liste de tuples en un dictionnaire.
"""

# Definition de la tuple
liste_de_tuples = [("z", 1), ("z", 2), ("x", 3)]

# Conversion de la liste de tuples en dictionnaire
dictionnaire = {}
for cle, valeur in liste_de_tuples:
    if cle not in dictionnaire:
        dictionnaire[cle] = []
    dictionnaire[cle].append(valeur)

# Affichage du dictionnaire
print(dictionnaire)