import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new = User("Gitonga", "Redcarpet")

    def test_init(self):
        self.assertEqual(self.new.username, "Gitonga")
        self.assertEqual(self.new.password, "Redcarpet")

    def tearDown(self):
        User.users = []
        
