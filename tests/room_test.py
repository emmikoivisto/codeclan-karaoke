import unittest
from src.room import Room
from src.songs import Songs
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
         self.song_to_add_1 = Songs("Move", "Taemin")
         self.guest_1 = Guest("Tim", 30)
         self.guest_2 = Guest("John", 18)
         new_guests = [self.guest_1, self.guest_2]
         self.room = Room("Jam Jar", new_guests)

    def test_room_has_name(self):
        self.assertEqual("Jam Jar", self.room.name)
    
    def test_playlist_has_songs(self):
         self.room.add_songs_to_playlist(self.song_to_add_1)
         self.assertEqual(1, len(self.room.playlist))

    def test_room_has_guestlist(self):
        self.assertEqual(2, self.room.guest_count())

    def test_add_guest(self):
        guest_3 = Guest("Jess", 28)
        self.room.add_guest_to_guestlist(guest_3)
        self.assertEqual(3, self.room.guest_count())
