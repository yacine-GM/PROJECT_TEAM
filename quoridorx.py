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
     def jouer_coup():
         if nx.shortest_path(graphe, self.pos1, 'B1') < nx.shortest_path(graphe, self.pos2, 'B2'):
             self.déplacer_jeton(position=p[1])
        else:
            if (self.pos2[0], self.pos2[1]-1) != list(self.murs):
                self.placer_mur(joueur=1, position=(self.pos2[0], self.pos2[1]-1), orientation='horizontal')
            elif (self.pos2[0], self.pos2[1]-1) == list(self.murs) and (self.pos2[0]-1, self.pos[1]) != list(self.murs):
                self.placer_mur(joueur=1, position=(self.pos2[0]-1, self.pos2[1]), orientation='vertical')
            elif (self.pos2[0], self.pos2[1]-1) == list(self.murs) and (self.pos2[0]-1, self.pos2[1]) == list(self.murs) and (self.pos2[0]+1, self.pos2[1]) != list(self.murs):
                self.placer_mur(joueur=1, position=(self.pos2[0]+1, self.pos2[1]), orientation='vertical')
        if self.joueur != 0 or self.joueur != 1:
            raise QuoridorError('Le numéro de joueur doit être 1 ou 2.')
        if self.partie_terminée:
            raise QuoridorError('La partie est déjà terminée.')
    def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
        super().construire_graphe(joueurs, murs_horizontaux, murs_verticaux)    
    def partie_terminée(self):
        super().partie_terminée(self)
    def placer_mur(self, joueur, position, orientation):
        super().placer_mur(self, joueur, position, orientation)
    def afficher_graphe(self):
        up()
        write(buffer)
        done()
        return afficher_graphe



