musiques =["Bad Romance", "Highway To Hell", "Beat It"]

def menu():   #fonction menu
    while True:   #lance le programme a l'infinie
        print("=====MA PLAYLIST=====")
        print("1.Ajouter une chanson\n2.Afficher la playlist\n3.Rechercher une chanson\n4.Supprimer\n5.Quitter")

        try:   #tente d'exécuter ce bloc ; si une exception survient, on passe au except
            choix=int(input("Que voulez vous faire ? "))
            if 1<= choix <=5:   #si le choix est supérieur ou égale a 1 ou inférieur ou égale a 5
                return choix    #renvoie la valeur de choix
            else :
                print("Veuillez rentrer un choix valide")   #message d'erreur si nombre inférieur ou superieur 
        except ValueError:   #si la saisie contient des lettres ou autres
            print("Veuillez entrer un nombre entre 1 et 5")
            print()

def ajouter_musique():   #fonction pour ajouter une musique
     ajout=input("Quelle musique voulez vous ajouté ? ")   #demande le titre
     ajout_propre = ajout.strip().lower().title()     #créer une nouvel valeur avec le titre propre sans espace,en minuscule et avec l'initiale en majuscule
     if ajout_propre =="":     #si en nettoyant le nom, exemple : "   "->"", alors afficher message erreur
         print("Erreur, le titre est vide")
     elif ajout_propre in musiques:      #verifie si l'ajout propre existe deja dans la playlist
        print("Musique déjà dans la playlist")
     else :
         musiques.append(ajout_propre)     #sinon ajouter le titre dans la playlist
         print(f"Musique : {ajout_propre} ajouté a la playliste")

def afficher_playlist():

    #not musique est true quand la liste est vide
    if not musiques:
        print("Playlist Vide")
    else: 
        musiques.sort()    #sinon au trie les musiques dans l'ordre alphabétique
        for numero, musique in enumerate(musiques, start=1):    #donne un numéro et une musique chaque tour grace au enumerate (on commence a 1)
            print(f"{numero}. {musique}")    #affiche le numéro qui va avec un titre a chaque tour


def rechercher_musique():
    saisie_recherche=input("Quelle musique voulez voux recherchez ? ")
    saisie_propre = saisie_recherche.strip().lower()    #nettoie la saisie pour faciliter la recherche

    trouve = False    #reste false tant que rien n'a été touvé
    for musique in musiques:     #on parcourt chaque musique dans la playlist
        if saisie_propre in musique.lower():      #on verifie si le contenue taper correspond a un titre dans la playlist(tout est mis en minuscule pour comparer)
            print(f"Trouvé: {musique}")        #affiche le titre complet selon la recherche(affiche le titre tel quel dans la liste)
            trouve = True       #on note que on a trouvé un résultat

          #s'execute seulement apres avoir parcourue toute la liste
    if not trouve:
        print("Pas trouvé")

def supprimer_musique():
    musique_suppr=input("Quelle musique voulez vous supprimer ? ")
    musique_suppr_propre = musique_suppr.lower().strip().title()      #nettoie la saisie
    if musique_suppr_propre in musiques:         #si le titre saisie est dans la playlist
        musiques.remove(musique_suppr_propre)      #on le supprime
        print(f"La musique {musique_suppr_propre} a été supprimé")
    else:
        print("Musique inexistante")

def main():      #fonction programme principal qui appelle les autres fonctions
    while True:      #affiche le menu a l'infinie jusqu'a choix ==5
        choix = menu()     # on appelle la fonction menu(), et on stocke ce qu'elle renvoie dans la variable choix
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
            break      #sort de la bouble, fin du programme

main()