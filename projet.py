import networkx as nx
import api
import main

class Quoridor:
    
    
    def __init__(self, joueurs, murs = None):
        if type(joueurs) is str:
            self.nom = joueurs.split()[0]
            self.pos = joueurs.split()[1]
            self.murs = '10'
            for i, j in enumerate(joueurs):
                if i>1:
                    raise IndexError('le jeu accepte pas plue que 2 joueurs ')#si l'itérable de joueurs en contient plus de deux
        if type(joueurs) is dict:
            self.nom1= joueurs['joueurs'][0]['nom']
            self.pos1 = joueurs['joueurs'][0]['pos']
            self.murs1 = joueurs['joueurs'][0]['murs']
            self.nom2= joueurs['joueurs'][1]['nom']
            self.pos2 = joueurs['joueurs'][1]['pos']
            self.murs2 = joueurs['joueurs'][1]['murs']
            self.murs = joueurs['murs']
            self.murs_h = joueurs['murs']['horizontaux']
            self.murs_v = joueurs['murs']['verticaux']    
        try:
            joueurs = iter(joueurs)
        except TypeError: 
            raise TypeError('QuoridorError')#si joueurs n'est pas itérable
        if 10 <self.murs1< 0 or 10 <self.murs2< 0 :
            raise IndexError('erreur dans le nombre de murs')#si le nombre de murs qu'un joueur peut placer est >10, ou négatif.
        #if (self.pos1)!= [5, 9] or (self.pos2) != [5, 1] :
           # raise IndexError("la position n'est pas valide")#si la position d'un joueur est invalide
        if (10- int(self.murs1) + 10 - int(self.murs2))> 20:
            raise IndexError('les nombre de murs est incorrecte ')#si le total des murs placés et plaçables n'est pas égal à 20
        if type(self.murs) is not dict:
            raise KeyError("la variable mur n'est pas un dictionnaire" )#si murs n'est pas un dictionnaire lorsque présent

    def __str__(self):           
        buffer = f"\nLégende: 1={self.nom1}, 2={self.nom2}\n"
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
        return(buffer)

    def déplacer_jeton(self, joueur, position):
        self.joueur = int(joueur)
        if self.joueur ==1:
            self.pos1 = position
        else:
            self.pos2 = position
        if 2<(self.joueur)<1 : 
            raise IndexError('numéro du joueur pas valide')
        if 9<int(position[0])<1 and 9<int(position[1])<1:
            raise IndexError('position pas valdie')
    
    def état_partie(self):
        V = []
        H = []
        H += self.murs_h
        V += self.murs_v
        F = {'joueurs': [{'nom': self.nom1, 'murs': 10 - int(self.murs1), 'pos':self.pos1 },
                {'nom': self.nom2, 'murs': 10 - int(self.murs2), 'pos': self.pos2}], 'murs': {'horizontaux': H, 'verticaux': V}}    
        return F

    def jouer_coup(self, joueur):
        
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
            if murs_horizontaux !=[]:
        
                for x, y in murs_horizontaux:
                    graphe.remove_edge((x, y-1), (x, y))
                    graphe.remove_edge((x, y), (x, y-1))
                    graphe.remove_edge((x+1, y-1), (x+1, y))
                    graphe.remove_edge((x+1, y), (x+1, y-1))
            if murs_horizontaux !=[]:
                for x, y in murs_verticaux:
                    graphe.remove_edge((x-1, y), (x, y))
                    graphe.remove_edge((x, y), (x-1, y))
                    graphe.remove_edge((x-1, y+1), (x, y+1))
                    graphe.remove_edge((x, y+1), (x-1, y+1))

            for joueur in map(tuple, joueurs):

                for prédécesseur in list(graphe.predecessors(joueur)):
                    graphe.remove_edge(prédécesseur, joueur)

                successeur = (2*joueur[0]-prédécesseur[0], 2*joueur[1]-prédécesseur[1])

            if successeur in graphe.successors(joueur) and successeur not in joueurs:
                graphe.add_edge(prédécesseur, successeur)

            else:
                for successeur in list(graphe.successors(joueur)):
                    if prédécesseur != successeur and successeur not in joueurs:
                        graphe.add_edge(prédécesseur, successeur)

            for x in range(1, 10):
                graphe.add_edge((x, 9), 'B1')
                graphe.add_edge((x, 1), 'B2')
            p = nx.shortest_path(graphe, self.pos1, 'B1')
            self.pos1 = p[1]
            return (self.pos1)
        construire_graphe(self.pos1, self.murs_h,self.murs_v)
        return(construire_graphe)
        
    def placer_mur(self, joueur, position, orientation):    
        self.position = (x, y)
        self.joueur = int(joueur)
        état["joueurs"][joueur]["murs"] += 1
        if self.orientation == "horizontaux" or "verticaux":
            return ((état['murs'][orientation]).append(position))
        return(état) #retourne la nouvelle forme de l'état avec le nouveau mur
        graphe =  construire_graphe([joueur['pos'] for joueur in état['joueurs']], état['murs']['horizontaux'],état['murs']['verticaux'])
        if self.joueur != 0 or self.joueur != 1:
                raise TypeError('QuoridorError')
        if self.position in list(état['murs'][self.orientation]) == 1:
            raise TypeError('QuoridorError') 
        #if  self.position != #je n'arrive pas a trouvé pour l'erreur d'orientation
            #raise TypeError('QuoridorError') 
        if (état[["joueurs"][joueur]["murs"]]):
            raise TypeError('QuoridorError') 
        print(graphe = construire_graphe([joueur['pos'] for joueur in état['joueurs']], état['murs']['horizontaux'],état['murs']['verticaux']))

        """
        if self.joueur == 1: #une autre manière avec les variables de def etat_partie mais je suis pas sur que ça marche 
            if orientation == 'horizontal':
                self.orientation = self.murs_h
            return (H.append(self.position) and (int(murs2)).add(1))
            if orientation == 'vertical':
                self.orientation == self.murs_v
            return(V.append(self.possition) and ((int(murs2)).add(1))) 

        if self.joueur == 0:
            if orientation == 'horizontal':
                self.orientation = self.murs_h
            return (H.append(self.position) and (int(murs1)).add(1))
            if orientation == 'vertical':
                self.orientation == self.murs_v
            return(V.append(self.possition) and ((int(murs1)).add(1)))

        raise TypeError('QuoridorError') if self.joueur != 0 or 1
        raise TypeError('QuoridorError') if self.position == i for i in list(H) or self.position == v for v in list(V)
        raise TypeError('QuoridorError') if  self.position 
        raise TypeError('QuoridorError') if (10 - int(self.murs1) == 0) or (10 - int(self.murs2)) == 0
    """
    def partie_terminée(self):
        if self.pos1 == (5,1):
            return (print(f'Le gagnant est {idul}'))
        if self.pos2 == (5,9):
            return (print("Le gagnant est l'automate"))
        else:
            return False

a= {"joueurs": [{"nom": "idul", "murs": 7, "pos": [5, 9]}, {"nom": "automate", "murs": 3, "pos": [5, 1]}], "murs": {"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]}}
b = Quoridor(a)
print(b)

état = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 6]},
        {"nom": "automate", "murs": 3, "pos": [5, 7]}
    ],
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
        "verticaux": [[6, 2], [4, 4], [2, 5], [7, 5], [7, 7]]
    }
}
