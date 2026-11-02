class Vehicule:   #classe mère : contient ce qui est commun à tous les véhicules
    nom = "Véhicule"   #attribut de classe (partagé par toutes les instances), redéfini dans les classes filles
    tarif_jour = 0   #tarif par jour par défaut, redéfini dans les classes filles

    def __init__(self, immatriculation):   #constructeur : seule l'immatriculation change d'un véhicule à l'autre
        self.immatriculation = immatriculation   #attribut d'instance propre à chaque véhicule

    def cout(self, jours):   #calcule le coût de base de la location
        return self.tarif_jour * jours   #tarif par jour x nombre de jours

class Voiture(Vehicule):   #Voiture hérite de Vehicule
        nom ="Voiture"   #redéfinit l'attribut de classe
        tarif_jour = 45   #tarif spécifique à la voiture (pas besoin de redéfinir cout ni __init__ : hérités)

class Utilitaire(Vehicule):   #Utilitaire hérite de Vehicule
      nom="Utilitaire"
      tarif_jour = 70

      def cout(self, jours):   #redéfinit la méthode cout de la classe mère
          return super().cout(jours)+30   #super().cout() appelle le calcul de la mère, puis on ajoute 30 € de frais fixes


class Scooter(Vehicule):   #Scooter hérite de Vehicule
      nom = "Scooter"
      tarif_jour = 25

      def cout(self, jours):   #redéfinit cout
        prix = super().cout(jours)   #on récupère le coût de base via la classe mère
        if jours >= 7:   #si la location dure 7 jours ou plus
            prix *= 0.8   #remise de 20 % (on paie 80 %)
        return prix   #on renvoie le prix final


TYPES = {   #dictionnaire : associe le texte saisi à la CLASSE correspondante (sans parenthèses : on stocke la classe, pas un objet)
     "voiture": Voiture,
     "utilitaire": Utilitaire,
     "scooter": Scooter,
}

total = 0   #cumul du prix de toutes les locations
for _ in range(int(input())):   #lit le nombre de locations et répète autant de fois (_ = variable jetable)
    genre, immatriculation, jours = input().split()   #découpe la saisie en 3 variables (déballage de liste)
    jours = int(jours)   #conversion str -> int
    if genre not in TYPES:   #si le type saisi n'est pas une clé du dictionnaire
        print(f"Type inconnu : {genre}")   #message d'erreur
        continue   #passe à la saisie suivante
    vehicule = TYPES[genre](immatriculation)   #TYPES[genre] donne la classe, puis (immatriculation) crée l'objet : polymorphisme(un même appel de méthode, plusieurs comportements selon le type de l’objet.), sans if/elif
    prix = vehicule.cout(jours)   #appelle la bonne version de cout() selon la classe de l'objet
    total += prix   #ajoute au total
    print(f"{vehicule.nom} {vehicule.immatriculation}, {jours} jours : {prix:.2f} €")   #affiche le résumé de la location (2 décimales)

print(f"Total des locations : {total:.2f} €")   #affiche le total