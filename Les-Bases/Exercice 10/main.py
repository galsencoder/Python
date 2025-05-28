"""
Écrire un programme en Python qui demande à l'utilisateur deux nombres a et b
et lui indique ensuite si le produit de ces deux nombres est positif ou négatif.
On prévoit dans le programme le cas où le produit peut être nul.
"""

a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxieme nombre : "))

if a * b > 0 :
    print("Le produit est positif.")
elif a * b < 0 :
    print("Le produit est negatif.")
else :
    print("Le produit est nul.")