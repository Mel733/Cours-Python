class SoldeInsuffisant(Exception):   #crée une exception personnalisée qui hérite de Exception
    pass   #pas de code supplémentaire : la classe sert juste de "type d'erreur"


def retirer(solde, montant):   #fonction qui retire un montant du solde et renvoie le nouveau solde
        if montant>solde:   #si on demande plus que ce qu'il y a sur le compte
            raise SoldeInsuffisant(f"Refusé : il manque {montant-solde:.2f} €")   #raise déclenche l'exception avec un message (montant manquant, 2 décimales)
        if montant<=0:   #si le montant est nul ou négatif
            raise ValueError   #déclenche une ValueError (montant invalide)
        return solde - montant   #sinon on renvoie le nouveau solde


solde = float(input())   #demande le solde de départ (conversion str -> float)
nombre = int(input())   #demande combien de retraits on va saisir
for _ in range(nombre):   #pour chaque retrait (_ = variable jetable)
 try :   #on essaie d'exécuter le bloc ; si une exception est levée, on saute au except correspondant
     texte = input()   #on garde la saisie brute pour pouvoir l'afficher en cas d'erreur
     montant = float(texte)   #conversion en float : lève une ValueError si ce n'est pas un nombre (ex. "abc")
     solde = retirer(solde, montant)   #on appelle la fonction et on met à jour le solde
     print(f"Retrait de {montant:.2f} €, solde {solde:.2f} €")   #affiche le retrait réussi et le nouveau solde
 except SoldeInsuffisant as erreur:   #si le solde est insuffisant, on récupère l'exception dans "erreur"
     print (erreur)   #affiche le message de l'exception ("Refusé : il manque ...")
 except ValueError:   #si le texte n'est pas un nombre OU si le montant est <= 0
     print(f"Montant invalide : {texte}")   #affiche le message avec la saisie d'origine

print(f"Solde final : {solde:.2f} €")   #affiche le solde final