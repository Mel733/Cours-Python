longueur ={"m":1.0,"km":1000.0,"cm":0.01, "mm":0.001, "pouce":0.0254, "pied":0.3048 } #dictionnaire des longueurs, chaque unité a son facteur vers le mètre (unité de base)
poids = {"g": 1.0, "kg": 1000.0, "tonnes":1000000.0, "livres":453.59237, "once":28.3495 } #pareil mais poids (unité de base : gramme)
volume = {"L":1.0, "ml": 0.001, "m3":1000.0, "gallon": 3.78541} #pareil mais volume (unité de base : litre)
facteurs = {"longueur": longueur, "poids": poids, "volume": volume} #dictionnaire de dictionnaires, regroupe les 3 catégories (pas la température)
categories = ["longueur", "poids", "temperature", "volume"] #liste de catégories, même ordre que le menu

def menu(): #fonction pour afficher menu
    while True:  #lance le programme a l'infinie
        print("====CONVERTISSEUR D'UNITés")
        print("1.LONGUEUR (m, km, cm, mm, pouces, pieds)\n2.POIDS (g, kg, tonnes, livres, onces)\n3.TEMPERATURES (°C, °F, K)\n4.Volume (L, mL, m³, gallons)\n5.Quitter")
        try:
            choix =int(input("Que voulez vous faire ? ")) #demande le choix a l'user
            if 1<= choix <= 5: #si le choix est valide
                return choix #on le retourne
            else:
                print("Veuillez rentrer un choix valide") #sinon erreur
        except ValueError:
            print("Merci de rentrer un choix valide")  #erreur si lettre


def convertir(categorie, valeur, depart, arrivee): #fonction qui convertit une valeur d'une unité à une autre
    table = facteurs[categorie] #table = le dictionnaire de la catégorie (ex: longueur)
    valeur_base = valeur * table[depart] #valeur en unité de base (ex: km vers m)
    resultat = valeur_base / table[arrivee] #de l'unité de base vers l'unité d'arrivée

    return resultat #renvoie le résultat

def saisir_conversion(categorie): # fonction qui demande les infos à l'utilisateur et affiche la conversion
    table = facteurs[categorie] #table = le dictionnaire de la catégorie (ex: longueur)
    print("Unités :", list(table.keys())) #affiche les unités possibles

    while True: #boucle jusqu'à une unité de départ valide
        depart = input("Unité de départ : ")
        if depart in table: #l'unité existe dans le dictionnaire
            break #on sort de la boucle
        print("Unité inconnue") #sinon on redemande

    while True : #pareil pour l'unité d'arrivée
        arrive = input("Unité d'arrivé : ")
        if arrive in table :
            break
        print("Unité inconnue")

    while True: #boucle jusqu'à une valeur valide
        try:
            valeur = float(input("Valeur : ")) #on essaie de transformer en nombre
            break #si ça marche, on sort
        except ValueError: #si ce n'est pas un nombre
            print("Veuillez rentrer un nombre")

    resultat = convertir(categorie, valeur, depart, arrive) #appelle convertir pour faire le calcul
    print(f"{valeur} {depart}= {resultat:.2f} {arrive}") #affiche avec 2 chiffres après la virgule


def convertir_temperature(valeur, depart, arrivee): # fonction qui convertit une température d'une unité à une autre
    
    if depart == "°C": #étape 1 : on passe tout en Celsius (unité de base)
        celsius = valeur #déjà en Celsius
    elif depart == "°F":
        celsius = (valeur - 32) * 5 / 9 #formule °F vers °C
    elif depart == "K":
        celsius = valeur - 273.15 #formule K vers °C

    if arrivee == "°C": #étape 2 : on passe de Celsius vers l'unité d'arrivée
        return celsius #déjà en Celsius, on renvoie direct
    elif arrivee == "°F":
        return celsius * 9 / 5 + 32 #formule °C vers °F
    elif arrivee == "K":
        return celsius + 273.15 #formule °C vers K


def saisir_temperature(): # fonction qui demande les infos à l'utilisateur et affiche la conversion de température
    unite = ["°C", "°F", "K"] #liste des unités possibles (pas de dictionnaire ici)
    print("Unités :", unite) #affiche les unités possibles

    while True: #boucle jusqu'à une unité de départ valide
        depart = input("Unité de départ : ")
        if depart in unite: #l'unité est dans la liste
            break #on sort de la boucle
        print("Unité inconnue") #sinon on redemande

    while True : #pareil pour l'unité d'arrivée
        arrive = input("Unité d'arrivé : ")
        if arrive in unite :
            break
        print("Unité inconnue")

    while True: #boucle jusqu'à une valeur valide
        try:
            valeur = float(input("Valeur : ")) #on essaie de transformer en float
            break #si ça marche, on sort
        except ValueError: #si ce n'est pas un nombre
            print("Veuillez rentrer un nombre")

    resultat = convertir_temperature(valeur, depart, arrive) #appelle la fonction convertir_temperature pour faire le calcul
    print(f"{valeur} {depart} = {resultat:.2f} {arrive}") #affiche avec 2 chiffres après la virgule


def main(): # fonction pour programme principal, tourne jusqu'à ce que l'utilisateur quitte
    while True: #le menu revient après chaque conversion
        choix = menu() #affiche le menu et récupère le choix (1 à 5)
        if choix == 1 or choix == 2 or choix == 4: #longueur, poids ou volume
            nom = categories[choix - 1] #choix 1 donne categories[0] = "longueur", etc.
            saisir_conversion(nom) #lance la conversion avec le nom de la catégorie
        elif choix == 3: #la température est un cas spécial
            saisir_temperature() #fonction à part, car pas de dictionnaire
        elif choix == 5: #quitter
            print("Au revoir")
            break #on sort de la boucle, le programme s'arrête

main()