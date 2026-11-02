class Article:   #classe qui représente une ligne du panier (un produit avec son prix et sa quantité)
    def __init__(self, nom, prix, quantite):   #constructeur : reçoit les 3 caractéristiques de l'article
        self.nom = nom   #attributs d'instance : propres à chaque article
        self.prix = prix
        self.quantite = quantite

    def total(self):   #calcule le total de cette ligne
        return self.prix * self.quantite   #prix unitaire x quantité


class Panier:   #classe qui gère l'ensemble des articles
    def __init__(self):   #constructeur sans paramètre : un panier commence vide
        self.articles = []   #liste d'objets Article

    def ajouter(self, nouveau):   #ajoute un article, en fusionnant s'il existe déjà
      for article in self.articles:   #on parcourt les articles déjà présents
          if article.nom == nouveau.nom:   #si un article du même nom existe déjà
              article.quantite += nouveau.quantite   #on additionne les quantités au lieu de créer un doublon
              return   #on sort de la méthode : rien d'autre à faire
      self.articles.append(nouveau)   #on arrive ici seulement si aucun article du même nom n'a été trouvé : on l'ajoute

    def total(self):   #total du panier
        return sum(article.total() for article in self.articles)   #somme des totaux de chaque article (générateur)

    def nombre_articles(self):   #nombre total d'unités dans le panier
        return sum(article.quantite for article in self.articles)   #somme des quantités (pas le nombre de lignes)


panier = Panier()   #on crée un panier vide (instance de Panier)
for _ in range(int(input())):   #lit le nombre d'articles à saisir et répète autant de fois
    nom, prix, quantite = input().split()   #découpe la saisie en 3 variables (déballage de liste)
    panier.ajouter(Article(nom, float(prix), int(quantite)))   #crée l'objet Article (avec conversions) et l'ajoute au panier
code = input()   #lit le code promo

for article in panier.articles:   #pour chaque article du panier
    print(f"{article.nom} x{article.quantite} : {article.total():.2f} €")   #affiche nom, quantité et total de la ligne (2 décimales)

total=panier.total()   #on calcule le total une fois et on le stocke
print(f"Articles : {panier.nombre_articles()}")   #affiche le nombre d'unités
print(f"Total : {total:.2f} €")   #affiche le total avant remise

remise = 0   #pas de remise par défaut
if code == "REDUC10" and total >=50:   #la remise s'applique seulement si le code est bon ET que le total atteint 50 €
    remise = total*0.10   #10 % du total
    print(f"Remise : {remise:.2f} €")   #affiche le montant de la remise

print(f"À payer : {total - remise :.2f} €")   #affiche le total moins la remise