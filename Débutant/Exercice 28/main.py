"""
Écrire un programme Python pour afficher les nombres
compris entre 1 et 10 divisibles par 2, 4 et les deux.
"""

print("Les nombres compris entre 1 et 10 divisibles par 2, 4 et les deux sont : ")

for i in range(1, 11):
    if i % 4 == 0:
        print(f"{i} est divisible par 2 et 4")
    elif i % 2 == 0:
        print(f"{i} est divisible par 2")