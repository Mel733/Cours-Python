#on importe les class dans leur fichiers respctif et le module random
from gandalf import Gandalf
from roi_mort_angmar import RoiMort
import random
class CombatManager:     #on crée la classe CombatManager
    def __init__(self):   #constructeur
        self.gandalf = Gandalf()  #on crée l'objet gandalf (instance) à partir de sa classe, stocké en attribut
        self.roimort=RoiMort()    #pareil mais pour roimort
        self.tour = 1    #on initialise le tour à 1

    def choix_attaque(self):   #methode pour choisir une attaque
          print("\n Choissisez une des trois attaques :")
          for numero, attaque in enumerate(self.gandalf.attaques, start=1):   # enumerate renvoie (numéro, attaque) à chaque tour, numérotation à partir de 1
               print(f"{numero}. {attaque["nom"]} (dégats: {attaque["dégats"]}, Esquive : {attaque["esquive"]*100}%)")
               #on affiche aussi à chaque tour les stats de l'attaque
               print()
               
          while True:   #boucle infinie, elle s'arrête uniquement grâce au return
               choix = input("Entrez le numéro de l'attaque(1,2 ou 3) : ")   #input renvoie une chaîne (str) : le choix de l'utilisateur
               print()
               if choix in ("1","2", "3"):   #si le choix est dans le tuple
                    return int(choix) -1   #on convertit le choix en int et on fait -1 pour coordonner avec les index des attaques
               print("Choix invalide. Veuillez entrer 1, 2 ou 3")   #sinon message d'erreur, et la boucle recommence

    def afficher_etat(self):   #méthode pour afficher l'état à chaque fin de tour
         for personnage in (self.gandalf, self.roimort):   #on parcourt le tuple contenant les deux objets
              print(f"{personnage.nom}: "   #on affiche leur nom
                    f"{personnage.points_de_vie:.2f}  PV / {personnage.points_de_vie_max} PV"   #PV actuels (2 décimales) / PV max
                    f" {personnage.xp} XP | {personnage.coef_puissance():.2f} puissance")   #leur xp et leur coef de puissance (2 décimales)
        
    def start(self):   #methode pour lancer le combat
        print("======GANDALF VS ROI MORT D'ANGMAR===========")
        for personnage in (self.gandalf, self.roimort):   #on parcourt le tuple contenant les deux objets
            print(personnage.presentation())   #on appelle la méthode presentation de chaque personnage
            print("Ses attaques :"+", ".join(a["nom"] for a in personnage.attaques))   #on assemble les noms des attaques en une chaîne séparée par ", " (join)
            print()

        print("Vous êtes Gandalf, que le combat commence !")   #petit rappel du personnage que on incarne

        while self.gandalf.est_vivant() and self.roimort.est_vivant():   #tant que gandalf ET roimort sont tous les deux vivants
                  print(f"\n----Tour n{self.tour}----")   #on affiche le numero du tour
                  choix = self.choix_attaque()   #on appelle la méthode pour choisir l'attaque
                  print(self.gandalf.attaquer(self.roimort, choix))   #on affiche le message renvoyé par attaquer() : gandalf attaque le roimort avec l'attaque d'index choix
                  if not self.roimort.est_vivant(): #  si le roi mort n'est plus vivant
                       break   #on sort de la boucle

                  choix_roi = random.randrange(len(self.roimort.attaques))   #choix aléatoire d'un index : randrange tire un entier entre 0 et len(liste)-1
                  print(f"Le roi Mort choisi l'attaque : {self.roimort.attaques[choix_roi]["nom"]}")   #affiche le choix avec le nom de l'attaque
                  print(self.roimort.attaquer(self.gandalf, choix_roi))   #on affiche le message renvoyé : le roi mort attaque gandalf avec l'attaque d'index choix_roi
                  self.afficher_etat()   #on affiche l'état de chaque personnage à la fin du tour
                  self.tour +=1   #on incrémente de 1 le numéro du tour
        print()
        print("=====FIN DU COMBAT=====")   #fin du combat
        self.afficher_etat()   #affiche l'état des personnages
        vainqueur = self.gandalf if self.gandalf.est_vivant() else self.roimort   #expression conditionnelle : gandalf s'il est vivant, sinon le roi mort
        print (f"Le grand vainqueur est : {vainqueur.nom} avec {vainqueur.points_de_vie:.2f} PV et {vainqueur.xp} XP ")   #affiche le vainqueur avec ses attributs (nom, PV, XP)
                  
                  
        
        

        


