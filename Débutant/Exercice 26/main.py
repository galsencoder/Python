"""
Écrire un programme Python pour compter les lettres,
les espaces, les chiffres et les autres caractères d’une chaîne saisie.
"""

chaine = input("Entrez une chaine de caracteres : ")

lettres = 0
espaces = 0
chiffres = 0
autres = 0

for caractere in chaine :
    if caractere.isalpha():
        lettres += 1
    elif caractere.isdigit():
        chiffres += 1
    elif caractere.isspace():
        espaces += 1
    else:
        autres += 1

print(f"Cette chaine de caracteres comporte : ")
print(f"{lettres} lettres")
print(f"{espaces} espaces")
print(f"{chiffres} chiffres")
print(f"et {autres} autres caractères ")