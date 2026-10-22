# =====================================================================
# P.O.O. : PROGRAMMATION ORIENTÉE OBJET
# =====================================================================
# Classe   : un plan (modèle) qui décrit des attributs (infos) et des méthodes(ou appéler fonctions) (actions)
# Objet    : une "copie" créée à partir de la classe (on dit une instance)
# Instanciation : le fait de créer un objet à partir d'une classe

# ---------------------------------------------------------------------
# EXEMPLE 1 : la classe Personne
# ---------------------------------------------------------------------
class Personne:

    # __init__ : s'exécute automatiquement à la création d'un objet
    # self = l'objet en cours de création
    def __init__(self, nom, age):
        self.nom = nom     # attribut nom
        self.age = age     # attribut age

    # Méthode : renvoie une phrase de présentation
    def sePresenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans"

    # Méthode : ajoute 1 an à la personne
    def viellir(self):
        self.age += 1
        return f"Maintenant j'ai {self.age} ans"


# Instanciation : on crée des objets à partir de la classe
alicia = Personne("Alicia", 19)    # self = alicia
print(f"{alicia.sePresenter()}\n{alicia.viellir()}")   # \n = retour à la ligne

mark = Personne("Mark", 21)
print(f"{mark.sePresenter()}")
print(f"{mark.viellir()}")                    

thomas = Personne("Thomas", 20)
print(f"{thomas.sePresenter()}")
thomas.viellir()
print(f"{thomas.sePresenter()}")

# ---------------------------------------------------------------------
# EXEMPLE 2 : la classe CompteBancaire
# ---------------------------------------------------------------------
class CompteBancaire:

    def __init__(self, titulaire, solde):
        self.titulaire = titulaire   # nom du propriétaire
        self.solde = solde           # argent sur le compte

    # Ajoute de l'argent
    def deposer(self, montant):
        if montant > 0:          #vérifie si chiffre positif lors du dépot
            self.solde += montant
        else:
            print("Le montant doit être positif") 

    # Retire de l'argent
    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:      # assez d'argent ?
                self.solde -= montant
            else:
                print("Solde insuffisant")
        else:
            # on lève une exception si le montant est négatif ou nul
            raise ValueError("Le montant doit être positif")

    # Renvoie les infos du compte
    def consulter(self):
        return f"Titulaire : {self.titulaire}, Solde restant : {self.solde}"


monCompte = CompteBancaire("Mélodie", 19000)
monCompte.deposer(50000)       # solde : 69000
monCompte.retirer(500000)      # trop élevé -> "Solde insuffisant"
print(monCompte.consulter())

# ---------------------------------------------------------------------
# EXEMPLE 3 : L'HÉRITAGE
# ---------------------------------------------------------------------
# Une classe "enfant" reprend tout ce que contient la classe "parent",
# et peut y ajouter ses propres attributs et méthodes.

# Classe PARENT : ce que tous les véhicules ont en commun
class Vehicule:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = 0         # tout véhicule neuf commence à 0 km

    def rouler(self, distance):
        self.kilometrage += distance
        # distance (le paramètre) 
        print(f"Le véhicule a roulé {distance} km, kilométrage total : {self.kilometrage}")

    def afficher_infos(self):
        return f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Kilométrage : {self.kilometrage} km"


# Classe ENFANT : Voiture hérite de Vehicule (le parent est entre parenthèses)
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nb_portes):
        super().__init__(marque, modele, annee)   # super() = appelle le __init__ du parent
        self.nb_portes = nb_portes                # attribut propre à Voiture

    # Méthode propre à Voiture
    def klaxonner(self):
        return "Klaxon !"

    # Même nom que dans le parent : celle-ci REMPLACE celle du parent (redéfinition)
    # On utilise return (et non print) pour que print(maVoiture.afficher_infos()) marche 
    def afficher_infos(self):
        return f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Kilométrage : {self.kilometrage} km, Nombre de portes : {self.nb_portes}"


# Classe ENFANT : Moto hérite aussi de Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, cylindree):
        super().__init__(marque, modele, annee)
        self.cylindree = cylindree                # attribut propre à Moto

    # Méthode propre à Moto
    def faire_wheelie(self):
        return "La moto fait un wheelie"


# --- Utilisation ---
maVoiture = Voiture("Peugeot", "308", 2020, 5)
maVoiture.rouler(120)                    # méthode héritée de Vehicule
print(maVoiture.afficher_infos())        # version de Voiture
print(maVoiture.klaxonner())

maMoto = Moto("Yamaha", "MT-07", 2021, 689)
print(maMoto.afficher_infos())           # version héritée de Vehicule (Moto n'a pas la sienne)
print(maMoto.faire_wheelie())
