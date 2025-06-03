"""
Écrivez un programme Python qui accepte le nombre total d’heures travaillées au cours
d’un mois et le montant que l’employé a reçu par heure. Affichez le salaire (avec deux décimales)
de l’employé pour un mois donné.
"""


heures = float(input("Entrez le nombre total d'heures travaillées ce mois ci : "))
taux_horaire = float(input("Entrez le montant reçu par heure (€) : "))

salaire = heures * taux_horaire

print(f"Le salaire pour ce mois est de : {salaire:.2f} €")