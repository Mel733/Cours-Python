#C'est quoi une exception:
nombre = int("abc")
# ValueError : "abc" n'est pas un nombre, Python ne sait pas le convertir.
# Sans protection, le programme S'ARRÊTE ici avec un message d'erreur rouge.
# Une exception est une erreur qu'on peut intercepter pour que le programme continue.
#-----------------------------------------------------------------------------------------------
#Try/except : intercepter l'erreur:
try:
    # On met ici le code qui PEUT planter.
    nombre = int(input())
    # Si l'utilisateur tape "12" -> nombre = 12, aucune erreur.
    # Si l'utilisateur tape "abc" -> ValueError, Python saute directement au except.
    print("Tout va bien")
    # Cette ligne n'est PAS exécutée si l'erreur arrive juste au-dessus.
except ValueError:
    # Ce bloc ne s'exécute que si une ValueError s'est produite dans le try.
    print("Ce n'est pas un nombre")
#------------------------------------------------------------------------------------------
#Execptions les plus courantes:
int("abc")           # ValueError : valeur invalide pour la conversion
10 / 0               # ZeroDivisionError : division par zéro
[1, 2, 3][5]         # IndexError : l'indice 5 n'existe pas (la liste a 3 éléments)
{"a": 1}["b"]        # KeyError : la clé "b" n'existe pas dans le dictionnaire
open("inconnu.txt")  # FileNotFoundError : le fichier n'existe pas
"a" + 5              # TypeError : on ne peut pas additionner un texte et un nombre
#--------------------------------------------------------------------------------------------




