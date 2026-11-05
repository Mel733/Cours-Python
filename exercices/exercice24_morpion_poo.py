import random

class User:  #créer classe User
    def __init__(self, symbole): #constructeur de l'objet user qui aura un symbole
        self.symbole = symbole #le self designe l'objet

    def demander_coup(self, grille): #methode pour demander coup, grille = objet Grille
        while True: #boucle infinie, on en sort avec le return
            try: #essaye le bloc ci dessous et passe au except si erreur
                print()
                choix = int(input(f"Votre tour {self.symbole}. Case : ")) #input demande la case, int() la transforme en entier

                # On appelle la méthode coup_valide de l'objet Grille
                if grille.coup_valide(choix): #si le coup est valide
                    return choix #on return le choix
                else:
                    print("Case invalide, veuillez en choisir une autre") #sinon on affiche que la case est invalide

            except ValueError: #erreur si int() ne peut pas convertir (lettres dans input)
                print("Merci de rentrer un chiffre valide")

    def jouer_coup_user(self, grille, choix): #methode pour le coup de l'user avec grille et choix comme parametre
        n = choix - 1 #choix -1 car élément d'une liste commence a 0
        ligne = n // 3 #calcule position ligne (division entière)
        colonne = n % 3 #pareil mais pour colonne (reste de la division)

        # On accède à la liste dans l'objet Grille
        grille.grille[ligne][colonne] = self.symbole #on remplace le nombre par le symbole






class Ia(User): #creer classe IA qui herite de la classe User
   def __init__(self, symbole): #constructeur de l'objet ia qui aura un symbole
       super().__init__(symbole) #super() appelle le constructeur de User, il range le symbole

   def coup_ia(self, grille, joueur): #methode pour coup ia, joueur = symbole de l'adversaire
    # Règle 1 : si je peux gagner, je joue ce coup
    position = self.coup_gagnant(grille, self.symbole) #on regarde si l'ia peut gagner en appelant la méthode coup gagnant dans la class IA
    if position is not None: #si on a trouvé une case
        return position #on joue cette case et on s'arrête (position = tuple (ligne, colonne))

    # Règle 2 : si l'adversaire peut gagner, je le bloque
    position = self.coup_gagnant(grille, joueur) #on regarde si le joueur peut gagner toujour en appelant sa methode
    if position is not None:
        return position #on prend sa case pour le bloquer

    libres = grille.cases_libres() #liste des cases libres

    # Règle 3a : le centre s'il est libre
    if (1, 1) in libres: #favorisera le centre
        return (1, 1)

    # Règle 3b : un coin libre, choisi au hasard
    coins_libres = [] #liste vide pour les coins libres
    for coin in [(0, 0), (0, 2), (2, 0), (2, 2)]: #pour chaque coin
        if coin in libres: #si le coin est libre
            coins_libres.append(coin) #on l'ajoute à la liste
    if coins_libres: #si il y a au moins un coin libre
        return random.choice(coins_libres) #on en prend un au hasard

    # Sinon : la première case libre (il ne reste que des côtés)
    return libres[0]
   
   def coup_gagnant(self,grille, symbole): #fonction qui cherche une case où le symbole gagnerait, sert à l'ia pour gagner et pour bloquer le joueur
    for (i, j) in grille.cases_libres(): #pour chaque case libre (i = ligne, j = colonne)
        ancienne = grille.grille[i][j] #on garde le nombre d'origine pour pouvoir le remettre
        grille.grille[i][j]  = symbole #on pose le symbole pour essayer
        if grille.a_gagner(symbole): #si ça fait gagner le symbole
            grille.grille[i][j] = ancienne #on remet la case comme avant
            return (i, j) #on renvoie la position qui fait gagner
        grille.grille[i][j] = ancienne #sinon on remet la case comme avant et on passe à la suivante
    return None #aucune case ne fait gagner, on renvoie rien
    


class Grille: #classe grille
 def __init__(self): #constructeur, crée la grille
        self.grille = [ #liste 2D : 3 lignes de 3 cases
            [1, 2, 3], #chaque case contient son numéro (int) tant qu'elle est libre
            [4, 5, 6],
            [7, 8, 9]
        ]

 def grille_pleine(self): #fonction pour voir si la grille est pleine
       if not self.cases_libres(): #si il n'y a plus aucune case libre (la liste est vide)
           return True #on return true, la grille est pleine
       else:
           return False #sinon false, il reste des cases libres
       
 def affichage_grille(self):  #fonction pour afficher la grille
    for g in self.grille: #pour chaque ligne dans grille
        print("------------") #séparateur de ligne
        print(" | ".join(str(number)for number in g)) #str() car les cases peuvent être des int, join assemble les trois cases avec un | qui les sépare


 def cases_libres(self): #fonction pour chercher les cases libres et renvoie leur position(ligne et colonne)

    libres = []   # liste vide ou se trouve les positions libres

    for i in range(3):        # i = numéro de ligne : 0, 1, 2
        for j in range(3):    # j = numéro de colonne : 0, 1, 2
            case = self.grille[i][j]   # contenu de la case à la ligne i, colonne j

            if isinstance(case, int):   # si la case qui est un nombre, est toujours libre ?
                                        # ("X" ou "O" = case déjà jouée car c'est une chaine)
                libres.append((i, j))   # on ajoute la position à la liste

    return libres   # après avoir tout parcouru, on renvoie la liste des cases libres

 def coup_valide(self, choix): #fonction qui vérifie si le choix (1 à 9) est jouable, renvoie True ou False
    if choix < 1 or choix > 9: #si hors de la grille
        return False #coup invalide

    n = choix - 1 #-1 car les listes commencent à 0
    ligne = n // 3 #position ligne
    colonne = n % 3 #position colonne

    return isinstance(self.grille[ligne][colonne], int) #True si la case est encore un nombre (donc libre)

 def a_gagner(self, symbole): #fonction qui regarde si le symbole a gagné, elle renvoie True ou False
     combinaisons= [ #une liste combinaison et chacune d'elle est une liste
     [(0,0), (0,1), (0,2)], #leur positions sur la grille (ligne, colonne) / ligne 1
     [(1,0), (1,1), (1,2)], #ligne 2
     [(2,0), (2,1), (2,2)], #ligne 3

     [(0,0), (1,1), (2,2)], #diagonale
     [(0,0), (1,0), (2,0)], #colonne 1
     [(0,1), (1,1), (2,1)], #colonne 2
     [(0,2), (1,2), (2,2)], #colonne 3
     [(0,2), (1,1), (2,0)], #diagonale
    ]
     for combi in combinaisons : #pour une combinaisons dans la liste
        case1 = self.grille[combi[0][0]][combi[0][1]] #contenu de la 1ere case de la combinaison
        case2 = self.grille[combi[1][0]][combi[1][1]] #contenu de la 2eme case
        case3 = self.grille[combi[2][0]][combi[2][1]] #contenu de la 3eme case
        if case1 ==symbole and case2==symbole and case3 ==symbole: #si les 3 cases ont le symbole
            return True #c'est gagné, on s'arrête
     return False #si aucune combinaison n'est complète, ce symbole n'a pas gagné








class PartieManager: #classe qui gère la partie
   def __init__(self): #constructeur
       self.grille = Grille() #objet Grille
       self.user = User("X") #objet user le joueur joue X
       self.ia = Ia("O") #objet ia l'ia joue O

   def affichage(self): #fonction pour afficher le titre de la partie
    print("==========PARTIE MORPION==========")
    print("=====USER VS IA=====")
    print("Vous jouez les X")       

   def jouer_partie(self): #fonction pour jouer la partie, renvoie "X", "O" ou "egalite"
    self.grille = Grille() #nouvelle grille à chaque partie (sinon l'ancienne reste remplie)
    self.affichage() #appele la fonction pour l'affichage
     
    self.grille.affichage_grille() #appelle la fonction affichage grille (sans argument)

    while True: #boucle infinie, tant qu'il reste des cases libres et que aucun joueur ne gagne (on en sort avec un return)
        # --- tour du joueur ---
        numero = self.user.demander_coup(self.grille) #la variable numero sera affecter au choix retourné par la fonction demander coup
        self.user.jouer_coup_user(self.grille, numero) #appel la fonction pour jouer le coup de l'user avec les arguments grille et numero (le symbole est dans self)
        self.grille.affichage_grille() #on afficher la grille avec le X
        if self.grille.a_gagner(self.user.symbole): #si X gagne
            return "X" #on return X et fin de partie
        if self.grille.grille_pleine(): #si la grille est pleine
            return "egalite" #egalite et fin de partie

        # --- tour de l'IA ---
        i, j = self.ia.coup_ia(self.grille, self.user.symbole) #coup_ia retourne un tuple (ligne, colonne), on le met dans i et j
        self.grille.grille[i][j] = "O" #on place le O à cette position
        print()
        print("L'IA joue en case", i * 3 + j + 1, "(O)") #i * 3 + j + 1 convertit la position en numéro de 1 à 9
        print()
        self.grille.affichage_grille() #on affiche la grille avec le coup de l'IA
        if self.grille.a_gagner(self.ia.symbole): #si O gagne
            return "O" #on return O et fin de partie





maPartie = PartieManager() #on crée l'objet qui gère la partie

scores = {"victoires": 0, "defaites": 0, "egalites": 0} #dictionnaire avec les score a 0, créé une seule fois avant la boucle pour garder les scores entre les parties

while True: #boucle infinie, on rejoue tant que l'user en sort avec le break
    resultat = maPartie.jouer_partie() #la variable resultat sera affecter avec le return de jouer partie

    if resultat == "X": #si le resultat est X
        scores["victoires"] += 1 #plus une victoire
    elif resultat =="O": #si c'est O (la lettre)
        scores["defaites"] +=1  #plus une defaite
    else:
        scores["egalites"]+=1  #sinon plus une egalité

    print("Victoires :", scores["victoires"]) #on affiche les scores a la fin de chaque partie
    print("Défaites :", scores["defaites"])
    print("Égalités :", scores["egalites"])

    rejouer = input("Rejouer ? (o/n) : ").lower() #la variable rejouer contient un input pour savoir si on veux rejouer
    if rejouer != "o": #si c'est tout sauf o
        break #on sort de la boucle while, le programme s'arrete