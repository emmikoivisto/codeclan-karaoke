import unittest
from src.room import Room
from src.songs import Songs


class TestRoom(unittest.TestCase):
    def setUp(self):
         self.room_name = Room("Dungeon")
         self.song_to_add_1 = Songs("Move", "Taemin")
         self.guest_1 = Guest("Tim", 30)
         self.guest_2 = Guest("John", 18)
         self.new_guests = 

    def test_room_has_name(self):
        self.assertEqual("Dungeon", self.room_name.name)
    
    def test_playlist_has_songs(self):
         self.room_name.add_songs_to_playlist(self.song_to_add_1)
         self.assertEqual(1, len(self.room_name.playlist))

    def test_room_has_guestlist(self):
        self.assertEqual()