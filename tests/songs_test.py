import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    
    def setUp(self):
        self.title = "Move"
        self.artist = "Taemin"
        self.new_song = "Jump"

    def test_song_has_title(self):
        self.assertEqual("Move", self.title)

    def test_song_has_artist(self):
        self.assertEqual("Taemin", self.artist)

    # def test_add_to_playlist(self):
    #     self.add_songs_to_playlist(self.new_song)
    #     self.assertEqual(1, len(self.playlist))