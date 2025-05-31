"""
Écrire un programme Python pour vérifier si un nombre est pair ou impair.
"""

a = int(input("Entrez un nombre entier : "))

if a % 2 == 0 : 
    print(f"{a} est pair.")
else : 
    print(f"{a} est impair.")