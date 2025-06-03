"""
Écrire un programme en Python qui affiche une demi-pyramide en utilisant
des alphabets, en fonction d’un entier N saisi par l’utilisateur.
"""



n = int(input("Entrez un entier N : "))

for i in range(n):
    for j in range(i + 1):
        # Convertir le nombre en lettre (A = 65 en ASCII)
        print(chr(65 + j), end=" ")
    print()
