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

def display_credentials():
    '''
    Function that returns all the saved users
    '''
    return Credentials.display_credentials()

def generate_password():
        '''
        Function to generate a random password
        '''
        password_list = []
        characters_upper = 'abcdefghijklmnopqrstuvwxyz'.upper()
        characters_lower = 'abcdefghijklmnopqrstuvwxyz'.lower()
        numbers = '0123456789'
        symbols = '!@#$%&*'
        for i in range(3):
            password_list.append(random.choice(characters_upper))
            password_list.append(random.choice(characters_lower))
            password_list.append(random.choice(numbers))
            password_list.append(random.choice(symbols))
        passwordgen = ''.join(password_list)
        return passwordgen


def main(): #main function that calls all the other function
    while True:
        print("Hello Welcome to your password-locker. Write signup or login to start")
        print("signup -or- login")
        option = input()
        
    if option == "signup":
        print("Create an account")
        
        print("🔒" *20)
        print("Enter your First name")
        first_name=input()
        print("Enter your Last name")
        last_name=input()
        print("Enter your Username")
        username=input()
        print("Set your password")
        password=input()
        print("\n")

save_user(create_user(first_name, last_name, username, password))

        print("Your accout was succesfully created.These are you details")
        print("🔒" *20)
                
        print(f"Name:{first_name} {last_name} \nUsername: {username} \nPassword: {password}")
        print("Login into your account with these details")





