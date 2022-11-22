from random import shuffle
from personnages import CARACTERISTIQUES
from personnages import charger_personnages

def types_caracteristiques_ordre_aleatoire():
    """
    Returns:
        list: liste(ordre aléatoire) des types de caractéristiques
    """
    type_caracteristique = list(CARACTERISTIQUES.keys())
    shuffle(type_caracteristique)
    return type_caracteristique

def valeurs_ordre_aleatoire(type_caracteristique):
    """
    Args:
        type_caracteristique (string): Le type de caractéristique
    Returns:
        list: liste(ordre aléatoire) des valeurs possibles pour ce type de caractéristique
    """
    liste_valeur_caracteristique = CARACTERISTIQUES.get(type_caracteristique)
    valeur_caracteristique = liste_valeur_caracteristique.copy()
    shuffle(valeur_caracteristique)
    return valeur_caracteristique

def possede(donnees_personnage, type_caracteristique, valeur_caracteristique):
    """
    Args:
        donnees_personnage (dict): Les données (sous forme type:valeur) pour un personnage
        type_caracteristique: Le type de caractéristique analysé
        valeur_caracteristique: La valeur de la caractéristique recherchée
    Returns:
        bool: True si le personnage possède la caractéristique, False sinon.
    """
    possede_characteristique = False
    if valeur_caracteristique in donnees_personnage[type_caracteristique]:
        possede_characteristique = True
    return possede_characteristique

def score_dichotomie(personnages_restants, type_caracteristique, valeur_caracteristique):
    """
    Args:
        personnages_restants (dict): L'ensemble des personnages n'ayant pas été éliminés encore.
        type_caracteristique (string): Le type de la caractéristique dont on veut connaître le score
        valeur_caracteristique (string): La valeur de la caractéristique dont on veut connaître le score
    Returns:
        int: score de dichotomie (nombre de personnages total - maximum(nombre de personnages ayant la caractéristique, nombre de personnages n'ayant pas la caractéristique))
    """
    personnages_ayant = 0
    personnages_nayant_pas = 0

    for nom_personnage in personnages_restants:
        if possede(personnages_restants.get(nom_personnage), type_caracteristique, valeur_caracteristique):
            personnages_ayant += 1
        else:
            personnages_nayant_pas += 1
    dichotomie_score = len(personnages_restants) - max(personnages_ayant, personnages_nayant_pas)
    return dichotomie_score

def selectionner_caracteristique(personnages_restants):
    """
    Args:
        personnages_restants (dict): Les personnages à considérer pour les scores.
    Returns:
        (string, string): Le type et la valeur ayant le meilleur score dichotomique
    """
    meilleur_score = 0
    for type in types_caracteristiques_ordre_aleatoire():
        for valeur in valeurs_ordre_aleatoire(type):
            score = score_dichotomie(personnages_restants, type, valeur)
            if score >= meilleur_score:
                meilleur_score = score
                meilleur_type = type
                meilleur_valeur = valeur
    return (meilleur_type, meilleur_valeur)

def mettre_a_jour_hypotheses(personnages_restants, type_caracteristique, valeur_caracteristique, reponse):
    """
    Args:
        personnages_restants (dict): Les personnages préalablement restants
        type_caracteristique (string): Le type de la caractéristique dont on
                                       veut conserver/enlever ceux qui l'ont
        valeur_caracteristique (string): La valeur de la caractéristique dont
                                   on veut conserver/enlever ceux qui l'ont
        reponse (bool): True si on doit conserver les personnages qui possèdent la caractéristique,
                        False si on doit conserver ceux qui ne la possèdent pas.
    Returns:
        dict: Le dictionnaire de personnages restants mis à jour.
    """
    personnages_restants_maj = personnages_restants.copy()
    for nom_personnage in personnages_restants: 
        if reponse and not possede(personnages_restants[nom_personnage], type_caracteristique, valeur_caracteristique):
            del personnages_restants_maj[nom_personnage]
        if not reponse and possede(personnages_restants[nom_personnage],type_caracteristique, valeur_caracteristique):
            del personnages_restants_maj[nom_personnage]
    return personnages_restants_maj

if __name__ == '__main__':
    print("Tests unitaires...")

    # Test de la fonction types_caracteristiques_ordre_aleatoire
    assert len(types_caracteristiques_ordre_aleatoire()) == len(CARACTERISTIQUES)

    # Test de la fonction valeurs_ordre_aleatoire
    assert len(valeurs_ordre_aleatoire("cheveux")) == len(CARACTERISTIQUES["cheveux"])

    # Tests de la fonction possede
    donnees = {"cheveux": "bruns", "accessoires": ["chapeau"]}
    assert possede(donnees, "cheveux", "bruns")
    assert not possede(donnees, "accessoires", "bijoux")

    # Tests de la fonction score_dichotomie
    personnages = {'Bernard': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Claire': {'genre': 'femme', 'accessoires': ['chapeau']},
                   'Eric': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'George': {'genre': 'homme', 'accessoires': ['chapeau']},
                   'Maria': {'genre': 'femme', 'accessoires': ['chapeau']}}
    assert score_dichotomie(personnages, 'genre', 'homme') == 2  # = 5 - max(3, 2)
    assert score_dichotomie(personnages, 'accessoires', 'chapeau') == 0  # = 5 - max(5, 0)

    # Aucun test n'est fourni pour selectionner_caracteristiques
    # **mon test (pas complet)
    assert selectionner_caracteristique(charger_personnages()) == ("cheveux", "roux")  

    # Tests de la fonction mettre_a_jour_hypotheses
    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', True)) == 3
    assert len(mettre_a_jour_hypotheses(personnages, 'genre', 'homme', False)) == 2
    
    print("Tests réussis!")