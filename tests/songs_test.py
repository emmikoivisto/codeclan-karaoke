import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):
    
    def setUp(self):
        self.title = "Move"
        self.artist = "Taemin"

    def test_song_has_title(self):
        self.assertEqual("Move", self.title)