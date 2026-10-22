#les fonctions 
#def : introduit la definition
# Paramètres : variables déclarées entre parenthèses dans la définition de la fonction. 
# Elles reçoivent les valeurs (arguments) passées lors de l'appel et permettent à la fonction d'effectuer son traitement.
#Fonctions : blocs de code réutilisables, définis avec le mot-clé def.
# Une fonction porte un nom, peut recevoir des paramètres, effectue un
# traitement, puis peut renvoyer un résultat avec return.
# On l'écrit une fois et on l'appelle autant de fois que nécessaire.
# c'est une économie de code avec des instructions sous forme de bloc de code reutilisable

#return : permet de renvoyer une valeur depuis la fonction, tout ce qui est apres ne passe pas

# Paramètres :
#   annee : année de naissance de la personne (ex. : 1990)
def calculer_age(annee):
    # Soustrait l'année de naissance à l'année actuelle (2026)
    return 2026 - annee

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