"""
Écrire un programme Python pour convertir les jours spécifiés en années,
semaines et jours. Note : Ne pas tenir en compte les années bissextiles.
"""

total_jours = int(input("Entrez le nombre total de jours : "))

annees = total_jours // 365
jours_restants = total_jours % 365

semaines = jours_restants // 7
jours = jours_restants % 7

print(f"{total_jours} jours correspondent à :")
print(f"{annees} annee(s), {semaines} semaine(s) et {jours} jour(s).")