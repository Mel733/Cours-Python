#opérateur arithmétique
print("7+2 =", 7 + 2)# addition
print("7-2 =", 7 - 2)#soustraction
print("7*2 =", 7 * 2)#multiplication
print("7/2 =", 7 / 2)#division

#// : division entière

print("7%2 =", 7 % 2)#modulo (affiche le reste d'une division)

#priorité des opérateurs
print("7+2*3 =", 7 + 2 * 3)#priorité au multiplication
print("(7+2)*3 =", (7 + 2) * 3)#priorité au calcul entre parenthèse

#comparaison : résultat boolean
print("7 > 2 =", 7 > 2)#true
print("7 < 2 =", 7 < 2)#false
print("7 == 2 =", 7 == 2)#false
print("7 != 2 =", 7 != 2)#true


#arrondis et conversion de type :
print("Arondis de 34.234567890: " , round(34.234567890, 2)) #combien de 2 chiffre apres la virgule
print ("Conversion de type :", int(34.12345678)) #conversion en 34 pile
print("Conversion de type:", float(34))#conversion en 34.0

#abération de code: flottant
print ("0.1 + 0.2 =", 0.1 + 0.2)#affiche 0.3000000
print ("0.1 + 0.2 =",round( 0.1 + 0.2, 1))#arrondi et affiche 0.3(arrondi a un chiffre apres virgule)

print ("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)#false, car 0.1 + 0.2 = 0.3000000



#conditons et logique booléennes

#== opérateur égalité
print("5 ==5:", 5 == 5)#true
print("5 == 6:", 5 == 6)#false
print("melodie == melodie:", "melodie"=="melodie")#true
print("melodie == Mélodie:", "melodie"=="Mélodie")#false => sensible a la casse

#comparaison chainées
note = 15
print("10<= note <= 20:", 10 <= note <= 20)#true

#differencier = et ==
note_parfaite = note == 20
#= affectation d'une valeur a une variable
#== comparaison
print("note_parfaite", note_parfaite)#false

#condition and, or , not
moyenne= 11.5
nombre_abscences = 4
a_rendu_son_projet = True

#and : vrai seulement si les deux conditions sont vraies
admis_sans_reserves = moyenne >= 10 and nombre_abscences <= 3
print("admis_sans_reserves:", admis_sans_reserves)#false

#or : vrai si au moins une des deux conditions est vraie
envoi_alerte = moyenne < 8 or nombre_abscences > 3
print("envoi_alerte:", envoi_alerte)#true

#not : inverse la valeur de la condition
print("Projet manquant:", not a_rendu_son_projet)#false

#parenthèses rendent les combinaisons plus lisibles
peut_passer_jury = (moyenne >= 10 or a_rendu_son_projet)and not nombre_abscences > 10
print("peut_passer_jury:", peut_passer_jury)#true