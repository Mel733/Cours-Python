nom_etudiant = "Mélodie"
note_1 = 11.5
note_2 = 8.0
note_3 = 13.0
print("Étudiant:", nom_etudiant)
print("Notes:", note_1, note_2, note_3)
print("Moyenne:", (note_1 + note_2 + note_3) / 3)

#calculs :
nombre_de_notes = 3
somme_des_notes = note_1 + note_2 + note_3
moyenne = somme_des_notes / nombre_de_notes

#comparaison : le resultat sera un booelan
est_admis = moyenne >= 10

#affcihage des résultats
print("Nombre de notes :", nombre_de_notes)
print("Somme des notes :", somme_des_notes)
print("Moyenne :", moyenne)
print("Résultat de l'admission :", est_admis)

#verfication du typage
print("Type du 'nom_etudiant' :", type(nom_etudiant))
print("Type du 'nombre de notes' :", type(nombre_de_notes))
print("Type de la 'somme_des_notes' :", type(somme_des_notes))
print("Type de la 'moyenne' :", type(moyenne))
print("Type de 'est_admis' :", type(est_admis))