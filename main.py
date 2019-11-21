"""Module main"""
import argparse

def analyser_commande():
    """Analyse les arguments de la commande d'exécution"""
    parser = argparse.ArgumentParser()
    # On joute le paramètre IDUL
    parser.add_argument(
        "idul", 
        help="IDUL du joueur."
    )
    # On ajoute le paramètre optionnel --lister
    parser.add_argument(
        "-l", "--lister", dest="lister", action='store_true',
        help="Lister les identifiants de vos 20 dernières parties."
    )
    return parser.parse_args()

def afficher_damier_ascii(idul, etat):
    """Affiche le damier à partir de l'état du jeu"""
    # On créer un variable pour entreposer les charactère du damier
    buffer = f"\nLégende: 1={idul}, 2=automate\n"
    buffer += f"   -----------------------------------\n"
    mat_line = []
    mat_open = []
    # On creer une liste contenant les caractères de base pour un 
    # damier de jeu vide
    for i in range(0, 9):
        mat_line.append(list(f"{(9-i)} | .   .   .   .   .   .   .   .   . |\n"))
    for i in range(0, 8):
        mat_open.append(list("  |                                   |\n"))
    #ajouter les pieces des joueurs dans le damier
    pos_joueur = etat["joueurs"][0]["pos"]
    pos_automate = etat["joueurs"][1]["pos"]
    mat_line[9-pos_joueur[1]][4 + (pos_joueur[0] - 1)*4] = "1"
    mat_line[9-pos_automate[1]][4 + (pos_automate[0] - 1)*4] = "2"
    #ajouter les murs dans le damier
    list_hor = etat['murs']['horizontaux']
    list_ver = etat['murs']['verticaux']
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
    print(buffer)

if __name__ == "__main__":
    # On appèle analyser_commande() au démarage pour lire les arguments
    ARGS = analyser_commande()

