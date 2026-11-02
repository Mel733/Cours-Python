from personnage import Personnage
class RoiMort(Personnage):
     def __init__(self):
        attaques = [
                         {"nom": "Coup d'épée", "dégats":14, "esquive": 0.10},
                         {"nom": "Lame de Mogul", "dégats":22, "esquive": 0.30},
                         {"nom": "Souffle d'effroi", "dégats":30, "esquive": 0.45}
        ]
        super().__init__("Roi Mort", 100, attaques)


     def presentation(self):
            return f"{self.nom } entre dans l'arène sur le dos de son dragon"
    