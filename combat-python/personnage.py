import random      #importe le module random
class Personnage :     #créer la classe Personnage
    #constructeur de la classe Personnage
    def __init__(self, nom, pv, attaques = None):      #le init s'execute lors de la création d'un objet de la classe avec les attributs
        if nom is None or nom.strip()=="":      #si le nom est vide
            raise ValueError("Le nom du personnage ne peut pas être vide")     #leve intentionnellement une erreur
        if pv <= 0:     #si les pv sont inférieur ou égale a 0
            raise ValueError("Les points de vie doivent etre supérieur a 0")     #on fait de meme
        self.nom = nom     #self designe l'objet en cour avec son attribut nom
        self._points_de_vie = pv
        self._points_de_vie_max = pv
        self.attaques = [] if attaques is None else attaques     #si aucune attaque est fournie on crée la liste vide sinon on utilise la liste existance
        self._xp = 0     #xp est un propriété protected(designer avec "_")

    @property     #getter pour les points de vie qui est un attribut protected
    def points_de_vie(self):     #méthode pour retourner la valeur de l'attribut protected des points de vie
        return self._points_de_vie

    @property     #pareil mais pour l'xp
    def xp(self):
        return self._xp

    @property     #pareil mais pour les points de vie mx
    def points_de_vie_max(self):
        return self._points_de_vie_max

    def est_vivant(self):     #méthode pour verifier si un personnage est vivant
        return self._points_de_vie>0     #return True si pv > 0 ou false si pv<=0 

    def presenter(self):     #méthode pour présenter le personnage
        return f"{self.nom} entre dans l'arène !"     #return une phrase avec le nom de l'objet de Personnage

    def subir_degats(self, degat):     #méthode pour subir des dégats
        if degat < 0:      #si les dégat sont inférieur a 0
            raise ValueError("Les dégats ne peuvent pas être négatif")     #on leve une erreur
        self._points_de_vie = max(0, self._points_de_vie - degat)     # On retire les dégâts aux PV, mais sans jamais descendre sous 0 :
        # max() retient 0 si le résultat est négatif, sinon pv - degat.

    def gagner_xp(self):    #methode pour gagner de l'xp
        self._xp += 10     #incrémentation de 10 a l'attribut proctected xp de l'objet

    def coef_puissance (self):     #methode pour calculer le coefficient de puissance
        return min(2, 1+self._xp/100)     # Multiplicateur basé sur l'XP : 1 + xp/100, plafonné à 2.
                # min() retient la plus petite des deux valeurs, donc 2 est le maximum autorisé.


    def attaquer(self, cible, index_attaque, tirage_aleatoire = None):    #méthode pour attaquer, le non signifie que le tirage est optionnel
        if not self.est_vivant():    #si le personage(le self, l'objet) est mort
            return f"{self.nom} est mort et ne peux pas attaquer"   #on return un message
        if not cible.est_vivant():    #si la cible n'est pas vivante
            return f"{cible.nom} est déjà mort"    #message qui le dit avec le nom de la cible

        if index_attaque < 0 or index_attaque >= len(self.attaques):     #si l'index de l'attaque est négatif ou superieur a la longueur de la liste attaques
            return f"Index d'attaque invalide. Veuillez choisir un index entre 0 et {len(self.attaques)-1}"
            #return un message qui dit de choisir entre 0 et 2 (trois attaques)
        attaque = self.attaques[index_attaque]    # On récupère l'attaque choisie : self.attaques est la liste des attaques du personnage, et index_attaque est la position de l'attaque voulue dans cette liste.
        if tirage_aleatoire is None:      # si aucun tirage n'a été fourni en argument
             tirage_aleatoire =random.random()    # on génère un nombre aléatoire entre 0.0 et 1.0

        if not 0 <= tirage_aleatoire<=1:    #si le nombre du tirage n'est pas supérieur ou égal a 0 et inférieur ou égale a 1
            raise ValueError("Le tirage aléatoire doit etres compris entre 0 et 1")    #on leve un erreur

        if tirage_aleatoire < attaque["esquive"]:    #si le tirage est inférieur au chiffre de la clé d'esquive dans le dictionaire de l'attaque dans la liste des attaques
            return f"Mais {cible.nom} a esquivé l'attaque  !"    #On prévien que la cible a esquivé
        
        cible.subir_degats(attaque["dégats"]* self.coef_puissance())    #sinon la cible subit les dégat qui sont multiplier par le coef
        self.gagner_xp()    #suite a des dégat, le personnage ayant lancer l'attaque gagne des xp

        return f"{self.nom} utilise {attaque["nom"]} sur {cible.nom} et inflige {attaque["dégats"]} points de dégats" 
    #on return une phrase avec le scénrio de la l'attque (qui? contre qui ? quelle attaque ? et combien de dégats ?)





