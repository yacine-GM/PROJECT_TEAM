import argparse
from turtle import *


class QuoridorX(Quoridor):
    def __init__(self, joueurs):
        super().__init__(self, joueurs)
    def __str__(self):
        super().__str__(self)
    def déplacer_jeton(self, joueur, position):
        super().déplacer_jeton(self, joueur, position)
    def état_partie(self):
        super().état_partie(self)   
    def jouer_coup(self, joueur):
        super().jouer_coup(self, joueur)
    def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
        super().construire_graphe(joueurs, murs_horizontaux, murs_verticaux)    
    def partie_terminée(self):
        super().partie_terminée(self)
    def placer_mur(self, joueur, position, orientation):
        super().placer_mur(self, joueur, position, orientation)
    def afficher_graphe(self):
        pass


