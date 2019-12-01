import networkx as nx


class QuoridorError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return str(self.message)
class Quoridor:


    def __init__(self, Joueurs, Murs = None):
        if type(Joueurs) is str:
            self.nom1 = Joueurs[0]
            self.nom2 = Joueurs[1]
            for i, j in enumerate(Joueurs):
                if i > 1:#si l'itérable de joueurs en contient plus de deux
                    raise QuoridorError('Le jeu accepte pas plus de 2 joueurs.')
        if type(Joueurs) is dict:
            self.id1 = Joueurs['joueurs'][0]['nom']
            self.pos1 = Joueurs['joueurs'][0]['pos']
            self.murs1 = Joueurs['joueurs'][0]['murs']
            self.id2 = Joueurs['joueurs'][1]['nom']
            self.pos2 = Joueurs['joueurs'][1]['pos']
            self.murs2 = Joueurs['joueurs'][1]['murs']
            self.Murs = Joueurs['murs']
            self.murs_h = Joueurs['murs']['horizontaux']
            self.murs_v = Joueurs['murs']['verticaux']    
        if Joueurs == iter(Joueurs):
            raise QuoridorError("Le joueur spécifié n'est pas un itérable.")
        if 10 < self.murs1 < 0 or 10 < self.murs2 < 0:
            raise QuoridorError('Le nombre de mur est impossible.')#si nbr mur placé est>10,ou négatif
        if self.pos1 != [5, 1] or self.pos2 != [5, 9]:
            raise QuoridorError("La position d'un joueur n'est pas valide.")#si la pos d'un joueur est invalide
        if (10- int(self.murs1) + 10 - int(self.murs2)) > 20:
            raise QuoridorError('Le nombre de mur est impossible.')#si le total des murs placés et plaçables n'est pas égal à 20
        if type(self.Murs) is not dict:
            raise QuoridorError("La variable mur n'est pas un dictionnaire.")#si murs n'est pas un dictionnaire lorsque présent
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

    def Déplacer_jeton(self, Joueur, Position):
        self.Joueur = int(Joueur)
        self.pos1 = Position
        if self.Joueur == 1:
            self.pos1 = Position
        else:
            self.pos2 = Position
        if 2 < (self.Joueur) < 1:
            raise QuoridorError('numéro du joueur pas valide.')
        if 9 < int(Position[0]) < 1 and 9 < int(Position[1]) < 1:
            raise QuoridorError('position pas valide.')
        if self.Position != self.pos1:
            raise QuoridorError("La positione entrée n'est pas conforme à l'état de la partie.")

    def État_partie(self):
        V = []
        H = []
        H += self.murs_h
        V += self.murs_v
        F = {'joueurs': [{'nom': self.nom1, 'murs': 10 - int(self.murs1), 'pos':self.pos1}, 
        {'nom': self.nom2, 'murs': 10 - int(self.murs2), 'pos': self.pos2}], 'murs': {'horizontaux': H, 'verticaux': V}}
        return F

    def Jouer_coup(self, Joueur):

        if self.pos1 < self.pos2:
            self.Déplacer_jeton
        else:
            self.Placer_mur
        if self.Joueur != 0 or self.Joueur != 1:
            raise QuoridorError('Le numéro de joueur doit être 1 ou 2.')
        if self.Partie_terminée:
            raise QuoridorError('La partie est déjà terminée.')

        def Construire_graphe(Joueurs, Murs_horizontaux, Murs_verticaux):
            Graphe = nx.DiGraph()
            for x in range(1, 10):
                for y in range(1, 10):
                    if x > 1:
                        Graphe.add_edge((x, y), (x-1, y))
                    if x < 9:
                        Graphe.add_edge((x, y), (x+1, y))
                    if y > 1:
                        Graphe.add_edge((x, y), (x, y-1))
                    if y < 9:
                        Graphe.add_edge((x, y), (x, y+1))

            for x, y in Murs_horizontaux:
                Graphe.remove_edge((x, y-1), (x, y))
                Graphe.remove_edge((x, y), (x, y-1))
                Graphe.remove_edge((x+1, y-1), (x+1, y))
                Graphe.remove_edge((x+1, y), (x+1, y-1))
            for x, y in Murs_verticaux:
                Graphe.remove_edge((x-1, y), (x, y))
                Graphe.remove_edge((x, y), (x-1, y))
                Graphe.remove_edge((x-1, y+1), (x, y+1))
                Graphe.remove_edge((x, y+1), (x-1, y+1))

            for Joueur in map(tuple, Joueurs):

                for Prédécesseur in list(Graphe.Predecessors(Joueur)):
                    Graphe.remove_edge(Prédécesseur, Joueur)

                Successeur = (2*Joueur[0]-Prédécesseur[0], 2*Joueur[1]-Prédécesseur[1])

            if Successeur in Graphe.Successors(Joueur) and Successeur not in Joueurs:
                Graphe.add_edge(Prédécesseur, Successeur)

            else:
                for Successeur in list(Graphe.Successors(Joueur)):
                    if Prédécesseur != Successeur and Successeur not in Joueurs:
                        Graphe.add_edge(Prédécesseur, Successeur)

            for x in range(1, 10):
                Graphe.add_edge((x, 9), 'B1')
                Graphe.add_edge((x, 1), 'B2')
            P = nx.shortest_path(Graphe, self.pos1, 'B1')
            self.pos1 = P[1]
            return self.pos1

        Construire_graphe(self.pos1, self.murs_h, self.murs_v)
        return Construire_graphe

    def Partie_terminée(self):
        if self.pos1 == ('B1'):
            return print(f'Le gagnant est {self.nom1}')
        if self.pos2 == ('B2'):
            return print(f'Le gagnant est {self.nom2}')
        else:
            return False

    def Placer_mur(self, Joueur, Position, Orientation):
        self.Joueur = int(Joueur)
        if self.Joueur == 1:
            self.Position = Position
            if Orientation == 'horizontal':
                self.murs_h = self.Position
                if Orientation != self.murs_h:
                    raise QuoridorError("L'orientation n'est pas valide.")
            if Orientation == 'vertical':
                self.murs_v = self.Position
                if Orientation != self.murs_v:
                    raise QuoridorError("L'orientation n'est pas valide.")

            if self.Joueur != 0 or self.Joueur != 1:
                raise QuoridorError('Le numéro du joueur doit être 1 ou 2.')
            if self.Position == list(self.Murs):
                raise QuoridorError('Un mur occupe déjà cette position.')
            if  10 - int(self.murs1) == 0:
                raise QuoridorError('Les murs sont tous placés.')
            if  10 - int(self.murs2) == 0:
                raise QuoridorError('Les murs sont tous placés.')
"""
test = nx.shortest_path(graphe, (5, 1), 'B1')
print(test)

#def __seterpos__(self, pos1, pos2):
    #self.pos1= 

#changer toutes les noms de variables en majuscules
#la ligne ne doit pas >100 
#gestion des erreurs
#classe avec les erreurs (classe QuoridorError qui hérite de Exception)


class MonErreur(Exception):
    pass # ici on hérite du comportement pas défaut
    
def action(test):
     if test:
         raise MonErreur('erreur très spéciale')
     return 'action normale'
     a= {"joueurs": [{"nom": "idul", "murs": 10, "pos": [5, 1]}, {"nom": "automate", "murs": 10, "pos": [5, 9]}], "murs": {"horizontaux": [], "verticaux": []}}
b = Quoridor(a)
print(b)
"""