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