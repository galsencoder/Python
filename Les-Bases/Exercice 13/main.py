"""
Écrire un programme Python pour échanger deux nombres sans utiliser une troisième variable.
"""

a = int(input("Entrez la valeur de A : "))
b = int(input("Entrez la valeur de B : "))

print(f"Avant l'echange on a : A = {a} et B = {b}")

a, b = b, a

print(f"Apres l'echange on a : A = {a} et B = {b}")