import random
class Personnage :
    #constructeur de la classe Personnage
    def __init__(self, nom, pv, attaques = None):
        if nom is None or nom.strip()=="":
            raise ValueError("Le nom du personnage ne peut pas être vide")
        if pv <= 0:
            raise ValueError("Les points de vie doivent etre supérieur a 0")
        self.nom = nom
        self._points_de_vie = pv
        self._points_de_vie_max = pv
        self.attaques = [] if attaques is None else attaques
        self._xp = 0

    @property#getter pour les points de vie
    def points_de_vie(self):
        return self._points_de_vie

    @property
    def xp(self):
        return self._xp

    @property
    def points_de_vie_max(self):
        return self._points_de_vie_max

    def est_vivant(self):
        return self._points_de_vie>0

    def presenter(self):
        return f"{self.nom} entre dans l'arène !"

    def subir_degats(self, degat):
        if degat < 0:
            raise ValueError("Les dégats ne peuvent pas être négatif")
        self._points_de_vie = max(0, self._points_de_vie - degat)

    def gagner_xp(self):
        self._xp += 10

    def coef_puissance (self):
        return min(2, 1+self._xp/100)  

    def attaquer(self, cible, index_attaque, tirage_aleatoire = None):
        if not self.est_vivant():
            return f"{self.nom} est mort et ne peux pas attaquer"
        if not cible.est_vivant():
            return f"Index d'attaque invalide. Veuillez choisir un index entre 0 et {len(self.attaques)-1}"
        
        attaque = self.attaques[index_attaque]
        if tirage_aleatoire is None:
             tirage_aleatoire =random.random()

        if not 0 <= tirage_aleatoire<=1:
            raise ValueError("Le tirage aléatoire doit etres compris entre 0 et 1")

        if tirage_aleatoire < attaque["esquive"]:
            return f"Mais {cible.nom} a esquivé l'attaque  !"
        
        cible.subir_degats(attaque["dégats"]* self.coef_puissance())
        self.gagner_xp()

        return f"{self.nom} utilise {attaque["nom"]} sur {cible.nom} et inflige {attaque["dégats"]} points de dégats"





