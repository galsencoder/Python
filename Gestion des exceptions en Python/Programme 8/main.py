"""
Écrire un programme Python qui exécute une division et
gère une exception ArithmeticError en cas d’erreur arithmétique.
"""

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erreur : Division par zéro non autorisée."
    except ArithmeticError:
        return "Erreur : Problème arithmétique."

if __name__ == "__main__":
    num1 = float(input("Veuillez saisir le numérateur : "))
    num2 = float(input("Veuillez saisir le dénominateur : "))
    print(division(num1, num2))