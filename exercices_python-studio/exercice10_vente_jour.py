n = int(input())   #demande combien de lignes (par exemple de produits ou vendeurs) on va saisir
ventes = [[int(valeur) for valeur in input().split()] for _ in range(n)]   #liste de listes (matrice) : pour chaque ligne, split() découpe aux espaces et on convertit chaque valeur en int

par_jour = [[ventes[i][j] for i in range(n)]for j in range(len(ventes[0]))]   #transposée de la matrice : pour chaque colonne j (un jour), on récupère la valeur de chaque ligne i. Les lignes deviennent des colonnes

for numero, jour in enumerate(par_jour, start=1):   #enumerate donne (numéro, liste du jour), numérotation à partir de 1
    print(f"Jour {numero} : {' '.join(str(valeur) for valeur in jour)}")   #affiche les ventes du jour, chaque valeur convertie en str puis séparée par un espace

totaux = [sum(jour) for jour in par_jour]   #total des ventes de chaque jour (sum de chaque liste)
print(f"Totaux : {totaux}")   #affiche la liste des totaux
print(f"Meilleur jour : {totaux.index(max(totaux))+1}")   #max() trouve le plus grand total, index() donne sa position (à partir de 0), +1 car les jours commencent à 1