#manipulation chaine de caracteres
mot="python"
print(mot[0]) #affiche le premier caractere qui est (p)
print(mot[-1]) #affiche la dernirer lettre qui est le (n)
print(mot[-2]) #affiche l'avant dernirere lettre qui est le (o)
print(mot[1:4]) #affiche les caractere 1 à 3 qui spnt (yth)
print(mot[:3])#affiche les 3 premier caractere qui sont pyt
print(mot[3:])#affiche les 3 dernier caractere qui sont hon

print(len(mot))#affiche la longeur du mot (6)

#print(mot[9]) => erreur car l'index(ou indice(lettre)) 9 n'existe pas dans la chaine "python"
mot[::-1]#"nohtyp" affiche a l'envers

#strip() supprime les espaces au début et a la fin d'une chaine
texte ="   Bonjour   "
print(texte.strip()) #"Bonjour"

#lower()convertit tous les caractères d'une chaine en miniscules
print(texte.lower()) #"   bonjour   "

#upper() : convertit tous les caracteres d'une chaine en majuscules
print(texte.upper()) #"   BONJOUR   "

#title() : convertit la premiere de chaque mot en majuscules
prenom = "mélodie robert"
print(prenom.title()) #Mélodie Robert"

#replace() : remplace une sous-chaine par une autre
texte_modifie = texte.replace("Bonjour", "Bonsoir").strip()
print(texte_modifie) #Bonsoir

#find(): retrouve l'index de la première occurence d'une sous-chaine, ou -1 si elle existe pas.
phrase ="Bonjour tout le monde"
print(phrase.find("le")) #12
print(phrase.find("la")) #-1

#Sous-chaine : mot dans une chaine de caractère 
#Occurence : nombre de fois qu'un élément spécifique apparait au sein d'une chaine ou liste

#in : retourne True si une sous-chaine est présente dans la chaine, False sinon
print("Bonjour" in phrase) #True
print("Python" in phrase) #False

#isdigit() : retourne True si tous les caractères de la chaine sont des chiffres, False sinon
print("1234".isdigit()) #True
print("1234a".isdigit()) #False

#isalpha(): retourne True si tous les caractères de la chaine sont des lettres, False sinon
print("abcde".isalpha()) #True
print("abcde1".isalpha()) #False
