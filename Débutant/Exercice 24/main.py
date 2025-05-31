"""
Écrire un programme en Python qui inverse une chaîne de caractères en utilisant une boucle while.
"""

chaine = input("Entrez une chaine de caractere : ")

chaine_inverse = ""
nombre_caractere = len(chaine) -1


while nombre_caractere >= 0 :
    chaine_inverse += chaine[nombre_caractere]
    nombre_caractere -= 1

print(f"La chaine inversée de {chaine} est {chaine_inverse}")
