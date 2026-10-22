# TUPLES : collection ordonnée et immuable (on ne peut ni modifier, ni ajouter, ni supprimer)

exemple_tuple = ("Mélodie", 18, True)
print(exemple_tuple[0])    # Mélodie (premier élément)
print(exemple_tuple[-1])   # True (dernier élément)

# Tuple d'un seul élément : la virgule est obligatoire
une_valeur = ("Mélodie",)

# --- Déballage (unpacking) ---
date = (22, "octobre", 2026)
jour, mois, annee = date   # chaque variable reçoit un élément, dans l'ordre
print(f"Jour : {jour}, Mois : {mois}, Année : {annee}")

# --- Une fonction peut renvoyer un tuple ---
def statistique(notes):
    # renvoie 3 valeurs, dans cet ordre : moyenne, max, min
    return (sum(notes) / len(notes), max(notes), min(notes))

resultat = statistique([12.0, 15.5, 18.25]) 
print(resultat)      #affcihe 15.25, 18.25, 12.0 : 15.25 est la moyenne car somme note au dessus/3 =15.25     
                     # le tuple complet
                     
# Déballage du résultat (même ordre que le return !)
moyenne, maximum, minimum = resultat

# Ou directement à l'appel
moyenne, note_max, note_min = statistique([12.0, 15.5, 18.25])
print(f"Note min : {note_min}, Note max : {note_max}, Moyenne : {moyenne:.2f}")

# --- Immuabilité ---
etudiant = ("Melvin", "Tom", "Tim")
print(etudiant[0])         # Melvin (lecture possible)
# etudiant[1] = "Mélodie"  # TypeError : un tuple ne se modifie pas

