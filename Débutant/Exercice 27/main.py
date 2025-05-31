"""
Écrire un programme Python pour afficher les nombres
impairs de 1 à 10. Afficher un nombre par ligne.
"""

print("Les nombres impairs de 1 à 10 sont : ")

for i in range(1,11) :
    if i % 2 != 0 :
        print(i)