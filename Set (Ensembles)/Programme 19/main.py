"""
Crée une fonction qui retourne un nouvel ensemble nettoyé, sans "" ni None.
"""

def nettoyer_ensemble(ensemble):
    return {element for element in ensemble if element not in ("", None)}



ensemble_exemple = {"chat", "", "chien", None, "oiseau", "poisson"}
ensemble_nettoye = nettoyer_ensemble(ensemble_exemple)
print(ensemble_nettoye)