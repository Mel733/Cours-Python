# C'est quoi une exception :
nombre = int("abc")
# ValueError : "abc" n'est pas un nombre.
# Sans protection, le programme S'ARRÊTE ici avec un message d'erreur.
# Une exception est une erreur qu'on peut intercepter pour que le programme continue.
#-------------------------------------------------------------------------
# Try/except : intercepter l'erreur
try:
    nombre = int(input())   # code qui PEUT planter
    print("Tout va bien")   # non exécuté si l'erreur arrive juste au-dessus
except ValueError:          # s'exécute seulement si une ValueError se produit dans le try
    print("Ce n'est pas un nombre")
#-------------------------------------------------------------------------
# Exceptions les plus courantes :
int("abc")           # ValueError : valeur invalide pour la conversion
10 / 0               # ZeroDivisionError : division par zéro
[1, 2, 3][5]         # IndexError : l'indice n'existe pas
{"a": 1}["b"]        # KeyError : la clé n'existe pas
open("inconnu.txt")  # FileNotFoundError : le fichier n'existe pas
"a" + 5              # TypeError : texte + nombre impossible
#-------------------------------------------------------------------------
# Plusieurs except + "as" : Python exécute le premier except qui correspond.
# "as erreur" stocke l'exception pour afficher son message.
try:
    montant = float(input())
    resultat = 100 / montant
except ValueError:
    print("Montant invalide")
except ZeroDivisionError as erreur:
    print(f"Problème : {erreur}")
#-------------------------------------------------------------------------
# raise : DÉCLENCHER soi-même une exception (try/except sert à la RATTRAPER).
# Le raise arrête la fonction (comme un return) et l'erreur remonte jusqu'au try/except.
def retirer(solde, montant):
    if montant <= 0:
        raise ValueError                          # montant invalide
    if montant > solde:
        raise ValueError("Solde insuffisant")     # avec un message
    return solde - montant

try:
    retirer(50, 80)
except ValueError as erreur:
    print(erreur)                                 # Solde insuffisant
#-------------------------------------------------------------------------
# Créer sa propre exception : une classe qui hérite de Exception
class SoldeInsuffisant(Exception):
    pass                                          # la classe sert de "type d'erreur"

try:
    raise SoldeInsuffisant("Refusé : il manque 30.00 €")
except SoldeInsuffisant as erreur:                # ne rattrape QUE cette erreur
    print(erreur)
# Si une exception hérite d'une autre, mettre la plus précise EN PREMIER.
#-------------------------------------------------------------------------
# Résumé :
# try     : code qui peut planter
# except  : que faire si l'erreur arrive
# raise   : déclencher une erreur soi-même
# else    : s'exécute si le try n'a pas planté
# finally : s'exécute dans tous les cas
