"""
Projet 4 : Filtre de commentaires toxiques

Objectif :
Créer un filtre qui détecte si un commentaire contient des mots interdits
(insultes, spam, etc.) en utilisant des ensembles.

Étapes :
Charger une liste de mots interdits (liste noire)
Comparer avec les mots du commentaire
Afficher les mots détectés ou bloquer le commentaire
"""

# Liste noire de mots interdits
blacklist = {
    "insulte1",
    "insulte2",
    "spam",
    "mauvaismot",
    "toxique",
    "haine",
    "violence",
    "discrimination",
    "harcèlement",
    "propos haineux"

}

def filtrer_commentaire(commentaire):
    """
    Filtre un commentaire et retourne les mots interdits détectés.
    """
    mots = set(commentaire.lower().split())
    mots_detectes = mots.intersection(blacklist)
    return mots_detectes


if __name__ == "__main__":
    commentaire = input("Entrez un commentaire : ")
    mots_detectes = filtrer_commentaire(commentaire)

    if mots_detectes:
        print("Commentaire bloqué. \nMots interdits détectés :", ", ".join(mots_detectes))
    else:
        print("Commentaire autorisé.")



