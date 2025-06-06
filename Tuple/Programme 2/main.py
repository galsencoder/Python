"""
Écrire un programme Python pour ajouter un élément à un tuple.
"""

# Définition du tuple initial
mon_tuple = (1, 2, 3)

# Conversion du tuple en liste pour pouvoir le modifier
ma_liste = list(mon_tuple)

# Ajout de l'élément à la liste
ma_liste.append(4)

# Conversion de la liste modifiée en tuple
mon_tuple = tuple(ma_liste)

# Affichage du nouveau tuple
print(mon_tuple)  # Résultat : (1, 2, 3, 4)


# Note: Tuples sont immuables, donc on ne peut pas ajouter directement un élément.
# Cependant, on peut créer un nouveau tuple avec l'élément ajouté.