class Parapluie: # Créer la classe Parapluie. Une classe est un modèle : chaque parapluie sera un objet créé à partir d'elle 

    def __init__(self, numero, couleur, defaut, etat): #C'est le constructeurs : c'est une méthode pour la création d'un objet avec les atrributs
        self.numero = numero #self désigne l'objet en cours avec son attribut
        self.couleur = couleur
        self.defaut = defaut
        self.etat = etat








class AtelierParapluies: # Créer la classe AtelierParapluie. Une classe est un modèle : chaque atelier sera un objet créé à partir d'elle
    def __init__(self, nom): #C'est le constructeurs : c'est une méthode pour la création d'un objet avec les atrributs
        self.nom = nom
        self.liste_parapluies = [] #attribut de l'atelier sous forme de liste pour l'instant vide, elle est comme l'étagère ou se retouve les parapluies

   
      
     
    def DeposerParapluie (self, parapluie): #méthode pour deposer un parapluie avec comme paramtere l'objet parapluie
        for p in self.liste_parapluies : #verifier chaque parapluie dans la liste
           if p.numero == parapluie.numero : #si le numéro d'un parapluie dans la liste est égale au numero du autre parapluie qu'on dépose
               print("Deja présent") #message d'indication que il est déja present dans la liste
               break #fin boucle
        else: #si aucun doublons n'a été touvé
              parapluie.etat = "en attente" #on change l'état de l'objet parapluie
              self.liste_parapluies.append(parapluie) #et on l'ajoute dans la liste
             
    def RechercherParapluie(self,numero): #méthode pour rechercher un parapluie avec comme parametre le numero
        if not self.liste_parapluies: #si il y a pas de parapluies dans la liste
            print("Liste vide") #message qui le previent
            return #arrrete la méthode
        for p in self.liste_parapluies: #verifier chaque parapluie dans la liste
            if p.numero == numero: #sinon si le numero du parapluie est égale au numéro du parapluie recherché
                p.etat = "réparé" #on change son état
                break #fin boucle
        else : #si on a pas trouver le numéro
          raise ValueError("Numéro inexistant")   #on lève une execption, on interrompt le programme avec une erreur
    
           

    def AfficherParapluies(self) : #méthode pour afficher les parapluies
        if not self.liste_parapluies: #si aucun parapluie dans la liste
            print("Liste vide") #message qui le dit
        else :
            trouve = False # sinon on met la valeur false a touve tant qu'il n'a rien touvé
            for p in self.liste_parapluies: #verifier chaque parapluie dans la liste
                if p.etat == "en attente": #si l'état du parapluie est en attente
                    print(f"Numéro :{p.numero}, Etat : {p.etat}") #alors on l'affiche
                    trouve = True #on le met en True car il en a trouvé
            if not trouve: #si trouve est toujours false
              print("Aucun en réparation") #alors message indicant que aucune réparation
         
            

monAtelier =AtelierParapluies("La Seconde Pluie") #on créer un objet monAtelier de la classe AtelierParapluie
monAtelier.DeposerParapluie(Parapluie("P-17","rouge","poignet cassée", "cassé" )) #on créer un objet parapluie avec ces atrributs et on appelle la fonction deposer et 
monAtelier.DeposerParapluie(Parapluie("P-18", "bleu", "baleine tordue", "cassé")) #pareil mais parapluie différent
monAtelier.RechercherParapluie("P-17") #recherche ce parapluie via le numero
monAtelier.AfficherParapluies() #appelle cette fonction
       

