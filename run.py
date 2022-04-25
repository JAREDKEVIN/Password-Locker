#!/usr/bin/env python3
from credentials  import Credentials
from user import User
import random
import string

# functions that implement the behaviours we have created in user
def create_user(first_name,last_name,username,password):
     '''
    Function to create a new user
    '''
new_user = User(first_name,last_name,username,password)
    return  new_user