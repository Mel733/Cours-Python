musiques =["Bad Romance", "Highway To Hell", "Beat It"]

def menu():
    while True:
        print("=====MA PLAYLIST=====")
        print("1.Ajouter une chanson\n2.Afficher la playlist\n3.Rechercher une chanson\n4.Supprimer\n5.Quitter")

        try:
            choix=int(input("Que voulez vous faire ? "))
            if 1<= choix <=5:
                return choix
            else :
                print("Veuillez rentrer un choix valide")
        except ValueError:
            print("Veuillez entrer un nombre entre 1 et 5")
            print()

def ajouter_musique():
     ajout=input("Quelle musique voulez vous ajouté ? ")
     ajout_propre = ajout.strip().lower().title()
     if ajout_propre =="":
         print("Erreur, le titre est vide")
     elif ajout_propre in musiques:
        print("Musique déjà dans la playlist")
     else :
         musiques.append(ajout_propre)
         print(f"Musique : {ajout_propre} ajouté a la playliste")

def afficher_playlist():

    #not musique est true quand la liste est vide
    if not musiques:
        print("Playlist Vide")
    else: 
        musiques.sort() #sinon au trie les musiques dans l'ordre alphabétique
        for numero, musique in enumerate(musiques, start=1): #donne un numéro et une musique chaque tour grace au enumerate (on commence a 1)
            print(f"{numero}. {musique}") #affiche le numéro et de la musique


def rechercher_musique():
    saisie_recherche=input("Quelle musique voulez voux recherchez ?")
    saisie_propre = saisie_recherche.strip().lower()

    trouve = False #reste false tant que rien n'a été touvé
    for musique in musiques: #on parcourt chaque musique dans la playlist
          if saisie_propre in musique.lower(): #on verifie si le contenue tape correstpont a un titre(tout est mis en minuscule ppur comparer)
             print(f"Trouvé: {musique}") #affiche le titre complet selon la recherche(affiche le titre tel quel dans la liste)
             trouve = True#on note que on a trouvé un résultat

          #s'execute seulement apres avoir parcourue toute la liste
    if not trouve:
        print("Pas trouvé")

def supprimer_musique():
    musique_suppr=input("Quelle musique voulez vous supprimer ? ")
    musique_suppr_propre = musique_suppr.lower().strip().title()
    if musique_suppr_propre in musiques:
        musiques.remove(musique_suppr_propre)
        print(f"La musique {musique_suppr_propre} a été supprimé")
    else:
        print("Musique inexistante")

def main():
    while True:
        choix = menu()
        print()
        if choix == 1:
            ajouter_musique()
        elif choix == 2:
            afficher_playlist()
        elif choix == 3:
            rechercher_musique()
        elif choix == 4:
            supprimer_musique()
        elif choix == 5:
            print("Au revoir")
            break

main()