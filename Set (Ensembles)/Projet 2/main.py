"""
Générateur de mots de passe "safe"

Objectif :
Créer un programme qui génère un mot de passe sans caractères ambigus, c’est-à-dire sans caractères
similaires (I, l, 1, O, 0, etc.) en utilisant des ensembles.

Contraintes :
Le mot de passe doit contenir au moins 1 majuscule, 1 minuscule, 1 chiffre et 1 caractère spécial.
Tous les caractères doivent appartenir à un ensemble de caractères « sûrs ».
"""

import random
def generer_mot_de_passe(longueur=12):
    caracteres_majuscules = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    caracteres_minuscules = set("abcdefghijklmnopqrstuvwxyz")
    caracteres_chiffres = set("0123456789")
    caracteres_speciaux = set("!@#$%^&*()-_=+[]{}|;:,.<>?")

    # Ensemble de caractères sûrs
    caracteres_surs = caracteres_majuscules.union(caracteres_minuscules, caracteres_chiffres, caracteres_speciaux)

    if longueur < 4:
        raise ValueError("La longueur du mot de passe doit être d'au moins 4 caractères.")

    mot_de_passe = [
        random.choice(list(caracteres_majuscules)),
        random.choice(list(caracteres_minuscules)),
        random.choice(list(caracteres_chiffres)),
        random.choice(list(caracteres_speciaux))
    ]

    mot_de_passe += random.choices(list(caracteres_surs), k=longueur - 4)
    random.shuffle(mot_de_passe)

    return ''.join(mot_de_passe)


if __name__ == "__main__":
    try:
        longueur = int(input("Entrez la longueur du mot de passe (minimum 4) : "))
        mot_de_passe = generer_mot_de_passe(longueur)
        print(f"Mot de passe généré : {mot_de_passe}")
    except ValueError as e:
        print(e)