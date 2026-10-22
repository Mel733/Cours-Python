#les tuples: collection ordonné et immuable (on peut pas en supprimer ou modifié ou ajouter)
exemple_tuple =("Mélodie", 18, True)
print (exemple_tuple[0])
print (exemple_tuple[-1])

une_valeur = ("Mélodie",)

date = (22, "octobre", 2026) #sans fonction
#Déballage : une seule variable pour chaque élément du tuple
jour, mois, annee = date #l'emplacement et l'ordre correspond a l'ordre de la ligne 8
print(f" Jour : {jour}, Mois : {mois}, Année : {annee}")


def statistique(notes): #avec fonction
    return(sum(notes)/ len(notes), max(notes), min(notes))

resultat = statistique([12.0, 15.5, 18.25])

print (resultat)
moyenne, maximum, minimum = resultat

note_min, note_max, moyenne = statistique([12.0, 15.5, 18.25])
print(f"Note min : {note_min}, Note max : {note_max}, Moyenne : {moyenne:.2f}")

etudiant =("Melvin","Tom", "Tim")
etudiant[0] #affiche Melvin
#etudiant [1] = "Mélodie" => typeError car les tuples sont immuables


