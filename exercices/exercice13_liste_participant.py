participants =["Mélodie", "Sélomey", "Melvin", "Thomas", "Mark", "Tim", "Alicia"]#liste participants
def menu(): #fonction pour menu
    while True : #lance a le menu a l'infinie jusqu'a que la saisie soient valide
        print("=====LISTE PARTICIPANTS=====")
        print("1.Ajouter un participant\n2.Afficher les participant\n3.Rechercher un participant\n4.Supprimer un participant\n5.Quitter")
        try : #essaye et execute le valueError en cas d'erreur de saisie
            choix =int(input("Que voulez vous faire ?"))

            if  1<= choix <= 5 : #si le choix est supérieur ou égale a 1 ou inférieur ou égale a 5
             return choix #renvoie la valeur de choix
            else :
              print()
              print("Veuillez choisir un chiffre valide") #message d'erreur si nombre inférieur ou superieur 
        except ValueError: #si la saisie contient des lettres ou autres
           print
           print("Merci de choisir un chiffre entre 1 et 5")

def ajouter_participant(): #fonction ajouter participant
    participant_aj = input("Qui voulez vous ajouter ? ") #demande le nom
    participant_nettoyer = participant_aj.strip().title().lower() #créer une nouvel valeur avec le nom sans espace,en minuscule et avec l'initiale en maj


    if participant_nettoyer == "": #si en nettoyant le nom, exemple : "   "->"", alors afficher message erreur
        print("Vous devez ajouter un nom !")
    elif any(caractere.isdigit() for caractere in participant_nettoyer): #prend chaque caractère dans participant_nettoyer, teste si chaque carectere est un chiffre, le any renvoie true si il y a un chiffre
        print("Le nom ne doit pas contenir de chiffres") #message d'avertissement
    elif participant_nettoyer in participants: #verifie si le participant souhaitant etre ajouter n'existe pas deja dans la liste
        print("Participant existant") #message prevenant l'existance du participant
    else:
        participants.append(participant_nettoyer)#sinon le partcipant_nettoyer rejoin la liste participant
        print(f"{participant_nettoyer} ajouté") #message de reussite a l'ajout
  
    
def afficher_participants():#fonction affichant la liste
   if participants =="": #si la liste est vide un message apparait
      print("Liste Vide, veuillez ajouter au moins un participant")
   else:
    for participant in range(0, len(participants)):#sinon une boucle for va afficher les participant de O(premier participant) a la longuer de la liste.
     print (f"{participants[participant]}") #a chaque tour on va afficher un participant de la liste     

    

def rechercher_participant(): #fonction rechercher participant
   recherche = input("Qui voulez vous rechercher ? ")
   recherche_nettoyer = recherche.lower().strip().title()#recherche nettoyer pour pouvoir comparer avec la liste

   trouve = False # on part du principe qu'on n'a rien trouvé
   for participant in participants: #on regarde chque participant un à un
      if participant == recherche_nettoyer: # si la recherche_nettoyé est identique a un participant
         trouve = True #true car on la trouvé
         break #on sort de la boucle

   if trouve : #apres la boucle on regarde le résultat et on l'affiche
      print("Trouvé")
   else :
      print("Pas trouvé")

def supprimer_participant(): #fonction supprimer un participant
   participant_sup = input("Qui voulez vous supprimer ? ")
   participant_sup_nettoyer = participant_sup.lower().strip().title() #nettoie le participant rentré pour pouvoir l'identifier dans la liste
   if participant_sup_nettoyer in participants : #si le participant_sup_nettoyer est dans la liste participants
      participants.remove(participant_sup_nettoyer) #alors on le supprime de la liste
      print(f"Participant supprimé de la liste : {participant_sup_nettoyer}") #message de reusite
   else :
      print("Utilisateur inexistant") #sinon utilisateur inexsitant

def main(): #fonction programme principal qui appelle les autres fonctions
   while True: #affiche le menu a l'infinie jusqu'a choix ==5
      choix = menu() # on appelle la fonction menu(), et on stocke ce qu'elle renvoie dans la variable choix
      print()
      if choix == 1:
         ajouter_participant()
         print()
      elif choix == 2:
         afficher_participants()
         print()
      elif choix == 3:
         rechercher_participant()
         print()
      elif choix == 4:
         supprimer_participant()
      elif choix == 5 :
         print("Au revoir")
         break   #sort de la bouble, fin du programme

main()
