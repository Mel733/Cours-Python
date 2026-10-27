
nom_ecole = "Digital Campus"#Variable école avec comme valeur son nom
annee_scolaire = 2026 #variable année avec l'anné comme valeur

matieres = ("Python", "HTML", "CSS", "JavaScript") #Un tuple avec les matiere

etudiants = [ #une liste d'étudiant, chaque étudiant est sous forme de dictionnaire clé-valeurs
    {
        "nom": "Martin",
        "prenom": "Lucas",
        "age": 20,
        "notes": [15, 12, 17, 14] #plusieur valeurs sous forme de liste dans la clé note
    },
    {
        "nom": "Dupont",
        "prenom": "Emma",
        "age": 22,
        "notes": [18, 16, 19, 17] #pareil
    },
    {
        "nom": "Bernard",
        "prenom": "Hugo",
        "age": 19,
        "notes": [8, 11, 9, 12] #pareil
    }
]


def afficher_menu(): #fonction pour afficher le menu

    print("\n================================")
    print("GESTION DES ETUDIANTS")
    print(nom_ecole, "-", annee_scolaire) #affiche le nom de l'école et l'année scolaire affecter au début
    print("================================")

    print("1. Afficher les étudiants")
    print("2. Ajouter un étudiant")
    print("3. Rechercher un étudiant")
    print("4. Ajouter une note")
    print("5. Afficher les moyennes")
    print("6. Afficher les étudiants admis")
    print("7. Afficher les statistiques")
    print("8. Supprimer un étudiant")
    print("9. Afficher les matières")
    print("0. Quitter")

    print("================================")


def afficher_etudiants(): #fonction pour afficher un etudiant

    if len(etudiants) == 0:  #si la liste d'étudiant est de 0
        print("Aucun étudiant enregistré.") #message
        return #renvoie une valeur non et n'execute pas le reste de la fonction

    print("\nLISTE DES ETUDIANTS") #Sinon

    compteur = 1 #le compteur commence a 1

    for etudiant in etudiants: #pour chaque tour il regarde les etudiant un par un dans la liste

        print("\nEtudiant numéro", compteur) #affiche le numéro avec le compteur a 1

        print("Nom :", etudiant["nom"]) #affiche le prénom
        print("Prénom :", etudiant["prenom"]) # affiche le nom
        print("Age :", etudiant["age"]) #affiche l'age
        print("Notes :", etudiant["notes"]) #affiche les notes

        compteur = compteur + 1 #le compteur augmente de 1 a chaque tour pour ensuite afficher les infos d'un autre étudiant


def ajouter_etudiant(): #focntion ajouter un étudiant

    print("\nAJOUT D'UN ETUDIANT")

    nom = input("Nom : ").strip() #demande le nom a l'user et efface les espaces inutiles
    prenom = input("Prénom : ").strip() #pareil pour le prenom

    if nom == "" or prenom == "": #si les valeur de nom et prenom sont vide
        print("Le nom et le prénom sont obligatoires.") #le message s'affiche
        return #renvoie une valeur non et n'execute pas le reste de la fonction

    try: # tente d'exécuter ce bloc ; si une exception survient, on passe au except
        age = int(input("Age : ")) #demande l'age qui sera de type int(chiffre entier) a l'user
    except ValueError: #si la saisie contient des lettres ou autres
        print("L'âge doit être un nombre entier.") #Ce message apparait
        return

    if age <= 0: #Si l'age est inférieur a 0
        print("Age incorrect.") #Ce message apparait
        return

    nouvel_etudiant = { #Construit la bibliothèque du nouvel étudiant, les notes sont vide pour le moment
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "notes": []
    }

    etudiants.append(nouvel_etudiant)  #ajoute cette bibliotheque dans la liste etudiants

    print("Etudiant ajouté avec succès !") #message de réussite


def rechercher_etudiant(): #fonction pour rechercher un étudiant

    recherche = input("Nom à rechercher : ").strip().lower() #demande a l'user de rentrer un nom qui sera en miniscule et dont les espaces seront supprimer

    resultats = [] #la liste résultat est vide, 

    for etudiant in etudiants: #la boucle verifie chaque etudiant un par un dans etudiants

        if recherche in etudiant["nom"].lower(): #si l'étudiant recherché est égale a un nom 

            resultats.append(etudiant) #ajoute l'édutiant dans resultat

    if len(resultats) == 0: #si la liste de résultat est de 0

        print("Aucun étudiant trouvé.") #message 

    else:

        print("\nRésultats de la recherche :") #sinon les résultat s'affiche

        for etudiant in resultats: #boucle pour afficher les étudiant rechercher dans résultat

            print( #affciher leur biblothèque
                etudiant["prenom"],
                etudiant["nom"],
                "-",
                etudiant["age"],
                "ans"
            )


def ajouter_note(): #fonction ajouter note

    nom = input("Nom de l'étudiant : ").strip().lower() #ajouter le nom de l'édutiant nettoyer des espaces et en minuscules

    trouve = False #reste false si l'étudiant n'est pas trouvé

    for etudiant in etudiants: #boucle pour vérifier chaque etudiant de la liste

        if etudiant["nom"].lower() == nom: #si le nom taper correspond a un etudiant(en minuscule) dans la liste

            trouve = True #trouve devien true

            try: #tente d'exécuter ce bloc ; si une exception survient, on passe au except
                note = float(input("Nouvelle note /20 : ")) #le user doit taper une note
            except ValueError:
                print("La note doit être un nombre.") #erreur si le input saisie sont des lettres
                return

            if note >= 0 and note <= 20: #si la note est égale ou supérieur a 0 ou inférieur ou égal a 0

                etudiant["notes"].append(note) #alors on ajoute la note dans la clé valeur de l'étudiant concerner

                print("Note ajoutée !")

            else:

                print("La note doit être entre 0 et 20.") #sinon message d'erreur

            break #fin de la fonnction

    if trouve == False: #si l'étudiant n'est pas trouvé dans la liste

        print("Etudiant introuvable.")


def calculer_moyenne(notes): #fonction calculer moyenne avec notes comme parametres

    if len(notes) == 0: #si le nombre de notes est égale a 0
        return 0 #on retourne 0

    total = 0 #le total est de 0 au commencement

    for note in notes: #boucle pour prendre chaque valeur de note d'un étudiant

        total = total + note #a chaque tour le total est additionné d'une note

    moyenne = total / len(notes) #calcule la moyenne

    return moyenne #retourne la valeur de la moyenne


def afficher_moyennes(): #fonction afficher moyenne

    print("\nMOYENNES DES ETUDIANTS")

    for etudiant in etudiants: #boucle pour chaque étudiant un a un

        moyenne = calculer_moyenne(etudiant["notes"])#calculer la moyenne en appelant la fonction au dessus et selon les note de l'étudiant en question

        print( #affichage pour chaque étudiant
            etudiant["prenom"],
            etudiant["nom"],
            ":",
            round(moyenne, 2), #arondi le resultat a deux chiffre apres la virgule
            "/20"
        )


def afficher_admis(): #fonction pour afficher admis ou non

    print("\nRESULTATS DES ETUDIANTS")

    for etudiant in etudiants: #pour chaque etudiant de la liste

        notes = etudiant["notes"] #regarde leur notes

        if len(notes) == 0: #si il n'on aucune note

            resultat = "Non évalué"

        else: #sinon

            moyenne = calculer_moyenne(notes) #appelle de la fonction calculer moyenne avec leur notes en paramtere

            if moyenne >= 16: #si la moyenne est supérieur ou égale a 16

                resultat = "Admis - Félicitations"

            elif moyenne >= 12: #si la moyenne est supérieur ou égale a 12

                resultat = "Admis - Bien"

            elif moyenne >= 10: #si la moyenne est supérieur ou égale a 10

                resultat = "Admis"

            else:  #sinon

                resultat = "Non admis"

        print( #affichage pour chaque étudiant
            etudiant["prenom"],
            etudiant["nom"],
            ":",
            resultat
        )


def afficher_statistiques(): #focntion pour afficher des statistiques

    print("\nSTATISTIQUES")

    nombre_etudiants = len(etudiants) #la valeur nombre etudiant est rempli selon le nombre d'étudiant dans la liste

    if nombre_etudiants == 0: #si il n'y a pas d'étudiant

        print("Aucune donnée disponible.")
        return #retourne rien et fin fonction

    total_moyennes = 0 #iniatilise tout a 0
    nombre_evalues = 0
    nombre_admis = 0
    nombre_refuses = 0

    meilleure_moyenne = -1 #valeur a -1
    meilleur_etudiant = "" #chaine de caractere vide pour le moment

    for etudiant in etudiants: #pour chaque etudiant de la liste

        if len(etudiant["notes"]) == 0: #si l'étudiant n'a pas de note
            continue #on laisse cette étudiant et on passe au suivant de la liste

        moyenne = calculer_moyenne(etudiant["notes"]) #calcule la moyenne de chaque étudinat selon ces notes

        total_moyennes = total_moyennes + moyenne #les moyenne de chaque étudiant s'ajoute au total a chaque tour
        nombre_evalues = nombre_evalues + 1 #ajoute un a chaque étudiant évaluer

        if moyenne >= 10: #si la moyenne est au dessu ou égale a 10

            nombre_admis = nombre_admis + 1 #no rajoute un étudiant admis

        else:

            nombre_refuses = nombre_refuses + 1 #sinon on ajoute un étudiant refuser

        if moyenne > meilleure_moyenne: #si la moyenne est au supérieur de la meilleur moyenne

            meilleure_moyenne = moyenne #alors sa valeur est affecter a meilleur moyenne(sa valeur peut changer au fil de la bouble car certain étudiant on une meilleur moyenne que les précedents)

            meilleur_etudiant = (
                etudiant["prenom"] + " " + etudiant["nom"] #le meilleur étudiant sera affecter a la variable meilleur étudiant
            )

    print("Nombre d'étudiants :", nombre_etudiants) #affiche le nombre de chaque variable
    print("Etudiants évalués :", nombre_evalues)
    print("Etudiants admis :", nombre_admis)
    print("Etudiants refusés :", nombre_refuses)

    if nombre_evalues > 0: #si le nombre d'évaluer est au dessus de 0

        moyenne_classe = total_moyennes / nombre_evalues #calsuler la moyenne de la classe selon le total et le nombre d'étudiant évaluer

        taux_reussite = nombre_admis / nombre_evalues * 100 #calcule pour le taux de réussite

        print("Moyenne de classe :", round(moyenne_classe, 2)) #affiche les résultat et arrondi 
        print("Taux de réussite :", round(taux_reussite, 2), "%")
        print("Meilleur étudiant :", meilleur_etudiant)
        print("Meilleure moyenne :", round(meilleure_moyenne, 2))

    else: #sinon ce message apparait

        print("Aucun étudiant évalué.")


def supprimer_etudiant(): #fonction pour supprimer un étudiant

    nom = input("Nom à supprimer : ").strip().lower() #demande a l'user qui il veut supprimer

    for etudiant in etudiants: #bouble pour chaque étudiant dans la liste

        if etudiant["nom"].lower() == nom: #si le nom saisi correspont a un nom dans la liste

            confirmation = input( #message de confirmation
                "Confirmer la suppression ? (oui/non) : "
            )

            if confirmation.lower() == "oui": #si oui(en minuscule)

                etudiants.remove(etudiant) #l'étudiant est supprimer de la liste

                print("Etudiant supprimé.") #message  de réussite

            else: #sinon 

                print("Suppression annulée.")

            return #fin de la fonction

    print("Etudiant introuvable.") #message si l'étudiant est introuvable


def afficher_matieres(): #fonction pour afficher les matières

    print("\nMATIERES ENSEIGNEES")

    for numero in range(len(matieres)): #renvoie un numéro pour chaque matiere dans la liste(le numéro commence a zéro car l'index commence a 0)

        print(numero + 1, "-", matieres[numero]) #afficher en mettant un +1 a chaque tour pour les autres matieres

    print("\nNombre de matières :", len(matieres)) #affiche le nombre total de matieres


def programme_principal(): #fonction pour le programme principal regroupant toute les fonctions

    continuer = True #donne une valeur booélen a continuer

    while continuer: #similaire a while True, le programme s'affiche a l'infini jusqua la fin

        afficher_menu() #appelle la fonction qui affiche le menu

        choix = input("\nVotre choix : ") #demande le choix

        if choix == "1": #si le choix est de 1

            afficher_etudiants() #appelle la fonction pour afficher les étudiants

        elif choix == "2": #si c'est 2

            ajouter_etudiant() #appelle la fonction ajouter un étudiant

        elif choix == "3": #si c'est 3

            rechercher_etudiant() #appelle la fonction pour rechercher un étudiant

        elif choix == "4": #si c'est 4

            ajouter_note() #appelle la fonction ajoute une note

        elif choix == "5": #si c'est 5

            afficher_moyennes() #appelle la fonction afficher les moyennes

        elif choix == "6": #si 6

            afficher_admis() #appellle la fonction pour afficher les admis

        elif choix == "7": #si 7

            afficher_statistiques() #appelle la fonction pour afficher les statistique

        elif choix == "8": #si 8

            supprimer_etudiant() #appelle la fonction supprimer un étudiant

        elif choix == "9": #si 9

            afficher_matieres() #appelle la fonction afficher les matieres

        elif choix == "0": #et si 0

            print("Fermeture du programme...") #message
            continuer = False #fin du programme

        else: #sinon choix incorrect

            print("Choix incorrect. Réessayez.")


programme_principal() #lance le programme principale en appelant sa fonction