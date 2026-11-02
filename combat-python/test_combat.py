from gandalf import Gandalf
from roi_mort_angmar import RoiMort

def test_regles():
    gandalf = Gandalf()
    roimort = RoiMort()

    assert len(gandalf.attaques) == 3, "Gandalf devrait avoir trois attaques"
    assert len(roimort.attaques) == 3, "Roi Mort devrait avoir trois attaques"

    message = gandalf.attaquer(roimort, 0, tirage_aleatoire=0.0)
    assert "a esquivé " in message, "L'attaque ne doit être esquivé"
    assert roimort.points_de_vie == 100, "Le roi mort de devrait pas subir de dégats"
    assert gandalf.xp == 0, "Gandalf ne devrait as gagner d'xp si l'attaque est esquivé"


    message = gandalf.attaquer(roimort, 0, tirage_aleatoire=0.99)
    assert "a esquivé" not in message, "l'attaque ne doit pas etre esquivé"
    assert roimort.points_de_vie < 100, "Le roi mort devrait subir des dégats"
    assert gandalf.xp == 10, "Gandalf devrait gagner 10xp après une attaque réussie"

    for _ in range(20):
        gandalf.gagner_xp()
        assert gandalf.coef_puissance()<= 2, "Le coef de puissance ne doit pas dépasser 2"

    roimort.subir_degats(roimort.points_de_vie+10)
    assert not roimort.est_vivant(), "Le roi devrait etre mort apres avoir recu des dégats supérieur a ses point de vie"
    assert roimort.points_de_vie == 0, "Les pv du roi de doivent pas êtres négatifs"



    message = gandalf.attaquer(roimort, 0, tirage_aleatoire=0.99)
    assert "attaque invalide" in message, "Gandalf ne devrait pas pouvoir attaquer un perso mort"
    

    autre_gandalf = Gandalf()
    gandalf.subir_degats(gandalf.points_de_vie + 10)
    
    message =autre_gandalf.attaquer(gandalf, 0, tirage_aleatoire=0.99)
    assert "attaque invalide" in message, "L'autre Gandalf ne devrait pas pouvoir attaquer un perso mort"
        



if __name__ =="__main__":
    test_regles()
    print("Tout les teste sont reussi")