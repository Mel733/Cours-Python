class Livre:   #classe qui représente un livre de la bibliothèque
    def __init__(self, titre, auteur):   #constructeur : reçoit le titre et l'auteur
        self.titre = titre   #attributs d'instance
        self.auteur = auteur
        self.disponible = True   #un livre est disponible par défaut (pas passé en paramètre)

    def emprunter(self):   #tente d'emprunter le livre, renvoie True si réussi, False sinon
        if not self.disponible:   #si le livre est déjà emprunté
            return False   #échec
        self.disponible = False   #sinon on le marque comme emprunté
        return True   #succès

    def rendre(self):   #remet le livre à disposition
        self.disponible = True

    def __str__(self):   #méthode spéciale : définit le texte affiché par print(objet)
        etat = "disponible" if self.disponible else "emprunté"   #expression conditionnelle 
        return f"{self.titre} ({self.auteur}) : {etat}"   #renvoie le texte (return, pas print)


livres = {}   #dictionnaire {titre: objet Livre} : permet de retrouver un livre rapidement par son titre
for _ in range(int(input())):   #lit le nombre de livres et répète autant de fois
    titre, auteur = input().split(" par ")   #découpe la saisie au séparateur " par " : donne [titre, auteur]
    livres[titre] = Livre(titre, auteur)   #crée l'objet Livre et le range dans le dictionnaire avec le titre comme clé

for _ in range(int(input())):   #lit le nombre d'actions et répète autant de fois
    action, titre = input().split(" ", 1)   #découpe au premier espace seulement (1 = une seule coupure) : le titre peut donc contenir des espaces
    if titre not in livres:   #si le titre n'est pas une clé du dictionnaire
        print(f"Livre inconnu : {titre}")
    elif action == "emprunter":   #sinon, si l'action est emprunter
        if livres[titre].emprunter():   #on appelle emprunter() : le if teste le True/False renvoyé
            print(f"Emprunté : {titre}")   #succès
        else:
            print(f"Déjà emprunté : {titre}")   #échec : il était déjà emprunté
    elif action == "rendre":   #sinon, si l'action est rendre
        livres[titre].rendre()   #remet le livre disponible
        print(f"Rendu : {titre}")

for livre in livres.values():   #values() donne les objets Livre (sans les clés)
    print(livre)   #print appelle automatiquement __str__