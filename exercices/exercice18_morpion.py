import random   #import random pour plus tard

def affichage(): #fonction pour afficher
    print("==========PARTIE MORPION==========")
    print("=====USER VS IA=====")
    print("Vous jouez les X")

def affichage_grille(grille):  #fonction pour afficher les grille avec grilles comme parametre
    for g in grille: #pour chaque ligne dans grille
        print("------------") #séparateur de ligne
        print(" | ".join(str(number)for number in g)) #on assemble les trois numéro avec un | les séparent
        
        
def creer_grille(): #fonction pour créer une nouvelle grille neuve
    return [ #on return la liste qui contient trois liste
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def cases_libres(grille): #fonction pour chercher les cases libres et renvoie leur position(ligne et colonne)

    libres = []   # liste vide ou se trouve les positions libres

    for i in range(3):        # i = numéro de ligne : 0, 1, 2
        for j in range(3):    # j = numéro de colonne : 0, 1, 2
            case = grille[i][j]   # contenu de la case à la ligne i, colonne j

            if isinstance(case, int):   # si la case qui est un nombre, est toujours libre ?
                                        # ("X" ou "O" = case déjà jouée car c'est une chaine)
                libres.append((i, j))   # on ajoute la position à la liste

    return libres   # après avoir tout parcouru, on renvoie la liste des cases libres



def coup_valide(grille, choix): #fonction pour savoir si un coup est valide avec choix et grille comme parametre
    if choix < 1 or choix > 9: #si le choix est inférieur a 1 ou superieur a 9
        return False #on return false
    n = choix - 1 #sinon on fait choix -1 car index liste commence a 0
    ligne = n //3   #on calcule l'emplacement de la ligne
    colonne = n%3    #pareil mais pour colonne
    return isinstance(grille[ligne][colonne], int) #on return True si la case est un int (case libre), False si elle est déjà prise

def jouer_coup_user(grille, choix, symbole): #fonction pour le user qui joue son coup avec grille, choix, symbole comme parametre
   n= choix -1 #meme chose
   ligne = n //3
   colonne = n%3
   grille [ligne] [colonne] = symbole #on remplacera l'emplacement par le symbole
    
def a_gagner(grille, symbole): #fonction qui regarde si le symbole a gagné, elle renvoie True ou False
     combinaisons= [ #une liste combinaison et chacune d'elle est une liste
     [(0,0), (0,1), (0,2)], #leur positions sur la grille (ligne, colonne)
     [(1,0), (1,1), (1,2)],
     [(2,0), (2,1), (2,2)],

     [(0,0), (1,1), (2,2)],
     [(0,0), (1,0), (2,0)],
     [(0,1), (1,1), (2,1)],
     [(0,2), (1,2), (2,2)],
     [(0,2), (1,1), (2,0)],
    ]
     for combi in combinaisons : #pour une combinaisons dans la liste
        case1 = grille[combi[0][0]][combi[0][1]] #contenu de la 1ere case de la combinaison
        case2 = grille[combi[1][0]][combi[1][1]] #contenu de la 2eme case
        case3 = grille[combi[2][0]][combi[2][1]] #contenu de la 3eme case
        if case1 ==symbole and case2==symbole and case3 ==symbole: #si les 3 cases ont le symbole
            return True #c'est gagné, on s'arrête
     return False #si aucune combinaison n'est complète, c'est perdu


def demander_coup(grille):#fonction pour demander le coup a l'user 
    while True: #on répète à l'infini jusqu'à ce que le coup soit valide (le return fait sortir de la boucle)
        try : #essaye
            print() #ligne vide pour aérer l'affichage
            choix = int(input("Votre tour X. Case : ")) #demande la case
            if coup_valide(grille, choix): #si le coup est valide
                return choix #on return son choix
            else:
                print("Case invalide, veuillez en choisir une autre") #sinon case invalide
        except ValueError: #error si c'est pas un chiffre
            print("Merci de rentrer un chiffre valide")

def grille_pleine(grille): #fonction pour voir si la grille est pleine
       if not cases_libres(grille): #si il n'y a plus aucune case libre (la liste est vide)
           return True #on return true, la grille est pleine
       else:
           return False #sinon false, il reste des cases libres


def coup_gagnant(grille, symbole): #fonction qui cherche une case où le symbole gagnerait, sert à l'ia pour gagner et pour bloquer le joueur
    for (i, j) in cases_libres(grille): #pour chaque case libre (i = ligne, j = colonne)
        ancienne = grille[i][j] #on garde le nombre d'origine pour pouvoir le remettre
        grille[i][j]  = symbole #on pose le symbole pour essayer
        if a_gagner(grille, symbole): #si ça fait gagner le symbole
            grille[i][j] = ancienne #on remet la case comme avant
            return (i, j) #on renvoie la position qui fait gagner
        grille[i][j] = ancienne #sinon on remet la case comme avant et on passe à la suivante
    return None #aucune case ne fait gagner, on renvoie rien
    


def coup_ia(grille, ia, joueur): #fonction qui choisit où l'ia joue, elle renvoie une position (ligne, colonne) mais elle place rien
    # Règle 1 : si je peux gagner, je joue ce coup
    position = coup_gagnant(grille, ia) #on regarde si l'ia peut gagner en appelant sa fonction coup gagnant
    if position is not None: #si on a trouvé une case
        return position #on joue cette case et on s'arrête

    # Règle 2 : si l'adversaire peut gagner, je le bloque
    position = coup_gagnant(grille, joueur) #on regarde si le joueur peut gagner toujour en appelant sa fonction
    if position is not None:
        return position #on prend sa case pour le bloquer

    libres = cases_libres(grille) #liste des cases libres

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

def jouer_partie(): #fonction pour jouer la partie
    affichage() #appele la fonction pour l'affichage
    grille = creer_grille() #la variable grille reçoit le return de la fonction creer_grille(une nouvelle grille)
    affichage_grille(grille) #appelle la fonction affichage grille avec comme argument grille

    while True: #boucle infinie, tant qu'il reste des cases libres et que aucun joueur ne gagne (on en sort avec un return)
        # --- tour du joueur ---
        numero = demander_coup(grille) #la variable numero sera affecter au choix retourné par la fonction demander coup
        jouer_coup_user(grille, numero, "X") #appel la fonction pour jouer le coup de l'user avec les arguments grille, numero et "X"
        affichage_grille(grille) #on afficher la grille avec le X
        if a_gagner(grille, "X"): #si X gagne
            return "X" #on return X et fin de partie
        if grille_pleine(grille): #si la grille est pleine
            return "egalite" #egalite et fin de partie

        # --- tour de l'IA ---
        i, j = coup_ia(grille, "O", "X") #coup_ia retourne un tuple (ligne, colonne), on le met dans i et j
        grille[i][j] = "O" #on place le O à cette position
        print()
        print("L'IA joue en case", i * 3 + j + 1, "(O)") #i * 3 + j + 1 convertit la position en numéro de 1 à 9
        print()
        affichage_grille(grille) #on affiche la grille avec le coup de l'IA
        if a_gagner(grille, "O"): #si O gagne
            return "O" #on return O et fin de partie

scores = {"victoires": 0, "defaites": 0, "egalites": 0} #dictionnaire avec les score a 0, créé une seule fois avant la boucle pour garder les scores entre les parties

while True: #boucle infinie, on rejoue tant que l'user en sort avec le break
    resultat = jouer_partie() #la variable resultat sera affecter avec le return de jouer partie

    if resultat == "X": #si le resultat est X
        scores["victoires"] += 1 #plus une victoire
    elif resultat =="O": #si c'est O (la lettre)
        scores["defaites"] +=1  #plus une defaite
    else:
        scores["egalites"]+=1  #sinon plus une egalité

    print("Victoires :", scores["victoires"]) #on affiche les scores a la fin de chaque partie
    print("Défaites :", scores["defaites"])
    print("Égalités :", scores["egalites"])

    rejouer = input("Rejouer ? (o/n) : ") #la variable rejouer contient un input pour savoir si on veux rejouer
    if rejouer != "o": #si c'est tout sauf o
        break #on sort de la boucle while, le programme s'arrete