import argparse
from turtle import *
import Quoridor


class QuoridorX(Quoridor):

    def afficher_graphe():
        super().construire_graphe()
        return (write(graphe))
        done()
        
up()
buffer = "\nLégende: 1=self.nom1, 2= self.nom2\n" #À CHANGER!!!!    
buffer += f"   -----------------------------------\n"
mat_line = []
mat_open = []

for i in range(0, 9):
    mat_line.append(list(f"{(9-i)} |  .    .    .    .    .    .    .    .    .  |\n"))
for i in range(0, 8):
    mat_open.append(list("   |                                             |\n"))
for i in range(len(mat_line)):
    buffer += ''.join(mat_line[i])
    if i < len(mat_open):
        buffer += ''.join(mat_open[i])
buffer += "--|-----------------------------------\n"
buffer += "   | 1   2   3   4   5   6   7   8   9\n"
write(buffer)
done()



def analyser_commande():
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1.')
    parser.add_argument('--lister', help='Lister les identifiants de vos 20 dernières parties.', 
    action = 'store_true')
    parser.add_argument('-a', '--auto', help='Lister les identifiants de vos 20 dernières parties.', 
    action = 'store_true')
    parser.add_argument('-x', '--manugraph', help=' pour jouer en mode manuel contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique.', 
    action = 'store_true')
    parser.add_argument('-ax', '--autoautograph', help='pour jouer en mode automatique contre le serveur avec le nom idul, mais avec un affichage dans une fenêtre graphique.', 
    action = 'store_true')
    parser.add_argument('idul', help=' IDUL du joueur ')
    return parser.parse_args()

print(analyser_commande().idul)
if analyser_commande().auto:
    print('auto')
if analyser_commande().manugraph:
    print('manuel avec affichage graphique')

if analyser_commande().autoautograph:
        print('auto avec affichage graphique')

else: 
    print('manuel')


'''
#Mode auto
def jouer_coup(self, joueur):
        self.joueur = joueur
        if nx.shortest_path(graphe, self.pos1, 'B1') < nx.shortest_path(graphe, self.pos2, 'B2'):
            self.déplacer_jeton(position = p[1])
        else:
            if (self.pos2[0], self.pos2[1]-1) != list(self.murs):
                return self.placer_mur(joueur = 1, position = (self.pos2[0], self.pos2[1]-1), orientation = 'horizontal')
            elif (self.pos2[0], self.pos2[1]-1) == list(self.murs) and (self.pos2[0]-1, self.pos[1]) != list(self.murs):
                return self.placer_mur(joueur = 1, position = (self.pos2[0]-1, self.pos2[1]), orientation = 'vertical')
            elif (self.pos2[0], self.pos2[1]-) == list(self.murs) and (self.pos2[0]-1, self.pos2[1]) == list(self.murs) and (self.pos2[0]+1, self.pos2[1]) != list(self.murs):
                return self.placer_mur(joueur = 1, position = (self.pos2[0]+1, self.pos2[1]), orientation = 'vertical')
        if self.joueur != 0 or self.joueur != 1:
            raise QuoridorError('Le numéro de joueur doit être 1 ou 2.')
        if self.partie_terminée:
            raise QuoridorError('La partie est déjà terminée.')
'''