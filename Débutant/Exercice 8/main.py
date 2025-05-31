"""
Ecrivez un programme en Python pour inverser les chiffres d'un nombre saisi par l'utilisateur.
"""

# Autre methode

nombre = int(input("Entrez un nombre : "))

negatif = False
if nombre < 0:
    negatif = True
    nombre = - nombre
while nombre > 0:
    dernier_chiffre = nombre % 10
    nombre_inverse = nombre_inverse * 10 + dernier_chiffre
    nombre //=  10


if negatif:
    nombre_inverse = - nombre_inverse

print("Le nombre inversé est", nombre_inverse)
