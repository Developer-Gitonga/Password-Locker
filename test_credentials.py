import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new = Credential("Gitonga","Redcarpet", "Twiiter", 1233)

    def tearDown(self):
        Credential.accounts = []

    def test_init(self):
        self.assertEqual(self.new.username, "Gitonga")
        self.assertEqual(self.new.password, "Redcarpet")
        self.assertEqual(self.new.account_name, "Twiiter")
        self.assertEqual(self.new.account_key, 1233)

if __name__=="__main__":
    unittest.main()
