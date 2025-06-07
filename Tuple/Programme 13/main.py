"""
Écrire un programme Python pour inverser un tuple.
"""

# Définition du tuple
mon_tuple = (1, 2, 3, 4, 5)

# Inversion du tuple
mon_tuple_inverse = mon_tuple[::-1]

# Affichage du tuple inversé
print("Le tuple inversé est :", mon_tuple_inverse)


# Autres méthodes pour inverser un tuple

"""
# 1. Utilisation de la fonction reversed()
mon_tuple_inverse_reversed = tuple(reversed(mon_tuple))
# Affichage du tuple inversé avec reversed()
print("Le tuple inversé avec reversed() est :", mon_tuple_inverse_reversed)
# 2. Utilisation d'une boucle for 
mon_tuple_inverse_for = ()
for element in mon_tuple:
    mon_tuple_inverse_for = (element,) + mon_tuple_inverse_for

# Affichage du tuple inversé avec une boucle for
print("Le tuple inversé avec une boucle for est :", mon_tuple_inverse_for)

# 3. Utilisation de la fonction join() et de la compréhension de tuple
mon_tuple_inverse_join = tuple(
    [mon_tuple[i] for i in range(len(mon_tuple) - 1, -1, -1)]
)
# Affichage du tuple inversé avec join() et compréhension de tuple
print("Le tuple inversé avec join() et compréhension de tuple est :", mon_tuple_inverse_join)

"""