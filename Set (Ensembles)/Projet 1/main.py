"""
Projet 1 : Détecteur de mots uniques dans plusieurs textes

Objectif :
Analyser plusieurs fichiers texte et déterminer :
Les mots communs à tous les textes
Les mots uniques à chaque texte
Les mots présents dans au moins deux textes
en français.
"""

def mots_du_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            texte = f.read()
            # Nettoyage des caractères spéciaux et séparation des mots
            mots = set(texte.lower().split())
            return mots
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
        return set()