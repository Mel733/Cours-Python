#P.O.O = Programmation Orienté Objet
#Clasee = plan ayant des propriete(attributs) mais aussi méthodes
#tout sa ppour créer des objets
#les objets sont des instances de classes (on partle d'instansation)

class Personne :
  def __init__(self, nom, age): #parametres pour preciser au instances d'objet qu'elle parametre utilisé
    self.nom = nom #propriété nom
    self.age = age #propriété age
    

  def sePresenter(self): #fonction qui présente la personne selon l'age et le nom
   return  f"Je m'appelle {self.nom} et j'ai {self.age}"

  def viellir(self):
    self.age += 1
    return f"Maintenant j'ai {self.age}"


#instansation
alicia = Personne("Alicia", 19) #le self renvoie a l'objet alicia créer a partire de la classe Personne
print(f"{alicia.sePresenter()}\n{alicia.viellir()}") #une facon de mettre la méthode viellir

mark = Personne("Mark", 21)
print(f"{mark.sePresenter()} {mark.viellir()}")
mark.viellir()

thomas = Personne("Thomas", 20)
print(f"{thomas.sePresenter()}")
thomas.viellir()

#---------------------------------
class CompteBancaire:
   def __init__(self, titulaire, solde): #self est un objet
     #propriété ou attribut du compte bancaire
     self.titulaire = titulaire
     self.solde = solde

     def deposer(self, montant):
       if montant > 0 :
         self.solde+= montant
       else :
           print("Solde insuffisant")

     def retirer(self, montant):
        if montant > 0:
         if self.code >= montant:
            self.solde -= montant
         else :
          print("Solde insuffisant")
        else :
        #on lève une execption si le montant est négatif
         raise ValueError("Le montant doit etre positif")
        
     def consilter(self):
       return f"Titulaire : {self.titulaire}, Solde restant : {self.solde}"  
     

monCompte = CompteBancaire("Mélodie", 19000)# en marche pas voire pourquoi
monCompte.deposer(50000)
monCompte.retirer(500000)
print(monCompte.consulter())

#l'héritage
class Vehicule:
  def __init__ (self,marque,modele,annee):
    self.marque = marque
    self.modele= modele
    self.annee = annee
    self.kilometrage = 0

  def rouler(self, distance):
   self.kilometrage += distance
   print(f"Le véhicule a roulé {self.distance} km, kilometrage total : {self.kilometrage}")

  def afficher_infos(self):
   return f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Kilométrage : {self.kilometrage} km"


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, nb_portes):
      super().__init__(marque, modele, annee)
      self.nb_portes = nb_portes

    def klaxonner(self):
      return "Klaxon !"

    def afficher_infos(self):
      print(f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee}, Kilométrage : {self.kilometrage} km, Nombre de porte : {self.nb_portes}")


class Moto(Vehicule):
  def __init__(self, marque, modele, annee, cylindree):
    super().__init__(marque, modele, annee)
    self.cylindree = cylindree

  def faire_wheelie(self):
     return "La moto fait un wheelie"


maVoiture