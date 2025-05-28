"""
Ecrivez un programme en Python qui calcule la somme de 1 à N,
où N est saisi par l'utilisateur. En utilisant la boucle "while".
"""

N = int(input("Entrez un entier positif : "))

somme = 0
i = 1

while i <= N:
    somme += i
    i += 1

print(f"La somme de 1 à {N} est {somme}")