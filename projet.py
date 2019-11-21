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

a= {"joueurs": [{"nom": "idul", "murs": 7, "pos": [5, 9]}, {"nom": "automate", "murs": 3, "pos": [5, 1]}],
 "murs": {"horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
 "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]}}#juste pour tester
b = Quoridor(a)#juste pour tester
print(b) #juste pour tester