def ligne_facture(article, prix, quantite=1): #créer la fonction ligne facture avec comme parametre article, prix et quantiité qui est =1 car optionnel
    total = prix*quantite #on calcule le total d'un article
    print(f"{article} x{quantite} : {total:.2f} €") #on affiche un message avec total
    return total #on retoure la valeur du total pour plus tard l'additionner


nombre = int(input()) #demande combien de ligne de facture
total_facture = 0 #initialiser a 0
for _ in range(nombre): #pour le nombre de ligne de factures demander on vas :
    morceaux = input().split() #couper la valeur donner pour morceaux séparement pour donner [article, prix, quantité]
    article = morceaux[0] #on précise que article prend la position 0 dans la liste
    prix = float(morceaux[1]) #on convertie prix en float et on précise qu'il a la position 1
    if len(morceaux) == 2 : #si la longeur de morceaux est de 2
      total_facture += ligne_facture(article, prix) #on execute la fonction avec seulement article et rix comme valeur puis on incrémente le total dans le total de la facture
    else : #autre 
        quantite = int(morceaux[2]) #on convertie en int quantite et on précise qu'il a la postion 2
        total_facture += ligne_facture(article, prix, quantite) #on fait la meme chose suaf que on rajoute la quantité

print(f"Total : {total_facture:.2f} €") #on affiche le total