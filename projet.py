class Quoridor:

    def __init__(self, joueurs, murs=None):
        if type(joueurs) is str:
            self.nom1 = joueurs.split()[0][0]
            self.pos1 = joueurs.split()[0][1]
            self.murs1i = joueurs.split()[0][2]
            self.nom2 = joueurs.split()[1][0]
            self.pos2 = joueurs.split()[1][1]
            self.murs2i = joueurs.split()[1][2]

        if type(joueurs) is dict:
            self.id1= joueurs['joueurs'][0]['nom']
            self.pos1 = joueurs['joueurs'][0]['pos']
            self.murs1 = joueurs['joueurs'][0]['murs']
            self.id2= joueurs['joueurs'][1]['nom']
            self.pos2 = joueurs['joueurs'][1]['pos']
            self.murs2 = joueurs['joueurs'][1]['murs']
            self.murs = joueurs['murs']
            self.murs_h = joueurs['murs']['horizontaux']
            self.murs_v = joueurs['murs']['verticaux']
        try:
            joueurs = iter(joueurs)
        except TypeError: 
            raise TypeError('QuoridorError')#si joueurs n'est pas itérable
        if int(self.murs1)> 10 or int(self.murs2) > 10 or int(self.murs1)<= 0 or int(self.murs2)<= 0:
            raise IndexError('erreur dans le nombre de murs')#si le nombre de murs qu'un joueur peut placer est >10, ou négatif.
        if (self.pos1)!= [5, 9] and (self.pos2) != [5, 9] or (self.pos2)!= [5, 1] and (self.pos1) != [5, 1]:
            raise IndexError("la position n'est pas valide")#si la position d'un joueur est invalide
        if type(self.murs) is not dict:
            raise KeyError("la variable mur n'est pas un dictionnaire" )#si murs n'est pas un dictionnaire lorsque présent
        for i, j in enumerate(joueurs['joueurs']):
            if i>1:
                raise IndexError('le jeu accepte as plue que 2 joueurs ')#si l'itérable de joueurs en contient plus de deux
        if (int(self.murs1i)- int(self.murs1) + int(self.murs2i) - int(self.murs2))> 20:
            raise IndexError('les nombre de murs est incorrecte ')#si le total des murs placés et plaçables n'est pas égal à 20

    def __str__(self):
        A = (f' legende : 1  2 = automate')
        B = ('   -----------------------------------')
        TAB = [[' 'for i in range(39)]for j in range(17)]
        for i, j in enumerate(TAB[::2]):
                j[0] = str(9-i)
                j[2] = '|'
                j[38] = '|'
                for L in range(4, 39, 4):
                    j[L] = '.'
        for j in TAB[1::2]:
            j[2] = j[38] = '|'
        TAB0 = []
        for j in TAB:
            TAB0 = TAB0 + j +['\n']
        TAB0.pop()
        TAB = list(TAB0)
        TAB0[(18-(int(self.pos1[1]))*2)*40+ 4 *(int(self.pos1[0]))] = '2'
        TAB0[(18-(int(self.pos2[1]))*2)*40 + 4 *(int(self.pos2[0]))] = '1'
        C = (''.join(TAB0))
        D = ('--|-----------------------------------')
        E = ('  | 1   2   3   4   5   6   7   8   9')
        return A+ '\n' + B+'\n' +C+'\n' +D + '\n' + E

    def déplacer_jeton(self, joueur, position):
        self.joueur = int(joueur)
        if self.joueur ==1:
            self.pos1 = position
        else:
            self.pos2 = position
        if 2<(self.joueur)<1 : 
            raise IndexError('numéro du joueur pas valide')
        if 9<int(self.position[0])<1 and 9<int(self.position[1])<1:
            raise IndexError('position pas valdie')

    def état_partie(self):
        return {
    'joueurs': [{'nom': self.nom1, 'murs': int(self.murs1i) - int(self.murs1), 'pos':self.pos1 },
        {'nom': self.nom2, 'murs': int(self.murs2i) - int(self.murs2), 'pos': self.pos2}], 'murs': {'horizontaux': self.murs_h, 'verticaux': self.murs_v}}



#a= {"joueurs": [{"nom": "idul", "murs": 7, "pos": [5, 9]}, {"nom": "automate", "murs": 3, "pos": [5, 1]}],
# "murs": {"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
# "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]}}#juste pour tester
#b = Quoridor(a)#juste pour tester
#print(b) #juste pour tester



import networkx as nx


def construire_graphe(self,joueurs, murs_horizontaux, murs_verticaux):
    self.joueur = (self.pos1, self.pos2)
    self.murs_horizontaux = (list(self.murs_h))
    self.murs_verticaux = (list(self.murs_v))
    graphe = nx.DiGraph()
    for x in range(1, 10):
        if x > 1:
            graphe.add_edge((x, y), (x-1, y))
        if x < 9:
            graphe.add_edge((x,y), (x+1, y))
        if y > 1:
            graphe.add_edge((x, y), (x, y-1))
        if y > 9:
            graphe.add_edge((x,y), (x, Y+1))
    for x,y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x, y+1), (x-1, Y+1))
        graphe.remove_edge((x-1, y+1), (x, y+1))
    for joueur in map(tuple,joueurs):
        for prédécesseur in list(graphe.predessors(joueur)):
            graphe.remove_edge(prédécesseur, joueur)
            successeur = (2*joueur[0] - prédécesseur[0], 2*joueur[1] - prédécesseur[1])
            if successeur in graphe.successors(joueur) and successeur not in joueurs: 
                graphe.add_edge(prédécesseur, successeur)
            else:
                 for successeur in list(graphe.successors(joueur)):
                    if prédécesseur != successeur and successeur not in joueurs:
                        graphe.add_edge(prédécesseur, successeur)
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe

def joueur_coup(self, joueur):#mmh je crois que 
    self.joueur = int(joueur)
    if self.joueur == 1:
        if nx.has_path(graphe, pos1, 'B1') < nx.has_path(graphe, pos2, 'B2'):
            return déplacer_jeton(self, joueur, position = nx.shortest_path(graphe, pos1, 'B1'))
        else:
            return placer_mur()
    if self.joueur == 2:
        if nx.has_path(graphe, pos2, 'B2') < nx.has_path(graphe, pos1, 'B1'):
            return déplacer_jeton(self, joueur, position = nx.shortest_path(graphe, pos2, 'B2'))
        else:
            return placer_mur()

