import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self, name, age):
        self.customer = ("Jack", 25)