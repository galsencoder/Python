"""
Écrire un programme Python pour gérer une exception ZeroDivisionError
lors de la division d’un nombre par zéro.
"""


def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Erreur : Division par zéro n'est pas autorisée."
    else:
        return f"Le résultat de la division est : {result}"
    

# Exemple d'utilisation
if __name__ == "__main__":
    num1 = float(input("Entrez le numérateur : "))
    num2 = float(input("Entrez le dénominateur : "))
    
    print(division(num1, num2))