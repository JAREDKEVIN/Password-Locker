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

def save_user(User):
    '''
    Function to save user
    '''
    User.save_user()

def delete_user(User):
    '''
    Function to delete a user
    '''
    User.delete_user()

def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_by_password(password)

def check_existing_user(username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return User.user_exist(username)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

# functions that implement the behaviours we have created in credentials
def create_account(account_name,account_username,account_password):
    '''
    Function to create a new account
    '''
    new_credentials = Credentials(account_name,account_username,account_password)
    return new_credentials

def save_credentials(Credentials):
    '''
    Function to save user
    '''
    Credentials.save_credentials()

def delete_credentials(Credentials):
    '''
    Function to delete a user
    '''
    Credentials.delete_credentials()

def find_account(account_name):
    '''
    Function that finds a user by password and returns the user
    '''
    return Credentials.find_by_account_name (account_name)

def check_existing_account(account_username):
    '''
    Function that check if a user exists with that username and return a Boolean
    '''
    return Credentials.account_exist(account_username)





