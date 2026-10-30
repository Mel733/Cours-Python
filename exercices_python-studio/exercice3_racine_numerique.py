# ---------- Fonction 1 : somme des chiffres d'un nombre ----------
# Exemple : somme_chiffres(9875) renvoie 9 + 8 + 7 + 5 = 29
def somme_chiffres(n):
    # CAS DE BASE : si n n'a qu'un chiffre (n < 10),
    # la somme de ses chiffres, c'est lui-même. On arrête la récursion.
    if n < 10:
        return n
    # CAS RÉCURSIF : on sépare le dernier chiffre du reste du nombre.
    # n % 10  -> dernier chiffre (9875 -> 5)
    # n // 10 -> nombre sans son dernier chiffre (9875 -> 987)
    # La fonction s'appelle elle-même sur le nombre raccourci.
    return (n % 10) + somme_chiffres(n // 10)


# ---------- Fonction 2 : liste des étapes jusqu'à la racine numérique ----------
# Exemple : etapes(9875) renvoie [9875, 29, 11, 2]
def etapes(n):
    # CAS DE BASE : si n n'a qu'un chiffre, on a fini.
    # La liste ne contient que ce nombre.
    if n < 10:
        return [n]
    # CAS RÉCURSIF : on met n au début de la liste,
    # puis on y colle les étapes du nombre suivant.
    # Le nombre suivant = somme des chiffres de n (9875 -> 29).
    return [n] + etapes(somme_chiffres(n))


# ---------- Programme principal ----------
# On lit le nombre saisi par l'utilisateur et on le convertit en entier
nombre = int(input())
# On calcule toutes les étapes (ex : [9875, 29, 11, 2])
suite = etapes(nombre)

# Affiche la somme des chiffres du nombre de départ (une seule passe)
print(f"Somme des chiffres : {somme_chiffres(nombre)}")
# Transforme chaque nombre de la liste en texte et les relie par " -> "
print(f"Étapes : {' -> '.join(str(valeur) for valeur in suite)}")
# suite[-1] = dernier élément de la liste = la racine numérique
print(f"Racine numérique : {suite[-1]}")