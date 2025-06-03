"""
Écrire un programme Python pour additionner, soustraire, multiplier et diviser deux nombres complexes.
"""

def operations_complexes(nombre1, nombre2):
    addition = nombre1 + nombre2
    soustraction = nombre1 - nombre2
    multiplication = nombre1 * nombre2
    division = nombre1 / nombre2 if nombre2 != 0 else "Division par zéro"

    return {
        "addition": addition,
        "soustraction": soustraction,
        "multiplication": multiplication,
        "division": division
    }

# Exemple d'utilisation
if __name__ == "__main__":
    nombre1 = complex(input("Entrez le premier nombre complexe (par exemple, 3+4j): "))
    nombre2 = complex(input("Entrez le deuxième nombre complexe (par exemple, 1+2j): "))
    
    resultats = operations_complexes(nombre1, nombre2)
    
    print(f"Addition: {resultats['addition']}")
    print(f"Soustraction: {resultats['soustraction']}")
    print(f"Multiplication: {resultats['multiplication']}")
    print(f"Division: {resultats['division']}")