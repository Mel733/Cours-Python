# #idéee de revenir en arrière
# #fonction est récursive si elle s'appelle elle meme = > systèmes des poupées russes
# #compte a rebiuts : fonctionqui affiche les nombe de n à 0

def compte_a_rebour(n):
    if n==0:
        print("Décollage")
        return
    print(n)
    compte_a_rebour(n-1)


compte_a_rebour(5)#exemple d'apple de la fonction


#addition nombre en recursif:
def add_recursive(n):
    if n==0:
        return 0 #cas de base
    return n + add_recursive(n-1) #appel récursif

add_recursive(5)




def double_recursive(n):
    if n == 0 : #si n est 0
        return 0 #retourne 0 car cas de base
    if n <0: #si n est négatif
        return -2 + double_recursive(n + 1) #on retourne et on fait  2 + (2x( n+1 ))
    return 2 + double_recursive(n - 1) #si c'est positif : 2 + (2 × (n-1))
                

print(double_recursive(5))
print(double_recursive(8))
print(double_recursive(0))
print(double_recursive(-5))


#idée exos :
#tour hanoi