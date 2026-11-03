liste1 = [int(x) for x in input().split()]   #liste en compréhension : on découpe la saisie aux espaces et on convertit chaque morceau en int
liste2 = [int(x) for x in input().split()]
fusion = []
i = j = 0   #i et j sont les index courants de liste1 et liste2

while i < len(liste1) and j < len(liste2):   #tant qu'aucune des deux listes n'est entièrement parcourue (on compare les valeurs aux index i et j)
   if liste1[i]<=liste2[j]:   #si le chiffre courant de la liste 1 est inférieur ou égal à celui de la liste 2
     fusion.append(liste1[i])   #ajoute le plus petit dans la liste fusion
     i += 1   #on incrémente i : on passe à l'élément suivant de liste1
   else :
     fusion.append(liste2[j]) #pareil avec liste2
     j += 1   #on passe à l'élément suivant de liste2
     
fusion.extend(liste1[i:])   #ajoute le reste de liste1 (tranche à partir de i) : il est déjà trié
fusion.extend(liste2[j:])   #pareil pour liste2 (une des deux tranches est vide)


print(" ".join(str(x) for x in fusion))   #affiche fusion : chaque nombre est converti en str, puis join les sépare par un espace