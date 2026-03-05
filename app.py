playlist_existante = []

class Playlist:
    def __init__(self, nom):
        if not nom:
            raise ValueError("Le nom ne peut pas etre vide.")
        if nom in playlist_existante:
            raise ValueError("Une playlist avec ce nom existe deja.")
        self.nom = nom
        self.musiques = []
        playlist_existante.append(nom)
    
    def ajoute_musique(self, musique):
        self.musiques.append(musique)
