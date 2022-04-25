import unittest # Importing the unittest module
from credentials import Credentials
from user import User

class TestCredentials(unittest.TestCase):
    '''hfbhbhfbvhbfhvbhfvb
    '''
    def setUp(self):
        """fhghgithgu"""
        self.new_credentials =Credentials("pintres", "pepe" , "pipi")

def test_init(self):
        "gfhugehthguthgu"

        self.assertEqual(self.new_credentials.account_name,"pintres")
        self.assertEqual(self.new_credentials.account_username,"pepe")
        self.assertEqual(self.new_credentials.account_password,"pipi")

def test_find_by_account_name(self):
        '''
        Test case to check if we can find an account by username and display information
        '''
        self.new_credentials.save_credentials()
        test_account = Credentials("Pintres", "pepe", "pipi")
        test_account.save_credentials()

        found_account = Credentials.find_by_account_name('pepe')
        self.assertEqual(found_account.account_name,test_account.account_name)