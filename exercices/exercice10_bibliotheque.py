liste_livre =["Le Hobbit", "Mathilda", "La guerre des étoiles", "L'Odysée", "Le Petit Prince"]

def menu_choix():
    while True :
      print("==========BIBLIOTHEQUE==========")
      print("1.Rechercher un livre \n2.Afficher tout les livre\n3.Quitter")

      try :
   
        choix=input("Que voulez vous faire ?")

        if choix == "1" or choix == "2" or choix =="3":
            return choix
        else:
            print("erreur : choix invalide")

      except ValueError:
          print("Merci de choisir 1 ou 2")


def affichage_un_livre(liste_livre):
   for livre in liste_livre.low().strip:
      if livre in liste_livre:
         print(f"TROUVER: {livre}")
      else :
         print(f"Non trouvé : {livre}")

def affichage_liste():
  return(liste_livre)


def programme():
   while True:
     choix = menu_choix()

     if choix =="1":
      print("Quel livre recherchez vous ? ")
      affichage_un_livre()
     elif choix =="2":
        affichage_liste(liste_livre)
     elif choix == "3":
        print("Au revoir") 
        break

programme()        
   

    