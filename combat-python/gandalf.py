from personnage import Personnage
class Gandalf(Personnage):
     def __init__(self):
         attaques = [
                     {"nom": "Coup de Bâton", "dégats":12, "esquive": 0.10},
                     {"nom": "Eclaire Magique", "dégats":20, "esquive": 0.25},
                     {"nom": "Flamme d'Anor", "dégats":32, "esquive": 0.50}
            ]
         super().__init__("Gandalf", 100, attaques)

     def presentation(self):
        return f"{self.nom } entre dans l'arène sur le dos de son cheval blanc"
