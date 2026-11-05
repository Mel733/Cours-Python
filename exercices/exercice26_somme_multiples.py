def sommes_multiples(limite, diviseur): #fonction pour calculer
    somme = 0 #accumulateur de la somme a 0
    if limite <=0 or diviseur <0: #si a limite est inférieur ou égale 0 ou si le diviseur est inférieur a 0
        print("Erreur de valeur") #erreur
    else:
        for i in range(1, limite +1): #sinon boucle qui s'enchainera selon le nombre de la limite qui commence a 1 et finis a limite +1 pour inclure le dernier chiffre de la limite
            if i % diviseur == 0: #si le modulo de 1 avec le diviseur est de O
                somme +=i #c'est un multiples et on l'ajoute dans la somme
        return somme #a la fin de la boucle on retourne la somme

print(sommes_multiples(10, 3)) #teste la fonction avec 10 de limite et 3 comme diviseur: résultat = 18
print(sommes_multiples(12, 4))
print(sommes_multiples(0, 3))