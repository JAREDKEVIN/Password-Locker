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

        class TestUser(unittest.TestCase): #subclass class that inherits from unittest.TestCase


'''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
 '''

#user account
def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.UserList = []



def setUp(self): #first test, test to see if our objects are being instantiated correctly.
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Tracy","Sareto","Tate","Tracy@2022") # create user object

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Tracy")
        self.assertEqual(self.new_user.last_name,"Sareto")
        self.assertEqual(self.new_user.username,"Tate")
        self.assertEqual(self.new_user.password,"Tracy@2022")


def test_save_user(self): #second test
        ''' test case to test if user objects is saved in UserList'''  
        self.new_user.save_user() 
        self.assertEqual(len(User.UserList),1) 
