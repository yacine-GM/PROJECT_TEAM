"""Modul API
utilise requests pour faire des requètes sur le site du cours
"""
import requests

URL_BASE = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(idul):
    """Retourne la liste des 20 dernières paries"""
    rep = requests.get(URL_BASE+'lister/', params={'idul': f'{idul}'})
    if rep.status_code == 200:
        rep = rep.json()
        return rep['parties']
    print(f"Le GET sur {URL_BASE+'lister'} a produit le code d'erreur {rep.status_code}.")
    raise RuntimeError

def débuter_partie(idul):
    """Demande au serveur de démarer une partie
    Retourne le ID de la partie et son état initial
    """
    rep = requests.post(URL_BASE+'débuter/', data={'idul': f'{idul}'})
    if rep.status_code == 200:
        rep = rep.json()
        return rep['id'], rep['état']
    print(f"Le GET sur {URL_BASE+'lister'} a produit le code d'erreur {rep.status_code}.")
    raise RuntimeError

def jouer_coup(id_partie, type_coup, position):
    """Effectue le coup indiqué par l'utilisateur
    Retourne l'état suite à la réponse de l'automate
    """
    rep = requests.post(URL_BASE+'jouer/', data={'id': f'{id_partie}', 'type': f'{type_coup}', 'pos': f'{position}'})
    if rep.status_code == 200:
        rep = rep.json()
        if rep['gagnant']:
            print(f"Le gagnant est {rep['gagnant']}")
            raise StopIteration
        else:
            return rep['etat']
    else:
        print(f"Le GET sur {URL_BASE+'lister'} a produit le code d'erreur {rep.status_code}.")
        raise RuntimeError
    