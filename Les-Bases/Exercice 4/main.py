"""
Ecrivez un programme en Python qui demande l’âge et permet de renseigner sa catégorie sachant que les catégories sont les suivantes:
Gamin de 6 à 7 ans
Pupille de 8 à 9 ans
Jeune de 10 à 11 ans
Cadet après 12 ans
"""

age = int(input("Saisissez l'âge de l'enfant : "))

if 6 <= age <= 7:
    print("Vous êtes Gamin")
elif 8 <= age <= 9:
    print("Vous êtes Pupille")
elif 10 <= age <= 11:
    print("Vous êtes Jeune")
elif age >= 12:
    print("Vous êtes Cadet")
else:
    print("Cette catégorie n'existe pas.")

