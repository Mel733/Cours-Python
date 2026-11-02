n = int(input())   #demande combien de produits on va saisir
lignes = [input().split() for _ in range(n)]   #liste en compréhension : pour chaque produit, on lit une ligne et split() la découpe en liste [nom, prix, catégorie]
categorie_promo = input()   #catégorie sur laquelle s'applique la promotion
remise = int(input())   #pourcentage de remise (ex. 20 pour 20 %)

produits = [(ligne[0], float(ligne[1]), ligne[2])for ligne in lignes ]   #transforme chaque liste en tuple (nom, prix converti en float, catégorie)
remises = {nom :prix * (100 - remise) / 100 for nom, prix, categorie in produits if categorie == categorie_promo}   #dictionnaire en compréhension : {nom: prix remisé}, uniquement pour les produits de la catégorie en promo
categories = set(categorie for nom, prix, categorie in produits)   #set des catégories : un set supprime les doublons

print(f"Promotion sur {categorie_promo} (-{remise} %) :")   #affiche l'en-tête de la promotion
if not remises :   #si le dictionnaire est vide (aucun produit dans cette catégorie)
    print("Aucun produit concerné")   #affiche un message
for nom, prix in  sorted(remises.items(), key=lambda paire: paire[1]):   #items() donne les paires (nom, prix) ; sorted trie selon le prix (paire[1]) du moins cher au plus cher
    print(f"{nom} : {prix:.2f} €")   #affiche le nom et le prix remisé (2 décimales)
print(f"Catégories : {', '.join(sorted(categories))}")   #trie les catégories par ordre alphabétique et les assemble avec ", "