from combat_manager import CombatManager #import CombatManager depuis le fichier combat_manager
# __name__ vaut "__main__" seulement si on lance CE fichier directement.
# Si le fichier est importé par un autre, le bloc est ignoré.
if __name__ == "__main__":
    combat_manager = CombatManager()  # on crée l'objet qui gère le combat depuis la Class CombatManager
    combat_manager.start()            # appele la méthode start qui lance le combar