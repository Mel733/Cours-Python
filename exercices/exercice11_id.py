
def prenom_identifiant(prenom, nom):
    prenom = prenom.strip()
    nom =nom.strip().replace(" ","").replace("-", "")
    return(prenom[0]+nom[:7].lower())


def numero_telephone (numero):
     numero = (numero.strip()
               .replace(".","")
               .replace("-","")
               .replace(" ", ""))
     return numero.replace(numero[2:8], "******")


def code_postal(code):
    return code.isdigit() and len(code)==5

def compter_mots(texte):
    return len(texte.split())

def main():
     print(prenom_identifiant("Mélodie", "Robert"))
     print(numero_telephone("07 67 43 23 12"))
     print(code_postal ("94210"))
     print(compter_mots ("Bonjour tout le monde"))

main()