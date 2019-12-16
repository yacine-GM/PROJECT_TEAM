import networkx as nx



class QuoridorError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return str(self.message)
class Quoridor:


    def __init__(self, joueurs):
        if type(joueurs) is str:
            self.nom1 = joueurs[0]
            self.nom2 = joueurs[1]
            for i in enumerate(joueurs):
                if i > 1:#si l'itérable de joueurs en contient plus de deux
                    raise QuoridorError('Le jeu accepte pas plus de 2 joueurs.')
        if type(joueurs) is dict:
            self.id1 = joueurs['joueurs'][0]['nom']
            self.pos1 = joueurs['joueurs'][0]['pos']
            self.murs1 = joueurs['joueurs'][0]['murs']
            self.id2 = joueurs['joueurs'][1]['nom']
            self.pos2 = joueurs['joueurs'][1]['pos']
            self.murs2 = joueurs['joueurs'][1]['murs']
            self.murs = joueurs['murs']
            self.murs_h = joueurs['murs']['horizontaux']
            self.murs_v = joueurs['murs']['verticaux']
        if joueurs == iter(joueurs):
            raise QuoridorError("Le joueur spécifié n'est pas un itérable.")
        if 10 < self.murs1 < 0 or 10 < self.murs2 < 0:
            raise QuoridorError('Le nombre de mur est impossible.')
        if self.pos1 != [5, 1] or self.pos2 != [5, 9]:
            raise QuoridorError("La position d'un joueur n'est pas valide.")
        if (10- int(self.murs1) + 10 - int(self.murs2)) > 20:
            raise QuoridorError('Le nombre de mur est impossible.')
        if type(self.murs) is not dict:
            raise QuoridorError("La variable mur n'est pas un dictionnaire.")
        #if self.Murs position impossible:
            #raise QuoridorError("La position du mur donné n'est pas valide")


    def __str__(self):
        buffer = "\nLégende: 1=self.nom1, 2= self.nom2\n" #À CHANGER!!!!
        buffer += f"   -----------------------------------\n"
        mat_line = []
        mat_open = []

        for i in range(0, 9):
            mat_line.append(list(f"{(9-i)} | .   .   .   .   .   .   .   .   . |\n"))
        for i in range(0, 8):
            mat_open.append(list("  |                                   |\n"))
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
        buffer += "--|-----------------------------------\n"
        buffer += "  | 1   2   3   4   5   6   7   8   9\n"
        return buffer

    def déplacer_jeton(self, joueur, position):
        self.joueur = int(joueur)
        self.pos1 = position
        if self.joueur == 1:
            self.pos1 = position
        else:
            self.pos2 = position
        if 2 < (self.joueur) < 1:
            raise QuoridorError('numéro du joueur pas valide.')
        if 9 < int(position[0]) < 1 and 9 < int(position[1]) < 1:
            raise QuoridorError('position pas valide.')
        if self.position != self.pos1:
            raise QuoridorError("La positione entrée n'est pas conforme à l'état de la partie.")

    def état_partie(self):
        v = []
        h = []
        h += self.murs_h
        v += self.murs_v
        f = {'joueurs': [
            {'nom': self.nom1, 'murs': 10 - int(self.murs1), 'pos':self.pos1},
            {'nom': self.nom2, 'murs': 10 - int(self.murs2), 'pos': self.pos2}],
             'murs': {'horizontaux': h, 'verticaux': v}}
        return f

    def jouer_coup(self, joueur):
        self.joueur = joueur
        if self.pos1 < self.pos2:
            return(déplacer_jeton())
        else:
            return(placer_mur())
        if self.joueur != 0 or self.joueur != 1:
            raise QuoridorError('Le numéro de joueur doit être 1 ou 2.')
        if self.partie_terminée:
            raise QuoridorError('La partie est déjà terminée.')

        def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
            graphe = nx.DiGraph()
            for x in range(1, 10):
                for y in range(1, 10):
                    if x > 1:
                        graphe.add_edge((x, y), (x-1, y))
                    if x < 9:
                        graphe.add_edge((x, y), (x+1, y))
                    if y > 1:
                        graphe.add_edge((x, y), (x, y-1))
                    if y < 9:
                        graphe.add_edge((x, y), (x, y+1))
            for x, y in murs_horizontaux:
                graphe.remove_edge((x, y-1), (x, y))
                graphe.remove_edge((x, y), (x, y-1))
                graphe.remove_edge((x+1, y-1), (x+1, y))
                graphe.remove_edge((x+1, y), (x+1, y-1))
            for x, y in murs_verticaux:
                graphe.remove_edge((x-1, y), (x, y))
                graphe.remove_edge((x, y), (x-1, y))
                graphe.remove_edge((x-1, y+1), (x, y+1))
                graphe.remove_edge((x, y+1), (x-1, y+1))

            j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])
            if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):
                graphe.remove_edge(j1, j2)
                graphe.remove_edge(j2, j1)
                
                def ajouter_lien_sauteur(noeud, voisin):
                    saut = 2*voisin[0]-noeud[0], 2*voisin[1]-noeud[1]
                    if saut in graphe.successors(voisin):
                        graphe.add_edge(noeud, saut)
                    else:
                        for saut in graphe.successors(voisin):
                            graphe.add_edge(noeud, saut)
                ajouter_lien_sauteur(j1, j2)
                ajouter_lien_sauteur(j2, j1)

            for x in range(1, 10):
                graphe.add_edge((x, 9), 'B1')
                graphe.add_edge((x, 1), 'B2')
            p = nx.shortest_path(graphe, self.pos1, 'B1')
            self.pos1 = p[1]
            return self.pos1

        construire_graphe(self.pos1, self.murs_h, self.murs_v)
        return construire_graphe

    def partie_terminée(self):
        if self.pos1 == ('B1'):
            return print(f'Le gagnant est {self.nom1}')
        if self.pos2 == ('B2'):
            return print(f'Le gagnant est {self.nom2}')

    def placer_mur(self, joueur, position, orientation):
        self.joueur = int(joueur)
        if self.joueur == 1:
            self.position = position
            if orientation == 'horizontal':
                self.murs_h = self.position
                if orientation != self.murs_h:
                    raise QuoridorError("L'orientation n'est pas valide.")
            if orientation == 'vertical':
                self.murs_v = self.position
                if orientation != self.murs_v:
                    raise QuoridorError("L'orientation n'est pas valide.")

            if self.joueur != 0 or self.joueur != 1:
                raise QuoridorError('Le numéro du joueur doit être 1 ou 2.')
            if self.position == list(self.murs):
                raise QuoridorError('Un mur occupe déjà cette position.')
            if  10 - int(self.murs1) == 0:
                raise QuoridorError('Les murs sont tous placés.')
            if  10 - int(self.murs2) == 0:
                raise QuoridorError('Les murs sont tous placés.')
