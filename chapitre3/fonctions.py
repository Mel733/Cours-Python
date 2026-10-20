#les fonctions 
#def : introduit la definition
#paramètres : valeur que la fonction peut recevoir pour affectuer son traitement
#return : permet de renvoyer une valeur depuis la fonction, tout ce qui est apres ne passe pas

def calculer_age (annee):
    return 2026 - annee

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