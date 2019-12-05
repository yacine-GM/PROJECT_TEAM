import argparse


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
