"""
Écrire un programme en Python qui vérifie si une chaîne est un palindrome.
Un palindrome est un mot qui s’écrit de la même manière après l’inversion
de ce dernier. ‘ada’ est un palindrome.
"""


chaine = input("Entrez une chaine de caractere : ")

chaine_inverse = ""
nombre_caractere = len(chaine) -1


while nombre_caractere >= 0 :
    chaine_inverse += chaine[nombre_caractere]
    nombre_caractere -= 1


if chaine == chaine_inverse :
    print(f"{chaine} est un palindrome.")
else :
    print(f"{chaine} n'est pas palindrome.")