# # =====================================================================
# LES FONCTIONS
# =====================================================================
#
# Une fonction est un bloc de code réutilisable, auquel on donne un nom.
# On l'écrit UNE fois, puis on l'appelle autant de fois que nécessaire.
# C'est une économie de code : on évite de recopier les mêmes instructions.
#
# Structure d'une fonction :
#
#   def nom_fonction(parametres):    <- définition (la fonction n'est pas encore exécutée)
#       instructions                 <- corps de la fonction (indenté)
#       return resultat              <- valeur renvoyée à celui qui appelle
#
# ---------------------------------------------------------------------
# Les mots-clés importants
# ---------------------------------------------------------------------
#
# def        : introduit la définition d'une fonction ("def" = définir).
#
# Paramètres : variables écrites entre parenthèses dans le def.
#              Ce sont des "cases vides" qui attendent une valeur.
#
# # Arguments  : valeurs réellement données lors de l'appel de la fonction.
#              Elles remplissent les paramètres : l'argument est la valeur
#              que prend le paramètre pendant cet appel.
#
#   def calculer_age(annee):     <- "annee" est le PARAMÈTRE (la case vide)
#   calculer_age(1990)           <- 1990 est l'ARGUMENT (la valeur qui remplit la case)


#
# return     : renvoie une valeur depuis la fonction ET arrête la fonction.
#              Tout ce qui est écrit après le return n'est jamais exécuté.
#
# ---------------------------------------------------------------------
# Les paramètres ne sont PAS toujours obligatoires
# ---------------------------------------------------------------------
#
# Un paramètre sert à donner une information à la fonction.
# Si la fonction a déjà tout ce qu'il lui faut pour travailler,
# elle n'a pas besoin de paramètre : on laisse les parenthèses vides ().
#
# Exemple : afficher toujours le même message, aucune donnée extérieure
# nécessaire.

def afficher_bienvenue():          # aucun paramètre : les parenthèses restent vides
    print("Bienvenue dans le programme !")

afficher_bienvenue()               # aucun argument à donner non plus
# Affiche : Bienvenue dans le programme !

# ---------------------------------------------------------------------
# Le return n'est PAS toujours obligatoire
# ---------------------------------------------------------------------
#
# Un return sert à RENVOYER un résultat, pour pouvoir le réutiliser ensuite
# (le stocker dans une variable, le mettre dans un calcul, etc.).
# Si la fonction fait juste une action (afficher, modifier, enregistrer...)
# et qu'on n'a pas besoin de récupérer un résultat, le return est inutile.
#
# Sans return, la fonction renvoie automatiquement None ("rien").

def saluer(prenom):
    print(f"Bonjour {prenom} !")   # la fonction AFFICHE, elle ne renvoie rien

saluer("Mélodie")                   # Affiche : Bonjour Melvin !

resultat = saluer("Mélodie")
print(resultat)                    # Affiche : None  (aucune valeur renvoyée)

# ---------------------------------------------------------------------
# Différence entre print et return
# ---------------------------------------------------------------------
#
# print  : affiche à l'écran, mais la valeur est perdue ensuite.
# return : renvoie la valeur, qu'on peut alors réutiliser.
#
# Quand utiliser quoi ?
#   - On veut seulement montrer quelque chose        -> print (pas de return)
#   - On veut réutiliser le résultat dans le code    -> return

# ---------------------------------------------------------------------
# EXEMPLE COMPLET (avec paramètre ET return)
# ---------------------------------------------------------------------

# Définition de la fonction
# Paramètre :
#   annee : année de naissance de la personne (ex. : 1990)
def calculer_age(annee):
    # Soustrait l'année de naissance à l'année actuelle (2026)
    return 2026 - annee
    # Rien de ce qui est écrit ici ne serait exécuté (après le return)

# Appel de la fonction : 1990 est l'argument, il prend la place du paramètre "annee"
age = calculer_age(1990)
print(age)   # Affiche : 36


calculer_age(2008)

age = calculer_age (1987)
print(f"Vous avez {age} ans")


def faire_lignes_avec_param(nb_de_fois):#(parametre)
    print("-"*nb_de_fois)

faire_lignes_avec_param(15)
faire_lignes_avec_param(45) 


def faire_lignes_avec_param():#(sans parametre)
    print("-"*40)

faire_lignes_avec_param()
faire_lignes_avec_param() 


def salutation(prenom):
    print(f"Bonjour {prenom}")

salutation("Mélodie")
salutation("Sélomey")
salutation("Melvin")
salutation("Tim")



def carre(nombre):
    return nombre * nombre

print(carre(5))#25
print(carre(10))#100
print(carre(0))#0


def calculatrice(operante1, operante2, operateur):
     if operateur == "+":
         print(operante1 + operante2)
     elif operateur == "-":
         print(operante1-operante2)
     elif operateur =="*":
      print(operante1*operante2)
     elif operateur =="/":
         if operante2 != 0:
             print(operante1/operante2)
         else :
          print("Divison par zéro impossible")
     else:
         print("Erreur : opérateur inconnu")


calculatrice (5, 34, "+")
calculatrice (12, 9, "-")  
calculatrice (56, 78, "*")  
calculatrice (43, 56, "/")
calculatrice(12, 0,"/") 
calculatrice (89, 56, "^")     