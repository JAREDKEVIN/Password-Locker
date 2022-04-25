import random
import string

class Credentials:
    """
    Class that generates new instances of credentials
    """
    Accountlist= [] #empty credential list

def __init__ (self,account_name,account_username,account_password):
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

def save_credentials(self):

        '''
        test case to test if accounts objects is saved in accountlist
        '''

        Credentials.Accountlist.append(self)

def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credential from the accountlist
        '''

        Credentials.Accountlist.remove(self)

@classmethod
def find_by_account_name(cls,account_name):
            '''
            Method that takes in a account_name and returns a account that matches that account_name.
            Args:
                account_name: user account_name to search for
            Returns :
                user of person that matches the account_name.
            '''

            for credential in cls.Accountlist:
                if credential.account_name == account_name:
                    return credential
