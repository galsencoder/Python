"""
Ecrivez un programme en Python pour inverser les chiffres d'un nombre saisi par l'utilisateur.
"""


nbr = int(input("Entrez un nombre entier : "))

if nbr < 0 :
    inverse = - int(str(abs(nbr))[::-1])
else :
    inverse = int(str(nbr)[::-1])

print(f"L'inverse de {nbr} est {inverse}")