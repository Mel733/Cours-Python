liste1 = [int(x) for x in input().split()]
liste2 = [int(x) for x in input().split()]
fusion = []
i = j = 0

while i < len(liste1) and j < len(liste2): #compare le nombre d'élément dans leur liste respective jusque une d'entre elle est vide
   if liste1[i]<=liste2[j]: #si le  chiffre courant de la liste 1 est inférieur ou égale au  chiffre courant de la liste 2
     fusion.append(liste1[i]) #ajoute le nombre courant dans la liste fusion
     i += 1 #ajoute une incrémentation de 1 à i
   else :
     fusion.append(liste2[j]) #pareil
     j += 1 #pareil
     
fusion.extend(liste1[i:]) #ajoute le reste dans la liste fusion
fusion.extend(liste2[j:]) #pareil


print(" ".join(str(x) for x in fusion)) #affiche la liste fusion, ajoute un esoace entre les chiffres qui sont convertie en string