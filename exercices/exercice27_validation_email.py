emails = [" alice@exemple.fr ", "bob@site", "@site.fr", "a b@site.fr", "x@y.z"] #liste avec des emails

def emails_valides(emails): #fonction qui verifie les emails valide avec emails comme parametres
    valide = [] #liste où on stockera les emails valide
   
    for email in emails: #boucle qui vérifie chaque emails dans la liste
        email_clean = email.strip() #on nettoie l'email avec le strip
       
        if email_clean.count("@") != 1: #une condition qui compte le nombre d'@ dans l'email, si se n'es pas égale a 1
            continue #on passe a la prochaine email dans la liste
        debut, domaine = email_clean.split("@") #on decoupe l'emaile en deux en precisant que l'@ est au milieuw du début et du domaine
        if debut =="" or domaine =="": #si le début ou le domaine est vide
            continue #on passe a la prochaine email dans la liste
        elif "." not in domaine: #si il n'y a pas de point dans la partie domaine
            continue #pareil
        if " " in email_clean: #et si l'email nettoyé est vide 
            continue #pareil
        
        valide.append(email_clean) #sinon si l'email passe toute les conditions,on l'ajoute dans la liste valides
    return valide #on retourne  la liste


print(emails_valides(emails)) #on affiche le resultat de la methodes emails_valide



