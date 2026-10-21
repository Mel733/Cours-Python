liste_livre =["Le Hobbit", "Mathilda", "La guerre des étoiles", "L'Odysée", "Le Petit Prince"]

def menu_choix():
    while True :
      print("==========BIBLIOTHEQUE==========")
      print("1.Rechercher un livre \n2.Afficher tout les livre\n3.Quitter")

      try :
   
        choix=int(input("Que voulez vous faire ?"))

        if choix == 1 or choix == 2 or choix ==3:
            return choix
        else:
            print("erreur : choix invalide")

      except ValueError:
          print("Merci de choisir 1 ou 2 ou 3")


def affichage_un_livre():
   saisie = input("Quel livre recherchez vous ? ")
   saisie = saisie.lower().strip()
   print()

   trouve = False
   for livre in liste_livre:
        if livre.strip().lower()== saisie:
         trouve = True
         break

   if trouve :
      print(f"TROUVER: {saisie}")
   else :
      print(f"Non trouvé : {saisie}")

def affichage_liste():
  for livre in liste_livre:
     print()
     print(livre)
     print()

def programme():
   while True:
     choix = menu_choix()

     if choix ==1:
      
      affichage_un_livre()
     elif choix ==2:
        print()
        affichage_liste()
        print()
     elif choix == 3:
        print("Au revoir") 
        break

programme()        
   

    