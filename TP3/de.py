"""
La classe Dé.

Représente un dé à 6 faces.
"""

from random import randint


class De:
    """ Représente un dé à 6 faces.

    Attributes:
        valeur (int): Un nombre de 1 à 6 inclusivement.
    """
    def __init__(self):
        """
        Constructeur de la classe De.
        Avant d'être lancé, sa valeur est None.
        """
        self.valeur = None

    def affichage_string(self, mode):
        """
        Donne la représentation en chaîne de caractères de la valeur
        du dé, selon le mode [2,3,4,5,6] ou [⚁,⚂,⚃,⚄,⚅].
        Si sa valeur est 1, on affiche X peu importe le mode.

        Args:
            mode (int): Le mode (1 pour [2,3,4,5,6], 2 pour [⚁,⚂,⚃,⚄,⚅]).

        Returns:
            str: La représentation de la valeur du dé.
        """
        valeur_de = {1: ['X','2','3','4','5','6'], 2: ['X','⚁','⚂','⚃','⚄','⚅']}
        return valeur_de[mode][self.valeur-1]
        # VOTRE CODE ICI

    def lancer(self):
        """
        Modifie aléatoirement la valeur du dé.
        """
        self.valeur = randint(1, 6)

    def ranger(self):
        """
        Met la valeur du dé à None.
        """
        self.valeur = None

if __name__=='__main__':
    # test personnel (facultatif)
    de = De()
    assert de.valeur==None, "mauvaise initialisation"
    
    de.lancer()
    assert 1<=de.valeur<=6, "la valeur apres lancer n'est pas entre 1 et 6"
    
    if de.valeur==1: assert de.affichage_string(1)=='X' and de.affichage_string(2)=='X', "valeur de de 1 doit retourner X"
    else: 
        assert de.affichage_string(1)==str(de.valeur), "mode 1 non-fonctionnel"
        assert de.affichage_string(2) in ['⚁','⚂','⚃','⚄','⚅'], "mode 2 non-fonctionnel"

    print('Tests pour la classe De réussis!🔑')

