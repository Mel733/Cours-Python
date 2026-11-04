mots_interdits = ["spam", "arnaque", "piratage"] #liste mot interdits
message_accepter = [] #liste des messages accepter
message_interdit=[]#liste message refusé

def menu(): #fonction pour afficher le menu
    while True: #lance le programme a l'infinie
        print("=====MODERATEUR MESSAGE=====")
        print("1.Analyser un message\n2.Afficher les messages acceptés\n3.Afficher les messages refusés\n4.Quitter")
        try : #lance le bloc et si une erreur on saute au execpt
            choix = int(input("Que voulez vous faire ? ")) #demande a l'user de faire un choix int
            if 1<= choix <= 5: #si le choix est entre 1 et  5
                return choix #on retourn le choix + fin fonction
            else: #sinon
                print()
                print("Choix invalide") #choix invalide
        except ValueError:
            print()
            print("Merci de rentrer un chiffre") #si le input sont des lettres


def analyser_message(): #fonction pour analyser message
    message = input("Quel est votre message ? ") #demande a l'user son message
    print(f"Message : {message}") #l'affche
    message_clean = message.strip().lower() #le nettoie et l'affecte dans une nouvelle variable

    if message_clean == "": #si le message propre est vide
        print("Message vide") #message vide
        return #on return et fin fonction
    if message_clean in message_interdit or message_clean in message_accepter: #si le message est deja dans une des liste
        print("Message déjà présent dans une liste") #message qui l'indique
        return #return et fin fonction
    trouve = False #affect false a trouve
    mot_trouve = "" #mot touve est vide pour l'instant
    for mot in message_clean.split(): #on coupe le message pour vérifier chaque mots
        if mot in mots_interdits: #si un mot est dans la liste des mots interdit
            trouve = True #on passe trouve a true
            mot_trouve = mot #on affecte le mot dans mot trouve

    if trouve: #si touve est true
        message_interdit.append(message_clean) #on ajoute le message dans la liste des messages interdit
        print(f"Message refusé : mot interdit détecté - {mot_trouve}") #on l'affiche avec le mot interdit
    else:
        print("Message accepté") #sinon message accepté
        message_accepter.append(message_clean) #on l'ajoute dans la liste des message accepter


def afficher_liste_accepter(): #fonction pour afficher la liste des acdepté
    if not message_accepter : #si la liste est vide
        print("Liste Vide")
    else: 
        for numero, message in enumerate(message_accepter, start=1): #boucle for qui affiche cahque message de la liste et les numérote en commencant par 1
            print(f"{numero}. {message}")

def afficher_liste_refuser(): #meme chose mais pour l'autre liste
    if not message_interdit :
        print("Liste Vide")
    else: 
        for numero, message in enumerate(message_interdit, start=1):
                    print(f"{numero}. {message}")

def main(): #fonction qui lancera le programme
    while True: #lance le programme a l'infinie jusqu'a break
        choix = menu() #le choix du menu sera a affecter a menu quand on appelera la fonction menu
        print()
        if choix ==1: #si le choix est 1
            analyser_message() #on appelle la fonction analyser message
            print()
        elif choix == 2:
            afficher_liste_accepter() #meme chose different choix et fonction
            print()
        elif choix == 3:
            afficher_liste_refuser()
            print()
        elif choix == 4: #si choix est 4
            print("Au revoir")
            break #on arrete le programme

main()