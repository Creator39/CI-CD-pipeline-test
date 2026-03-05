from app import Playlist
import pytest

def test_cree_playlist():
    playlist = Playlist("Ma playlist")
    assert playlist.nom == "Ma playlist"
    assert playlist.musiques == []

def test_cree_playlist_nom_vide():
    with pytest.raises(ValueError):
        Playlist("")

def test_ajoute_musique():
    playlist = Playlist("Ma playlist 2")
    playlist.ajoute_musique("Bohemian Rhapsody")
    assert "Bohemian Rhapsody" in playlist.musiques

def test_palylist_nom_dupliquer():
    p1 = Playlist("Rock")
    with pytest.raises(ValueError):
        p2 = Playlist("Rock")