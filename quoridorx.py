import argparse
from turtle import *


class QuoridorX(Quoridor):
    def __init__(self, joueurs):
        super().__init__(self, joueurs)
    def __str__(self):
        up()
        buffer = "\nLégende: 1=self.nom1, 2= self.nom2\n" #À CHANGER!!!!
        buffer += f"   ----------------------------\n"
        mat_line = []
        mat_open = []

        for i in range(0, 9):
            mat_line.append(list(f"{(9-i)} | .   .   .   .   .   .   .   .   .  |\n"))
        for i in range(0, 8):
            mat_open.append(list("   |                                    |\n"))
        pos_joueur = self.pos1
        pos_automate = self.pos2
        mat_line[9-pos_joueur[1]][4 + (pos_joueur[0] - 1)*4] = "1"
        mat_line[9-pos_automate[1]][4 + (pos_automate[0] - 1)*4] = "2"
        list_hor = self.murs_h
        list_ver = self.murs_v

        for coord in list_hor:
            y = 9-coord[1]
            x = 4+(coord[0]-1)*4
            mat_open[y][x-1] = '-'
            mat_open[y][x] = '-'
            mat_open[y][x+1] = '-'
            mat_open[y][x+2] = '-'
            mat_open[y][x+3] = '-'
            mat_open[y][x+4] = '-'
            mat_open[y][x+5] = '-'

        for coord in list_ver:
            y = y = 9-coord[1]
            x = 4+(coord[0]-1)*4
            mat_line[y][x-2] = '|'
            mat_open[y-1][x-2] = '|'
            mat_line[y-1][x-2] = '|'
        for i in range(len(mat_line)):
            buffer += ''.join(mat_line[i])
            if i < len(mat_open):
                buffer += ''.join(mat_open[i])
        buffer += "--|---------------------------\n"
        buffer += "   | 1  2  3  4  5  6  7  8  9\n"
        write(buffer)
        done()
        return buffer
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



