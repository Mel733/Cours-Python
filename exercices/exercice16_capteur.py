class Capteur:           #Créer la classe Capteur
  def __init__(self, nom, type, etat):             #le constructeur pour les objets capteur avec leurs attributs
    self.nom = nom            #self deisgne l'objet en cour avec son attribut
    self.type = type
    self.etat = etat


class Drone_sous_marin :          #crer la classe Drone_sous_marin
    def __init__(self, nom, profondeur_max, niveau_batterie, etat):         #le constructeur pour l'objet drone sous marin
       self.nom = nom             #self deisgne l'objet en cour avec son attribut
       self.profondeur_max = profondeur_max
       self.niveau_batterie = niveau_batterie
       self.etat = etat
       self.liste_capteurs = []        #une liste vide avec les future objets capteurs

    def AjouterCapteur(self, capteur):           #méthode pour ajouter un capteur
       for c in self.liste_capteurs:             #boucle for pour vérifier chauque capteurs dans la liste
           if c.nom == capteur.nom:             #si le nom du capteur saisie est identique à un nom de capteur déjà present dans la liste
              print("Capteur déja présent")      #on prévient le user
              break #fin méthode
       else: #
          self.liste_capteurs.append(capteur)       #on ajoute l'objet capteur dans la liste
          
              
    def check_drone(self):           #méthode pour vérifier l'état du drone
         if not self.liste_capteurs:          #si il n'y a aucun élément dans la liste
            print("liste vide")             #message pour le dire
         for c in self.liste_capteurs:       #boucle for pour vérifier les capteurs dans la liste
            if c.etat == "actif" and c.type == "sonar" and self.niveau_batterie>=30:      #si l'état du capteur est actif et que son type est sonar et que le niveau de batterie du drone est >= 30
              self.etat = "pret"          #on change l'état du drone pour dire qu'il est prêt
              print(f"Le drone sous marin est {self.nom} est prêt")       #message d'indication
              break     #fin methode
         else :
              print("Le sous marin n'est pas prêt")      #sinon message prevenant que l'une ou plusieurs des conditions ne sont pas bonne
            
         


class Mission:          #créer la classe Mission
     def __init__(self,nom, profondeur_travail, drone_mission):           #le constructeur pour les objets tiré de Mission avec ces attributs
        self.nom = nom          #self désigne l'objet en cours avec son attribut
        self.profondeur_travail = profondeur_travail
        self.drone_mission = drone_mission

     def check_mission(self):           #méthode pour vérifier si la mission peut démarrer
        if self.drone_mission.etat =="pret" and self.profondeur_travail<= self.drone_mission.profondeur_max:       #si l'etat de l'objet drone mission est pret et que la profondeur de travail de l'objet mission est <= a la profondeur max de l'objet drone
           print(f"La mission {self.nom} peut démarrer")          #message avec le nom de l'objet mission
           print(f"Prondeur de travail : {self.profondeur_travail}")         #message avec la profondeur de travail de l'objet mission
           
        else:
           print("La mission n'est pas prête")       #sinon message pour dire sue une des condition n'est pa bonne dont mission pas prete
         


monDrone = Drone_sous_marin("Néreide", 120, 78, "en attente")        #création objet monDrone avec ces attributs avec réel valeur
monDrone.AjouterCapteur(Capteur("Capteur 1","sonar", "actif"))          #on créer un objet capteur avec ces attributs et on appelle fonction pour ajouter capteur
monDrone.AjouterCapteur(Capteur("Capteur 2", "température", "inactif"))      #pareil mais attributs différent
monDrone.check_drone()           #appelle la méthode pour verifier le drone sur l'objet monDrone
maMission = Mission("Epave du phare", 80, monDrone)           #création objet maMission avec ces attriburs avec de réel valeur
maMission.check_mission()           #appelle de la methode pour verifier si la mission peut démarrer sur mon objet maMission
        
