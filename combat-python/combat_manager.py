
from gandalf import Gandalf
from roi_mort_angmar import RoiMort
import random
class CombatManager:
    def __init__(self):
        self.gandalf = Gandalf()
        self.roimort=RoiMort()
        self.tour = 1

    def choix_attaque(self):
          print("\n Choissisez une des trois attaques :")
          for numero, attaque in enumerate(self.gandalf.attaques, start=1):
               print(f"{numero}. {attaque["nom"]} (dégats: {attaque["dégats"]}, Esquive : {attaque["esquive"]*100}%)")
               print()
               
          while True:
               choix = input("Entrez le numéro de l'attaque(1,2 ou 3) : ")
               print()
               if choix in ("1","2", "3"):
                    return int(choix) -1
               print("Choix invalide. Veuillez entrer 1, 2 ou 3")

    def afficher_etat(self):
         for personnage in (self.gandalf, self.roimort):
              print(f"{personnage.nom}:"
                    f"{personnage.points_de_vie:.2f} PV / {personnage.points_de_vie_max} PV"
                    f" {personnage.xp} XP | {personnage.coef_puissance():.2f} puissance")
        
    def start(self):
        print("======GANDALF VS ROI MORT D'ANGMAR===========")
        for personnage in (self.gandalf, self.roimort):
            print(personnage.presentation())
            print("Ses attaques :"+", ".join(a["nom"] for a in personnage.attaques))
            print()

        print("Vous êtes Gandalf, que le combat commence !")

        while self.gandalf.est_vivant() and self.roimort.est_vivant():
                  print(f"\n----Tour n{self.tour}----")
                  choix = self.choix_attaque()
                  print(self.gandalf.attaquer(self.roimort, choix))
                  if not self.roimort.est_vivant():
                       break

                  choix_roi = random.randrange(len(self.roimort.attaques))
                  print(f"Le roi Mort choisi l'attaque : {self.roimort.attaques[choix_roi]["nom"]}")
                  print(self.roimort.attaquer(self.gandalf, choix_roi))
                  self.afficher_etat()
                  self.tour +=1

        print("=====FIN DU COMBAT=====")
        self.afficher_etat()
        vainqueur = self.gandalf if self.gandalf.est_vivant() else self.roimort
        print (f"Le grand vainqueur est : {vainqueur.nom} avec {vainqueur.points_de_vie} PV et {vainqueur.xp} XP ")


                  
                  
        
        

        


