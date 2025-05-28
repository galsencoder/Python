"""
Écrire un programme en Python pour calculer la factorielle d’un nombre entier saisi par l’utilisateur.
(Remarque: le factoriel de 5, qui s’écrit 5! = 5 × 4 × 3 × 2 × 1).
"""

n = int(input("Entrez un nombre positif : "))

while( n < 0) :
    print("la factorielle n'existe pas pour les nombres négatifs.")
    n = int(input("Veuillez, entrez un nombre positif : "))

facto = 1
for i in range(2,n+1):
    facto *= i

print(f"La factorielle de {n} est {facto}")