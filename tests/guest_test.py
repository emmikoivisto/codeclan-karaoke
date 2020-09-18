import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Jack", 25)
    
    def test_guest_has_name(self):
        self.assertEqual("Jack", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(25, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual([], self.guest.money)