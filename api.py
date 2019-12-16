"""Modul API
utilise requests pour faire des requètes sur le site du cours
"""
import requests


def lister_parties(idul):
    """Retourne la liste des 20 dernières paries"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.get(url_base+'lister/', params={'idul': f'{idul}'})
    if rep.status_code == 200:
        rep = rep.json()
        return rep['parties']
    print(f"Le GET sur {url_base+'lister'} a produit le code d'erreur {rep.status_code}.")
    raise RuntimeError

def débuter_partie(idulenchaine):
    "Permet au joueur de débuter une partie avec son idul"
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idulenchaine})
    rep = rep.json()
    if rep.get('message'):
        raise RuntimeError(rep['message'])
    else:
        return (rep['id'], rep['état'])

def jouer_coup(identifiant, coup, posit):
    "permet au joueur de jouer un coup dans sa partie avec le type de coup et le point"
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'jouer/', data={'id': identifiant, 'type': coup, 'pos': posit})
    a = rep.json()
    if a.get('message'):
        raise RuntimeError(a['message'])
    if a.get('gagnant'):
        raise StopIteration(a['gagnant'])
    else:
        return a['état']
