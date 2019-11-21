class Quoridor:

    def __init__(self, joueurs, murs=None):
        if type(joueurs) is str:
            self.nom = joueurs.split()[0]
            self.pos = joueurs.split()[1]
            self.murs = '10'
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
        if int(self.murs1)> 10 or int(self.murs2) > 10 or int(self.murs1)<= 0 or int(self.murs2)<= 0:
            raise IndexError('erreur dans le nombre de murs')
        if (self.pos1)!= [5, 9] and (self.pos2) != [5, 9] or (self.pos2)!= [5, 1] and (self.pos1) != [5, 1]:
            raise IndexError("la position n'est pas valide")
        if type(self.murs) is not dict:
            raise KeyError("la variable mur n'est pas un dictionnaire" )

