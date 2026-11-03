def ligne_facture(article, prix, quantite=1):    #crée la fonction ligne_facture avec les paramètres article, prix et quantite (valeur par défaut = 1, donc optionnel)
    total = prix*quantite    #on calcule le total d'un article
    print(f"{article} x{quantite} : {total:.2f} €")   #on affiche une ligne avec le total (2 décimales)
    return total #on retourne le total pour l'additionner plus tard


nombre = int(input())   #demande combien de lignes de facture (conversion str -> int)
total_facture = 0 #initialisé à 0
for _ in range(nombre):   #pour chaque ligne de facture demandée (_ = variable jetable) :
    morceaux = input().split()   #split() découpe la saisie aux espaces et donne une liste [article, prix, quantité]
    article = morceaux[0]   #article = élément à l'index 0 de la liste
    prix = float(morceaux[1])   #prix = élément à l'index 1, converti en float
    if len(morceaux) == 2 :   #si la liste contient 2 éléments (pas de quantité saisie)
      total_facture += ligne_facture(article, prix)   #on appelle la fonction sans quantité (valeur par défaut 1) et on ajoute le total à total_facture
    else :   #sinon (la quantité est présente)
        quantite = int(morceaux[2])   #quantite = élément à l'index 2, converti en int
        total_facture += ligne_facture(article, prix, quantite)   #même chose, mais avec la quantité

print(f"Total : {total_facture:.2f} €")   #on affiche le total de la facture (2 décimales)