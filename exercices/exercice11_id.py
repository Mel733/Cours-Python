
def prenom_identifiant(prenom, nom): #fonction avec parametre nom et prenom
    prenom = prenom.strip() #enlever les espaces autour du prenom
    nom =nom.strip().replace(" ","").replace("-", "") #enleve les espace et remplace les espaces et tiret pas rien
    return(prenom[0]+nom[:7].lower()) #retourne le prenom avec seulement l'initial collé au nom qui affiche max 8 caractere + nom en miniscule 


def numero_telephone (numero): #fonction avec parametre numero
     numero = (numero.strip() # enleve les espaces
               .replace(".","") #remplace le . par rien
               .replace("-","") #remplace le - par rien
               .replace(" ", "")) # remplace les espaces par rien
     return numero.replace(numero[2:8], "******") #retounrne le numero et remplace les chiffres par étoiles entre le 2nd et 8ème caractere


def code_postal(code): #fonction avec parametre code
    return code.isdigit() and len(code)==5 # retourne un booélen True si le code a 5 caractere et si ils sont tous des chiffres

def compter_mots(texte): #fonction avec parametre texte
    return len(texte.split()) #coupe la phrase afin de compter le nombre de mot

def main(): #fonction du programme principal, il a afficher des valeur tout en executant les fonctions crée
     print(prenom_identifiant("Mélodie", "Robert"))
     print(numero_telephone("07 67 43 23 12"))
     print(code_postal ("94210"))
     print(compter_mots ("Bonjour tout le monde"))

main()#lancement du programme principal