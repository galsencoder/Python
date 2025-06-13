"""
Écrire un programme Python pour trouver tous les mots uniques 
et compter la fréquence d’apparition à partir d’une liste donnée de chaînes de caractères en francais.
"""

# Definition de la liste de mots
mots = [
    "chat", "chien", "oiseau", "chat", "chien", "chat", 
    "poisson", "oiseau", "chat", "chien", "poisson"
]

# Fonction pour compter la fréquence des mots
def compter_frequence(mots):
    frequence = {}
    for mot in mots:
        if mot in frequence:
            frequence[mot] += 1
        else:
            frequence[mot] = 1
    return frequence


# Appel de la fonction et affichage des résultats
frequence_mots = compter_frequence(mots)
for mot, count in frequence_mots.items():
    print(f"Le mot '{mot}' apparaît {count} fois.")

