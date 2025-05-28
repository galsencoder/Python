"""
Écrire un programme en Python qui affiche la table de multiplication d'un entier saisi par l'utilisateur, en utilisant la boucle "for".
"""
a = int(input("Entrez un entier positif : "))

print(f"La table de multiplication de {a} : ")
multi = 1

for i in range(11) :
    print(f"{a} x {i} = {a*i}")