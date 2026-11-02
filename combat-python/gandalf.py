from personnage import Personnage
#on importe la Classe Personnage dans le fichier personnage
class Gandalf(Personnage):     #on créer la classe Gandalf qui hérite de la classe Personnage
     def __init__(self):     #le constructeur de l'objet
         attaques = [     #une liste d'attaques, chaque attaque est sous forme de dictionnaire avec clé, valeur pour le nom, degat et esquive pour l'attaque
                     {"nom": "Coup de Bâton", "dégats":12, "esquive": 0.10},
                     {"nom": "Eclaire Magique", "dégats":20, "esquive": 0.25},
                     {"nom": "Flamme d'Anor", "dégats":32, "esquive": 0.50}
            ]
         super().__init__("Gandalf", 100, attaques)    # super().__init__(...) appelle le constructeur de la classe mère Personnage.
# Il initialise nom="Gandalf", points de vie=100 et attaques, sans réécrire le code.

     def presentation(self):    #méthode pour présenter
        return f"{self.nom } entre dans l'arène sur le dos de son cheval blanc" #return une phrase pour présenter avec le nom de l'objet
